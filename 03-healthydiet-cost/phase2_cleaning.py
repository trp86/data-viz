import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

print("="*100)
print("PHASE 2: DATA CLEANING")
print("="*100)

# Load the dataset
print("\n[2.1] Loading original dataset...")
df = pd.read_csv("data/01-num_people_unable_afford_healthy_diet/FAO_CAHD_7006.csv")
print(f"Original dataset: {df.shape[0]:,} rows x {df.shape[1]} columns")

# Step 1: Filter for target indicator
print("\n[2.2] Filtering for target indicator...")
target_indicator = "Number of people unable to afford a healthy diet (million)"
df_filtered = df[df['INDICATOR_LABEL'] == target_indicator].copy()
print(f"After filtering indicator: {df_filtered.shape[0]:,} rows")

# Step 2: Keep only normal/public observations
print("\n[2.3] Filtering for normal and public observations...")
print(f"Before filtering:")
print(f"  OBS_STATUS_LABEL unique values: {df_filtered['OBS_STATUS_LABEL'].unique()}")
print(f"  OBS_CONF_LABEL unique values: {df_filtered['OBS_CONF_LABEL'].unique()}")

df_filtered = df_filtered[
    (df_filtered['OBS_STATUS_LABEL'] == 'Normal value') &
    (df_filtered['OBS_CONF_LABEL'] == 'Public')
].copy()
print(f"After filtering status/confidentiality: {df_filtered.shape[0]:,} rows")

# Step 3: Convert OBS_VALUE to numeric
print("\n[2.4] Converting OBS_VALUE to numeric...")
print(f"OBS_VALUE dtype before: {df_filtered['OBS_VALUE'].dtype}")
df_filtered['OBS_VALUE'] = pd.to_numeric(df_filtered['OBS_VALUE'], errors='coerce')
print(f"OBS_VALUE dtype after: {df_filtered['OBS_VALUE'].dtype}")

# Step 4: Convert TIME_PERIOD to integer
print("\n[2.5] Converting TIME_PERIOD to integer...")
print(f"TIME_PERIOD dtype before: {df_filtered['TIME_PERIOD'].dtype}")
df_filtered['TIME_PERIOD'] = df_filtered['TIME_PERIOD'].astype(int)
print(f"TIME_PERIOD dtype after: {df_filtered['TIME_PERIOD'].dtype}")

# Step 5: Remove rows with missing OBS_VALUE
print("\n[2.6] Removing rows with missing OBS_VALUE...")
print(f"Missing OBS_VALUE before: {df_filtered['OBS_VALUE'].isna().sum()}")
df_filtered = df_filtered[df_filtered['OBS_VALUE'].notna()].copy()
print(f"After removing missing values: {df_filtered.shape[0]:,} rows")

# Step 6: Keep only useful columns
print("\n[2.7] Selecting useful columns...")
useful_columns = [
    'REF_AREA',
    'REF_AREA_LABEL',
    'INDICATOR',
    'INDICATOR_LABEL',
    'TIME_PERIOD',
    'OBS_VALUE',
    'UNIT_MEASURE',
    'UNIT_MEASURE_LABEL',
    'UNIT_MULT',
    'UNIT_MULT_LABEL',
    'OBS_STATUS_LABEL',
    'OBS_CONF_LABEL'
]

df_cleaned = df_filtered[useful_columns].copy()
print(f"Columns kept: {len(useful_columns)}")
for col in useful_columns:
    print(f"  - {col}")

# Additional cleaning: Sort by country and year
print("\n[2.8] Sorting data...")
df_cleaned = df_cleaned.sort_values(['REF_AREA_LABEL', 'TIME_PERIOD']).reset_index(drop=True)

# Save cleaned dataset
print("\n[2.9] Saving cleaned dataset...")
output_file = "output/cleaned_unable_to_afford_healthy_diet.csv"
df_cleaned.to_csv(output_file, index=False)
print(f"Saved to: {output_file}")

# Print summary
print("\n" + "="*100)
print("CLEANING SUMMARY")
print("="*100)
print(f"Original rows: {df.shape[0]:,}")
print(f"Cleaned rows: {df_cleaned.shape[0]:,}")
print(f"Rows removed: {df.shape[0] - df_cleaned.shape[0]:,}")
print(f"Columns: {df_cleaned.shape[1]}")
print(f"\nUnique countries: {df_cleaned['REF_AREA_LABEL'].nunique()}")
print(f"Years covered: {df_cleaned['TIME_PERIOD'].min()} to {df_cleaned['TIME_PERIOD'].max()}")
print(f"Total years: {df_cleaned['TIME_PERIOD'].nunique()}")

# Data quality checks
print("\n[2.10] DATA QUALITY CHECKS")
print("-" * 100)
print(f"Missing values per column:")
for col in df_cleaned.columns:
    missing = df_cleaned[col].isna().sum()
    if missing > 0:
        print(f"  {col}: {missing}")
    else:
        print(f"  {col}: 0 (OK)")

print(f"\nOBS_VALUE statistics:")
print(f"  Min: {df_cleaned['OBS_VALUE'].min():.2f} million")
print(f"  Max: {df_cleaned['OBS_VALUE'].max():.2f} million")
print(f"  Mean: {df_cleaned['OBS_VALUE'].mean():.2f} million")
print(f"  Median: {df_cleaned['OBS_VALUE'].median():.2f} million")
print(f"  Total (sum): {df_cleaned['OBS_VALUE'].sum():.2f} million")

print(f"\nCountries per year:")
year_counts = df_cleaned.groupby('TIME_PERIOD')['REF_AREA_LABEL'].nunique().sort_index()
for year, count in year_counts.items():
    print(f"  {year}: {count} countries")

print("\n[2.11] Sample of cleaned data:")
print("-" * 100)
print(df_cleaned.head(10).to_string(index=False))

print("\n" + "="*100)
print("PHASE 2 COMPLETE - DATA CLEANING")
print("="*100)
print(f"\nCleaned dataset ready for analysis!")
print(f"File: {output_file}")
print(f"Records: {len(df_cleaned):,}")
print(f"Countries: {df_cleaned['REF_AREA_LABEL'].nunique()}")
print(f"Years: {df_cleaned['TIME_PERIOD'].nunique()} ({df_cleaned['TIME_PERIOD'].min()}-{df_cleaned['TIME_PERIOD'].max()})")
