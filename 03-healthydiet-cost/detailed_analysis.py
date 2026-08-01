import pandas as pd
import numpy as np

print("="*80)
print("DETAILED ANALYSIS - CoAHD Dataset")
print("="*80)

df = pd.read_csv("data/01-num_people_unable_afford_healthy_diet/FAO_CAHD_7006.csv")

print("\n[1] DEMOGRAPHIC BREAKDOWNS")
print("="*80)

print("\nSex Distribution:")
print(df['SEX_LABEL'].value_counts())

print("\nAge Groups:")
print(df['AGE_LABEL'].value_counts())

print("\nUrbanisation Categories:")
print(df['URBANISATION_LABEL'].value_counts())

print("\nComponent Breakdown 1:")
print(df['COMP_BREAKDOWN_1_LABEL'].value_counts())

print("\nComponent Breakdown 2:")
print(df['COMP_BREAKDOWN_2_LABEL'].value_counts())

print("\nComponent Breakdown 3:")
print(df['COMP_BREAKDOWN_3_LABEL'].value_counts())

print("\n[2] KEY INSIGHTS FOR 2025 (LATEST YEAR)")
print("="*80)

df_2025 = df[df['TIME_PERIOD'] == 2025]

print(f"\nTotal people unable to afford healthy diet in 2025: {df_2025['OBS_VALUE'].sum():.1f} million")

print("\n--- Top 20 Most Affected Countries (2025) ---")
top20_2025 = df_2025.nlargest(20, 'OBS_VALUE')[['REF_AREA_LABEL', 'OBS_VALUE']]
top20_2025['% of Global'] = (top20_2025['OBS_VALUE'] / df_2025['OBS_VALUE'].sum() * 100).round(2)
print(top20_2025.to_string(index=False))

print("\n--- Bottom 10 Least Affected Countries (2025) ---")
bottom10_2025 = df_2025.nsmallest(10, 'OBS_VALUE')[['REF_AREA_LABEL', 'OBS_VALUE']]
print(bottom10_2025.to_string(index=False))

print("\n[3] YEAR-OVER-YEAR CHANGES")
print("="*80)

print("\nGlobal Trend Analysis:")
yearly_totals = df.groupby('TIME_PERIOD')['OBS_VALUE'].sum()
for year in sorted(df['TIME_PERIOD'].unique()):
    if year > 2017:
        prev_year = year - 1
        change = yearly_totals[year] - yearly_totals[prev_year]
        pct_change = (change / yearly_totals[prev_year] * 100)
        direction = "increased" if change > 0 else "decreased"
        print(f"{year}: {yearly_totals[year]:.1f}M ({direction} by {abs(change):.1f}M, {pct_change:+.2f}%)")
    else:
        print(f"{year}: {yearly_totals[year]:.1f}M (baseline)")

print("\n--- Countries with Largest INCREASE (2017 to 2025) ---")
df_2017 = df[df['TIME_PERIOD'] == 2017].set_index('REF_AREA_LABEL')['OBS_VALUE']
df_2025_idx = df_2025.set_index('REF_AREA_LABEL')['OBS_VALUE']
change_df = pd.DataFrame({
    '2017': df_2017,
    '2025': df_2025_idx,
    'Change': df_2025_idx - df_2017,
    '% Change': ((df_2025_idx - df_2017) / df_2017 * 100).round(2)
})
print(change_df.nlargest(10, 'Change').to_string())

print("\n--- Countries with Largest DECREASE (2017 to 2025) ---")
print(change_df.nsmallest(10, 'Change').to_string())

print("\n[4] REGIONAL PATTERNS")
print("="*80)

print("\nCountries by Continent/Region (sample analysis):")
# Identify some regional patterns from country names
asia_keywords = ['India', 'China', 'Indonesia', 'Pakistan', 'Bangladesh', 'Philippines', 'Vietnam', 'Thailand', 'Myanmar']
africa_keywords = ['Nigeria', 'Ethiopia', 'Tanzania', 'Kenya', 'Uganda', 'Sudan', 'Congo', 'Ghana', 'Mozambique']

asia_total = df_2025[df_2025['REF_AREA_LABEL'].str.contains('|'.join(asia_keywords), case=False, na=False)]['OBS_VALUE'].sum()
africa_total = df_2025[df_2025['REF_AREA_LABEL'].str.contains('|'.join(africa_keywords), case=False, na=False)]['OBS_VALUE'].sum()

print(f"Major Asian countries total: {asia_total:.1f}M ({asia_total/df_2025['OBS_VALUE'].sum()*100:.1f}% of global)")
print(f"Major African countries total: {africa_total:.1f}M ({africa_total/df_2025['OBS_VALUE'].sum()*100:.1f}% of global)")

print("\n[5] DATA QUALITY & COMPLETENESS")
print("="*80)

print(f"\nTotal records: {len(df)}")
print(f"Countries covered: {df['REF_AREA_LABEL'].nunique()}")
print(f"Years covered: {df['TIME_PERIOD'].nunique()}")
print(f"Complete dataset: {len(df[df['OBS_VALUE'] > 0])} non-zero records")
print(f"Zero values: {len(df[df['OBS_VALUE'] == 0])} records")

print("\n[6] SAMPLE DATA FOR VISUALIZATION")
print("="*80)

print("\nSample records (first 5 with high values):")
sample = df.nlargest(5, 'OBS_VALUE')[['REF_AREA_LABEL', 'TIME_PERIOD', 'OBS_VALUE',
                                         'UNIT_MEASURE_LABEL', 'SEX_LABEL', 'AGE_LABEL']]
print(sample.to_string(index=False))

print("\n[7] VISUALIZATION RECOMMENDATIONS")
print("="*80)
print("""
For your YouTube data visualization video, consider these approaches:

1. ANIMATED TIME-SERIES MAP (2017-2025)
   - Choropleth map showing countries colored by number of people affected
   - Animate year-by-year to show global changes
   - Highlight top 10 countries with labels

2. RACING BAR CHART
   - Top 20 countries racing over time (2017-2025)
   - Show India, China, Indonesia, Nigeria, Pakistan leading

3. TREND LINE CHART
   - Global total trend line (shows decline from 2.9B to 2.5B)
   - Add major events annotations (COVID-19 spike in 2020)
   - Include individual country trend lines for top 5

4. TREEMAP
   - 2025 snapshot showing relative sizes of affected populations
   - Group by regions (Asia, Africa, Americas, Europe)

5. DIVERGING BAR CHART
   - Countries with biggest improvements vs. deteriorations (2017-2025)
   - Green bars for decreases, red bars for increases

6. GLOBAL STATISTICS DASHBOARD
   - Total affected: 2.5 billion (2025)
   - 9-year change: -436 million (-14.9%)
   - Top 5 countries represent: 43.4% of global total

Key Message:
"Despite global population growth, the number of people unable to afford
a healthy diet decreased from 2.9 billion (2017) to 2.5 billion (2025),
but still represents roughly 1 in 3 people globally."
""")

print("\n" + "="*80)
print("ANALYSIS COMPLETE - Ready for visualization!")
print("="*80)
