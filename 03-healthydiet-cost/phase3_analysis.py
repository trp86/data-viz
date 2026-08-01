import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

print("="*100)
print("PHASE 3: ANALYSIS")
print("="*100)

# Load cleaned dataset
print("\n[3.1] Loading cleaned dataset...")
df = pd.read_csv("output/cleaned_unable_to_afford_healthy_diet.csv")
print(f"Loaded: {len(df):,} records")

# ANALYSIS 1: Basic Summary
print("\n" + "="*100)
print("[3.2] BASIC SUMMARY")
print("="*100)

num_countries = df['REF_AREA_LABEL'].nunique()
min_year = df['TIME_PERIOD'].min()
max_year = df['TIME_PERIOD'].max()
num_records = len(df)
unit = df['UNIT_MEASURE_LABEL'].iloc[0] + " (" + df['UNIT_MULT_LABEL'].iloc[0] + ")"

print(f"Number of countries/economies: {num_countries}")
print(f"Minimum year: {min_year}")
print(f"Maximum year: {max_year}")
print(f"Total years: {max_year - min_year + 1}")
print(f"Number of records: {num_records:,}")
print(f"Unit used: {unit}")

# ANALYSIS 2: Latest Year Analysis
print("\n" + "="*100)
print("[3.3] LATEST YEAR ANALYSIS")
print("="*100)

latest_year = df['TIME_PERIOD'].max()
print(f"Latest available year: {latest_year}")

df_latest = df[df['TIME_PERIOD'] == latest_year].copy()
df_latest = df_latest.sort_values('OBS_VALUE', ascending=False)

print(f"\nTotal people unable to afford healthy diet in {latest_year}: {df_latest['OBS_VALUE'].sum():,.1f} million")
print(f"That's {df_latest['OBS_VALUE'].sum()/1000:.2f} BILLION people!\n")

# Top 20 countries
print(f"--- TOP 20 COUNTRIES ({latest_year}) ---")
top20_latest = df_latest.head(20).copy()
top20_latest['Rank'] = range(1, len(top20_latest) + 1)
top20_latest['% of Global'] = (top20_latest['OBS_VALUE'] / df_latest['OBS_VALUE'].sum() * 100).round(2)
top20_latest_export = top20_latest[['Rank', 'REF_AREA', 'REF_AREA_LABEL', 'OBS_VALUE', '% of Global']]
print(top20_latest_export.to_string(index=False))

# Save top 20
top20_latest_export.to_csv("output/latest_year_top20.csv", index=False)
print(f"\nSaved: output/latest_year_top20.csv")

# Bottom 20 countries
print(f"\n--- BOTTOM 20 COUNTRIES ({latest_year}) ---")
bottom20_latest = df_latest.tail(20)[['REF_AREA', 'REF_AREA_LABEL', 'OBS_VALUE']].sort_values('OBS_VALUE')
print(bottom20_latest.to_string(index=False))

# ANALYSIS 3: Change Over Time
print("\n" + "="*100)
print("[3.4] CHANGE OVER TIME")
print("="*100)

first_year = df['TIME_PERIOD'].min()
print(f"Comparing {first_year} vs {latest_year}")

df_first = df[df['TIME_PERIOD'] == first_year][['REF_AREA_LABEL', 'OBS_VALUE']].rename(columns={'OBS_VALUE': f'Value_{first_year}'})
df_last = df[df['TIME_PERIOD'] == latest_year][['REF_AREA_LABEL', 'OBS_VALUE']].rename(columns={'OBS_VALUE': f'Value_{latest_year}'})

df_change = pd.merge(df_first, df_last, on='REF_AREA_LABEL', how='outer')
df_change['Absolute_Change'] = df_change[f'Value_{latest_year}'] - df_change[f'Value_{first_year}']

# Calculate percentage change (handle zeros)
def calc_pct_change(row):
    if pd.isna(row[f'Value_{first_year}']) or row[f'Value_{first_year}'] == 0:
        return np.nan
    return ((row[f'Value_{latest_year}'] - row[f'Value_{first_year}']) / row[f'Value_{first_year}'] * 100)

