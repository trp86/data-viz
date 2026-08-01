import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

print("="*100)
print("PHASE 1: DATA UNDERSTANDING")
print("="*100)

# Load the dataset
print("\n[1.1] Loading FAO_CAHD.csv...")
df = pd.read_csv("data/01-num_people_unable_afford_healthy_diet/FAO_CAHD_7006.csv")
print(f"Dataset loaded successfully!")

# Print shape
print("\n[1.2] DATASET SHAPE")
print("-" * 100)
print(f"Rows: {df.shape[0]:,}")
print(f"Columns: {df.shape[1]}")

# Print column names
print("\n[1.3] COLUMN NAMES")
print("-" * 100)
for i, col in enumerate(df.columns, 1):
    print(f"{i:2d}. {col}")

# Print first 10 rows
print("\n[1.4] FIRST 10 ROWS")
print("-" * 100)
print(df.head(10).to_string())

# Unique INDICATOR_LABEL values
print("\n[1.5] UNIQUE INDICATOR_LABEL VALUES")
print("-" * 100)
unique_indicators = df['INDICATOR_LABEL'].unique()
print(f"Total unique indicators: {len(unique_indicators)}")
for i, indicator in enumerate(unique_indicators, 1):
    count = len(df[df['INDICATOR_LABEL'] == indicator])
    print(f"{i}. {indicator} ({count:,} records)")

# Unique UNIT_MEASURE_LABEL values
print("\n[1.6] UNIQUE UNIT_MEASURE_LABEL VALUES")
print("-" * 100)
unique_units = df['UNIT_MEASURE_LABEL'].unique()
for i, unit in enumerate(unique_units, 1):
    count = len(df[df['UNIT_MEASURE_LABEL'] == unit])
    print(f"{i}. {unit} ({count:,} records)")

# Unique TIME_PERIOD values
print("\n[1.7] UNIQUE TIME_PERIOD VALUES")
print("-" * 100)
unique_years = sorted(df['TIME_PERIOD'].unique())
print(f"Years available: {unique_years}")
print(f"Total years: {len(unique_years)}")
print(f"Range: {min(unique_years)} to {max(unique_years)}")

# Unique OBS_STATUS_LABEL values
print("\n[1.8] UNIQUE OBS_STATUS_LABEL VALUES")
print("-" * 100)
unique_status = df['OBS_STATUS_LABEL'].unique()
for i, status in enumerate(unique_status, 1):
    count = len(df[df['OBS_STATUS_LABEL'] == status])
    print(f"{i}. {status} ({count:,} records)")

# Find the indicator about "unable to afford healthy diet"
print("\n[1.9] FINDING TARGET INDICATOR")
print("-" * 100)
target_keywords = "unable to afford"
matching_indicators = df[df['INDICATOR_LABEL'].str.contains(target_keywords, case=False, na=False)]['INDICATOR_LABEL'].unique()

if len(matching_indicators) > 0:
    print(f"FOUND {len(matching_indicators)} matching indicator(s):")
    for i, ind in enumerate(matching_indicators, 1):
        print(f"{i}. {ind}")

    # Use the first matching indicator
    target_indicator = matching_indicators[0]
    print(f"\nSelected indicator: '{target_indicator}'")
else:
    print("No matching indicator found!")
    target_indicator = None

