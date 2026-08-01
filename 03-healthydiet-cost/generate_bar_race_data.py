import pandas as pd
import json
import warnings
warnings.filterwarnings('ignore')

print("="*100)
print("GENERATING BAR CHART RACE DATA (2017-2025)")
print("="*100)

# Load data
print("\n[1] Loading data...")
df = pd.read_csv("output/cleaned_unable_to_afford_healthy_diet.csv")

# World Bank population data (millions) - using 2025 estimates
population_data = {
    'India': 1428.6,
    'Indonesia': 277.5,
    'Nigeria': 223.8,
    'Pakistan': 240.5,
    'China': 1425.9,
    'Congo, Dem. Rep.': 102.3,
    'Ethiopia': 126.5,
    'Bangladesh': 173.6,
    'Philippines': 117.3,
    'Tanzania': 67.4,
    'Brazil': 216.4,
    'Mexico': 128.5,
    'Vietnam': 98.5,
    'Egypt, Arab Rep.': 111.0,
    'Iran, Islamic Rep.': 89.2,
    'Thailand': 71.8,
    'Myanmar': 54.6,
    'Kenya': 56.2,
    'Uganda': 48.6,
    'South Africa': 60.4,
}

# Get all years
years = sorted(df['TIME_PERIOD'].unique())

# Prepare data structure for bar chart race
race_data = []

for year in years:
    print(f"\n[2] Processing year {year}...")

    df_year = df[df['TIME_PERIOD'] == year].copy()

    # Calculate global total for this year
    global_total = df_year['OBS_VALUE'].sum()

    # Get top 10 for this year
    top10 = df_year.nlargest(10, 'OBS_VALUE').copy()

    # Add percentages
    top10['pct_of_global'] = (top10['OBS_VALUE'] / global_total * 100)
    top10['population'] = top10['REF_AREA_LABEL'].map(population_data)
    top10['pct_of_own_pop'] = (top10['OBS_VALUE'] / top10['population'] * 100).fillna(0)

    # Create year data
    year_data = {
        'year': int(year),
        'global_total': round(global_total, 1),
        'countries': []
    }

    for idx, row in top10.iterrows():
        country_data = {
            'rank': int(len(year_data['countries']) + 1),
            'name': row['REF_AREA_LABEL'],
            'value': round(row['OBS_VALUE'], 1),
            'pct_of_global': round(row['pct_of_global'], 1),
            'pct_of_own_pop': round(row['pct_of_own_pop'], 1),
        }
        year_data['countries'].append(country_data)
        print(f"  #{country_data['rank']}: {country_data['name']} - {country_data['value']}M")

    race_data.append(year_data)

# Save to JSON for Remotion
output_file = "healthydiet-video/public/data/bar_race_data.json"
with open(output_file, 'w') as f:
    json.dump(race_data, f, indent=2)

print(f"\n[3] Saved: {output_file}")

# Also save a summary
print("\n[4] Summary of ranking changes:")
print("="*60)

# Track India, Indonesia, Nigeria across years
tracked = ['India', 'Indonesia', 'Nigeria']
for country in tracked:
    print(f"\n{country}:")
    for year_data in race_data:
        for c in year_data['countries']:
            if c['name'] == country:
                print(f"  {year_data['year']}: #{c['rank']} - {c['value']}M people "
                      f"({c['pct_of_own_pop']}% of population)")
                break

print("\n" + "="*100)
print("SUCCESS: BAR CHART RACE DATA GENERATED!")
print("="*100)