df_change['Percentage_Change'] = df_change.apply(calc_pct_change, axis=1)

# Save change summary
df_change_export = df_change.sort_values('Absolute_Change', ascending=False)
df_change_export.to_csv("output/country_change_summary.csv", index=False)
print(f"Saved: output/country_change_summary.csv")

# Biggest increases
print(f"\n--- TOP 10 BIGGEST INCREASES ({first_year} to {latest_year}) ---")
increases = df_change.nlargest(10, 'Absolute_Change')[['REF_AREA_LABEL', f'Value_{first_year}', f'Value_{latest_year}', 'Absolute_Change', 'Percentage_Change']]
print(increases.to_string(index=False))

# Biggest decreases
print(f"\n--- TOP 10 BIGGEST DECREASES ({first_year} to {latest_year}) ---")
decreases = df_change.nsmallest(10, 'Absolute_Change')[['REF_AREA_LABEL', f'Value_{first_year}', f'Value_{latest_year}', 'Absolute_Change', 'Percentage_Change']]
print(decreases.to_string(index=False))

# ANALYSIS 4: Specific Country Checks
print("\n" + "="*100)
print("[3.5] SPECIFIC COUNTRY TRENDS")
print("="*100)

check_countries = ['India', 'China', 'Nigeria', 'Pakistan', 'Bangladesh', 'United States', 'Germany']

selected_countries_data = []

for country in check_countries:
    country_df = df[df['REF_AREA_LABEL'].str.contains(country, case=False, na=False)].copy()

    if len(country_df) > 0:
        country_name = country_df['REF_AREA_LABEL'].iloc[0]
        country_code = country_df['REF_AREA'].iloc[0]

        print(f"\n--- {country_name.upper()} ---")
        print(f"Country Code: {country_code}")
        print(f"Records: {len(country_df)}")

        trend = country_df[['TIME_PERIOD', 'OBS_VALUE']].sort_values('TIME_PERIOD')
        print(trend.to_string(index=False))

        # Calculate trend
        first_val = trend.iloc[0]['OBS_VALUE']
        last_val = trend.iloc[-1]['OBS_VALUE']
        change = last_val - first_val
        pct_change = (change / first_val * 100) if first_val != 0 else np.nan

        print(f"\nChange: {first_val:.1f}M ({first_year}) -> {last_val:.1f}M ({latest_year})")
        print(f"Absolute change: {change:+.1f}M")
        print(f"Percentage change: {pct_change:+.1f}%")

        # Add to export list
        for _, row in trend.iterrows():
            selected_countries_data.append({
                'Country': country_name,
                'Country_Code': country_code,
                'Year': row['TIME_PERIOD'],
                'Value_Millions': row['OBS_VALUE']
            })
    else:
        print(f"\n--- {country.upper()} ---")
        print(f"NOT FOUND in dataset")

# Save selected country trends
df_selected = pd.DataFrame(selected_countries_data)
df_selected.to_csv("output/selected_country_trends.csv", index=False)
print(f"\n\nSaved: output/selected_country_trends.csv")

# Global trend
print("\n" + "="*100)
print("[3.6] GLOBAL TREND")
print("="*100)

global_trend = df.groupby('TIME_PERIOD')['OBS_VALUE'].sum().sort_index()
print("\nTotal people unable to afford healthy diet (millions):")
for year, total in global_trend.items():
    if year > first_year:
        prev_total = global_trend[year-1]
        change = total - prev_total
        pct = (change / prev_total * 100)
        direction = "DOWN" if change < 0 else "UP"
        print(f"{year}: {total:>8,.1f}M  ({direction} {abs(change):>6,.1f}M, {pct:>+6.2f}%)")
    else:
        print(f"{year}: {total:>8,.1f}M  (baseline)")

print(f"\n{'='*100}")
print("PHASE 3 COMPLETE - ANALYSIS")
print("="*100)
print(f"\nFiles created:")
print(f"  1. output/latest_year_top20.csv")
print(f"  2. output/country_change_summary.csv")
print(f"  3. output/selected_country_trends.csv")