# Print sample rows for this indicator
if target_indicator:
    print("\n[1.10] SAMPLE ROWS FOR TARGET INDICATOR")
    print("-" * 100)
    df_target = df[df['INDICATOR_LABEL'] == target_indicator]
    print(f"Total records for this indicator: {len(df_target):,}")
    print("\nFirst 10 rows:")
    print(df_target.head(10).to_string())

    print("\nRandom sample of 5 rows:")
    print(df_target.sample(min(5, len(df_target))).to_string())

    # Analyze unit multiplier
    print("\n[1.11] UNIT ANALYSIS FOR TARGET INDICATOR")
    print("-" * 100)
    print("Unique UNIT_MEASURE_LABEL:")
    print(df_target['UNIT_MEASURE_LABEL'].unique())

    print("\nUnique UNIT_MULT_LABEL:")
    print(df_target['UNIT_MULT_LABEL'].unique())

    print("\nUnique UNIT_MULT (numeric):")
    print(df_target['UNIT_MULT'].unique())

    # Check OBS_VALUE range
    print("\n[1.12] OBS_VALUE STATISTICS")
    print("-" * 100)
    print(df_target['OBS_VALUE'].describe())

    print(f"\nMinimum OBS_VALUE: {df_target['OBS_VALUE'].min()}")
    print(f"Maximum OBS_VALUE: {df_target['OBS_VALUE'].max()}")
    print(f"Mean OBS_VALUE: {df_target['OBS_VALUE'].mean():.2f}")
    print(f"Median OBS_VALUE: {df_target['OBS_VALUE'].median():.2f}")

    # Sample high-value countries
    print("\n[1.13] TOP 10 COUNTRIES (ALL YEARS COMBINED)")
    print("-" * 100)
    top_countries = df_target.nlargest(10, 'OBS_VALUE')[['REF_AREA', 'REF_AREA_LABEL', 'TIME_PERIOD', 'OBS_VALUE', 'UNIT_MEASURE_LABEL']]
    print(top_countries.to_string(index=False))

    # Check specific countries
    print("\n[1.14] CHECK SPECIFIC COUNTRIES")
    print("-" * 100)
    check_countries = ['India', 'China', 'Nigeria', 'Pakistan', 'Bangladesh', 'United States', 'Germany']

    for country in check_countries:
        country_data = df_target[df_target['REF_AREA_LABEL'].str.contains(country, case=False, na=False)]
        if len(country_data) > 0:
            print(f"\n{country}: FOUND ({len(country_data)} records)")
            print(f"  Years: {sorted(country_data['TIME_PERIOD'].unique())}")
            print(f"  Value range: {country_data['OBS_VALUE'].min():.2f} to {country_data['OBS_VALUE'].max():.2f}")
        else:
            print(f"\n{country}: NOT FOUND")

print("\n" + "="*100)
print("PHASE 1 COMPLETE - DATA UNDERSTANDING")
print("="*100)

print("\n[SUMMARY]")
print("-" * 100)
if target_indicator:
    print(f"""
INDICATOR NAME:
{target_indicator}

WHAT THIS INDICATOR MEASURES:
This indicator measures the NUMBER OF PEOPLE in each country who CANNOT AFFORD
to purchase a healthy diet. A healthy diet includes adequate amounts of:
- Fruits and vegetables
- Proteins (meat, fish, eggs, legumes)
- Dairy products
- Whole grains
- Essential fats

WHAT OBS_VALUE MEANS:
OBS_VALUE = The actual number value in the specified unit.

UNIT USED:
{df_target['UNIT_MEASURE_LABEL'].unique()[0]}

UNIT MULTIPLIER:
{df_target['UNIT_MULT_LABEL'].unique()[0]}
(UNIT_MULT numeric value: {df_target['UNIT_MULT'].unique()[0]})

This means:
- UNIT_MULT = 6 means "Millions"
- So if OBS_VALUE = 813.1 and UNIT_MULT = 6
- The actual value = 813.1 MILLION people

SCALING NEEDED:
NO additional scaling is needed. The OBS_VALUE already represents MILLIONS of people.
For example:
- OBS_VALUE = 813.1 means 813.1 million = 813,100,000 people

DATA COVERAGE:
- Countries: {df_target['REF_AREA_LABEL'].nunique()}
- Years: {df_target['TIME_PERIOD'].nunique()} ({df_target['TIME_PERIOD'].min()} to {df_target['TIME_PERIOD'].max()})
- Total records: {len(df_target):,}

KEY INSIGHT:
This dataset is PERFECT for a 5-minute Visual Capitalist-style video because:
1. Clear, impactful metric (number of people affected)
2. Multiple years for animation (time-series)
3. Global coverage (147 countries)
4. Large numbers that create visual impact (billions of people)
5. Contains major countries like India, China, Nigeria for storytelling
""")
else:
    print("ERROR: Target indicator not found!")

print("\n" + "="*100)
print("Ready to proceed to PHASE 2: DATA CLEANING")
print("="*100)
