import pandas as pd
import json
import warnings
warnings.filterwarnings('ignore')

print("="*100)
print("PHASE 4: VIDEO-READY DATA")
print("="*100)

# Load cleaned dataset
print("\n[4.1] Loading cleaned dataset...")
df = pd.read_csv("output/cleaned_unable_to_afford_healthy_diet.csv")
print(f"Loaded: {len(df):,} records")

# Handle China duplicate issue - keep only mainland China (higher values)
print("\n[4.2] Handling duplicate countries (China)...")
china_before = len(df[df['REF_AREA'] == 'CHN'])
print(f"China records before deduplication: {china_before}")

# For China, keep the record with higher OBS_VALUE for each year (mainland China)
df_china = df[df['REF_AREA'] == 'CHN'].copy()
df_china_deduplicated = df_china.sort_values('OBS_VALUE', ascending=False).drop_duplicates(subset=['TIME_PERIOD'], keep='first')

# Remove all China records and add back deduplicated ones
df = df[df['REF_AREA'] != 'CHN']
df = pd.concat([df, df_china_deduplicated], ignore_index=True)
df = df.sort_values(['REF_AREA_LABEL', 'TIME_PERIOD']).reset_index(drop=True)

china_after = len(df[df['REF_AREA'] == 'CHN'])
print(f"China records after deduplication: {china_after}")
print(f"Total records after deduplication: {len(df):,}")

# VIDEO DATA 1: Bar Chart Race Format
print("\n[4.3] Creating bar chart race JSON...")

video_data = []

for year in sorted(df['TIME_PERIOD'].unique()):
    year_data = df[df['TIME_PERIOD'] == year].copy()
    year_data = year_data.sort_values('OBS_VALUE', ascending=False)

    countries_list = []
    for _, row in year_data.iterrows():
        countries_list.append({
            "countryCode": row['REF_AREA'],
            "country": row['REF_AREA_LABEL'],
            "value": round(float(row['OBS_VALUE']), 2)
        })

    video_data.append({
        "year": int(year),
        "countries": countries_list
    })

# Save full bar chart race data
output_file1 = "output/video_ready_bar_chart_race.json"
with open(output_file1, 'w', encoding='utf-8') as f:
    json.dump(video_data, f, indent=2, ensure_ascii=False)

print(f"Saved: {output_file1}")
print(f"  Years: {len(video_data)}")
print(f"  Countries per year: ~{len(video_data[0]['countries'])}")

# VIDEO DATA 2: Top 10 per Year
print("\n[4.4] Creating top 10 yearly JSON...")

top10_data = []

for year in sorted(df['TIME_PERIOD'].unique()):
    year_data = df[df['TIME_PERIOD'] == year].copy()
    year_data = year_data.sort_values('OBS_VALUE', ascending=False).head(10)

    top10_list = []
    for rank, (_, row) in enumerate(year_data.iterrows(), 1):
        top10_list.append({
            "rank": rank,
            "countryCode": row['REF_AREA'],
            "country": row['REF_AREA_LABEL'],
            "value": round(float(row['OBS_VALUE']), 2)
        })

    top10_data.append({
        "year": int(year),
        "top10": top10_list
    })

output_file2 = "output/yearly_top10.json"
with open(output_file2, 'w', encoding='utf-8') as f:
    json.dump(top10_data, f, indent=2, ensure_ascii=False)

print(f"Saved: {output_file2}")
print(f"  Years: {len(top10_data)}")

# VIDEO DATA 3: Global Stats per Year
print("\n[4.5] Creating global statistics JSON...")

global_stats = []

for year in sorted(df['TIME_PERIOD'].unique()):
    year_data = df[df['TIME_PERIOD'] == year]

    total = year_data['OBS_VALUE'].sum()
    num_countries = len(year_data)

    # Top 5 countries
    top5 = year_data.nlargest(5, 'OBS_VALUE')[['REF_AREA_LABEL', 'OBS_VALUE']].to_dict('records')
    top5_formatted = [{"country": r['REF_AREA_LABEL'], "value": round(float(r['OBS_VALUE']), 2)} for r in top5]

    # Top 5 contribution
    top5_sum = year_data.nlargest(5, 'OBS_VALUE')['OBS_VALUE'].sum()
    top5_percentage = (top5_sum / total * 100) if total > 0 else 0

    global_stats.append({
        "year": int(year),
        "totalMillions": round(float(total), 1),
        "totalBillions": round(float(total) / 1000, 2),
        "countriesCount": int(num_countries),
        "averagePerCountry": round(float(total / num_countries), 2),
        "top5Countries": top5_formatted,
        "top5Percentage": round(float(top5_percentage), 2)
    })

output_file3 = "output/global_stats_yearly.json"
with open(output_file3, 'w', encoding='utf-8') as f:
    json.dump(global_stats, f, indent=2, ensure_ascii=False)

