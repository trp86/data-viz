import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

print("="*80)
print("WORLD BANK CoAHD DATASET ANALYSIS")
print("Cost and Affordability of a Healthy Diet (CoAHD)")
print("Indicator: Number of people unable to afford a healthy diet (million)")
print("="*80)

# 1. LOAD THE DATASET
print("\n[1] LOADING DATASET...")
data_file = "data/01-num_people_unable_afford_healthy_diet/FAO_CAHD_7006.csv"
datadict_file = "data/01-num_people_unable_afford_healthy_diet/FAO_CAHD_7006_DATADICT.csv"

df = pd.read_csv(data_file)
data_dict = pd.read_csv(datadict_file)

print(f"Main dataset loaded: {df.shape[0]} rows x {df.shape[1]} columns")
print(f"Data dictionary loaded: {data_dict.shape[0]} rows x {data_dict.shape[1]} columns")

# 2. INSPECT THE DATASET
print("\n" + "="*80)
print("[2] DATASET INSPECTION")
print("="*80)

print("\n2.1 First 10 rows:")
print(df.head(10))

print("\n2.2 Dataset Info:")
print(df.info())

print("\n2.3 Column Names:")
for i, col in enumerate(df.columns, 1):
    print(f"  {i}. {col}")

print("\n2.4 Data Types:")
print(df.dtypes)

print("\n2.5 Missing Values:")
missing = df.isnull().sum()
missing_pct = (missing / len(df) * 100).round(2)
missing_df = pd.DataFrame({
    'Column': missing.index,
    'Missing Count': missing.values,
    'Missing %': missing_pct.values
})
print(missing_df[missing_df['Missing Count'] > 0])

# 3. UNDERSTAND THE DATASET
print("\n" + "="*80)
print("[3] DATASET UNDERSTANDING")
print("="*80)

print("\n3.1 Data Dictionary:")
print(data_dict)

# Identify country and year columns
country_col = None
year_col = None

if 'Country' in df.columns or 'country' in df.columns:
    country_col = 'Country' if 'Country' in df.columns else 'country'
elif 'REF_AREA_LABEL' in df.columns:
    country_col = 'REF_AREA_LABEL'

if 'Year' in df.columns or 'year' in df.columns:
    year_col = 'Year' if 'Year' in df.columns else 'year'
elif 'TIME_PERIOD' in df.columns:
    year_col = 'TIME_PERIOD'

if country_col:
    print(f"\n3.2 Unique Countries/Regions: {df[country_col].nunique()}")
    print(f"\nTop 10 Countries by frequency:")
    print(df[country_col].value_counts().head(10))

if year_col:
    print(f"\n3.3 Year Range: {df[year_col].min()} to {df[year_col].max()}")
    print(f"Years covered: {sorted(df[year_col].unique())}")

# Identify numeric columns
numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
print(f"\n3.4 Numeric Columns ({len(numeric_cols)}):")
for col in numeric_cols:
    print(f"  - {col}")

# 4. BASIC SUMMARIES
print("\n" + "="*80)
print("[4] BASIC SUMMARIES")
print("="*80)

print("\n4.1 Statistical Summary (Numeric Columns):")
print(df.describe())

# Find the value column (likely contains the indicator data)
value_cols = [col for col in df.columns if 'value' in col.lower() or 'million' in col.lower()]
if not value_cols and numeric_cols:
    # Use the last numeric column if no obvious value column found
    value_cols = [numeric_cols[-1]]

if value_cols:
    value_col = value_cols[0]
    print(f"\n4.2 Indicator Analysis (Column: {value_col}):")
    print(f"  - Mean: {df[value_col].mean():.2f} million people")
    print(f"  - Median: {df[value_col].median():.2f} million people")
    print(f"  - Min: {df[value_col].min():.2f} million people")
    print(f"  - Max: {df[value_col].max():.2f} million people")
    print(f"  - Std Dev: {df[value_col].std():.2f} million people")

    if country_col in df.columns and year_col in df.columns:
        print(f"\n4.3 Top 10 Countries (Most Recent Year Available):")
        latest_year = df[year_col].max()
        latest_data = df[df[year_col] == latest_year].sort_values(by=value_col, ascending=False)
        print(f"\nYear: {latest_year}")
        print(latest_data[[country_col, value_col]].head(10).to_string(index=False))

        print(f"\n4.4 Global Trend (Total per Year):")
        yearly_total = df.groupby(year_col)[value_col].sum().sort_index()
        print(yearly_total)

        print(f"\n4.5 Number of Countries with Data per Year:")
        countries_per_year = df.groupby(year_col)[country_col].nunique()
        print(countries_per_year)

print("\n" + "="*80)
print("ANALYSIS COMPLETE")
print("="*80)
print("\nDataset is ready for visualization!")
print(f"Total records: {len(df):,}")
print(f"Countries/Regions: {df[country_col].nunique() if country_col in df.columns else 'N/A'}")
print(f"Time period: {df[year_col].min()}-{df[year_col].max() if year_col in df.columns else 'N/A'}")