print(f"Saved: {output_file3}")

# VIDEO DATA 4: Selected Countries Timeline
print("\n[4.6] Creating selected countries timeline JSON...")

selected_countries = ['India', 'China', 'Nigeria', 'Pakistan', 'Bangladesh', 'United States', 'Germany']

countries_timeline = []

for country_name in selected_countries:
    country_data = df[df['REF_AREA_LABEL'].str.contains(country_name, case=False, na=False)].copy()

    if len(country_data) > 0:
        country_actual_name = country_data['REF_AREA_LABEL'].iloc[0]
        country_code = country_data['REF_AREA'].iloc[0]

        # Handle China duplicates - already deduplicated above
        timeline = []
        for _, row in country_data.sort_values('TIME_PERIOD').iterrows():
            timeline.append({
                "year": int(row['TIME_PERIOD']),
                "value": round(float(row['OBS_VALUE']), 2)
            })

        countries_timeline.append({
            "country": country_actual_name,
            "countryCode": country_code,
            "timeline": timeline
        })

output_file4 = "output/selected_countries_timeline.json"
with open(output_file4, 'w', encoding='utf-8') as f:
    json.dump(countries_timeline, f, indent=2, ensure_ascii=False)

print(f"Saved: {output_file4}")
print(f"  Countries included: {len(countries_timeline)}")

# VIDEO DATA 5: Change Analysis (2017 vs 2025)
print("\n[4.7] Creating change analysis JSON...")

first_year = df['TIME_PERIOD'].min()
last_year = df['TIME_PERIOD'].max()

df_first = df[df['TIME_PERIOD'] == first_year][['REF_AREA', 'REF_AREA_LABEL', 'OBS_VALUE']].rename(columns={'OBS_VALUE': 'value_first'})
df_last = df[df['TIME_PERIOD'] == last_year][['REF_AREA', 'REF_AREA_LABEL', 'OBS_VALUE']].rename(columns={'OBS_VALUE': 'value_last'})

df_change = pd.merge(df_first, df_last, on=['REF_AREA', 'REF_AREA_LABEL'], how='inner')
df_change['absolute_change'] = df_change['value_last'] - df_change['value_first']
df_change['percentage_change'] = ((df_change['value_last'] - df_change['value_first']) / df_change['value_first'] * 100).round(2)

# Top 10 increases
increases = df_change.nlargest(10, 'absolute_change').to_dict('records')
increases_formatted = [{
    "country": r['REF_AREA_LABEL'],
    "countryCode": r['REF_AREA'],
    "valueFirst": round(float(r['value_first']), 2),
    "valueLast": round(float(r['value_last']), 2),
    "absoluteChange": round(float(r['absolute_change']), 2),
    "percentageChange": round(float(r['percentage_change']), 2)
} for r in increases]

# Top 10 decreases
decreases = df_change.nsmallest(10, 'absolute_change').to_dict('records')
decreases_formatted = [{
    "country": r['REF_AREA_LABEL'],
    "countryCode": r['REF_AREA'],
    "valueFirst": round(float(r['value_first']), 2),
    "valueLast": round(float(r['value_last']), 2),
    "absoluteChange": round(float(r['absolute_change']), 2),
    "percentageChange": round(float(r['percentage_change']), 2)
} for r in decreases]

change_analysis = {
    "firstYear": int(first_year),
    "lastYear": int(last_year),
    "globalFirst": round(float(df_first['value_first'].sum()), 1),
    "globalLast": round(float(df_last['value_last'].sum()), 1),
    "globalChange": round(float(df_last['value_last'].sum() - df_first['value_first'].sum()), 1),
    "top10Increases": increases_formatted,
    "top10Decreases": decreases_formatted
}

output_file5 = "output/change_analysis.json"
with open(output_file5, 'w', encoding='utf-8') as f:
    json.dump(change_analysis, f, indent=2, ensure_ascii=False)

print(f"Saved: {output_file5}")

# Print sample from each file
print("\n[4.8] Sample data preview:")
print("\n--- Sample from yearly_top10.json (2025) ---")
print(json.dumps(top10_data[-1], indent=2))

print("\n--- Sample from global_stats_yearly.json (2025) ---")
print(json.dumps(global_stats[-1], indent=2))

print("\n" + "="*100)
print("PHASE 4 COMPLETE - VIDEO-READY DATA")
print("="*100)
print(f"\nJSON files created:")
print(f"  1. {output_file1} (full bar chart race data)")
print(f"  2. {output_file2} (top 10 per year)")
print(f"  3. {output_file3} (global statistics)")
print(f"  4. {output_file4} (selected countries timeline)")
print(f"  5. {output_file5} (change analysis)")
print(f"\nThese JSON files are ready for:")
print(f"  - Remotion video rendering")
print(f"  - D3.js visualizations")
print(f"  - Plotly animations")
print(f"  - Web-based dashboards")
