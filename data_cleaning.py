"""
Data cleaning script for customer_churn_sample.csv

Steps:
1. Load raw data
2. Standardize column headers to lowercase
3. Fix categorical string inconsistencies (preserve correct acronym casing, etc.)
4. Validate: no nulls, no duplicates, cross-field consistency (totalcharges = monthlycharges * tenuremonths)
5. Save cleaned file
"""

import pandas as pd

INPUT_PATH = "customer_churn_sample.csv"
OUTPUT_PATH = "customer_churn_sample_clean.csv"

# 1. Load raw data
raw = pd.read_csv(INPUT_PATH)
df = raw.copy()

# 2. Standardize column headers (PascalCase -> lowercase)
df.columns = [c.lower() for c in df.columns]

# 3. Standardize categorical strings
# UPI is an acronym -> must stay uppercase
df['paymentmethod'] = df['paymentmethod'].str.strip()
df['paymentmethod'] = df['paymentmethod'].replace({'Upi': 'UPI', 'upi': 'UPI'})

# customerid -> keep uppercase prefix convention (CUST-XXXX)
df['customerid'] = df['customerid'].str.upper().str.strip()

# contracttype -> standardize casing, keep "to" lowercase (Month-to-Month)
df['contracttype'] = (
    df['contracttype']
    .str.strip()
    .str.replace('Month-To-Month', 'Month-to-Month', regex=False)
    .str.replace('Month-to-month', 'Month-to-Month', regex=False)
)

# Remaining categorical columns -> just strip whitespace, already consistent
for col in ['gender', 'subscriptiontype', 'churn']:
    df[col] = df[col].str.strip()

# 4. Validation checks
assert df.isnull().sum().sum() == 0, "Unexpected nulls found!"
assert df.duplicated().sum() == 0, "Duplicate rows found!"
assert df['customerid'].duplicated().sum() == 0, "Duplicate customer IDs found!"

diff = (df['monthlycharges'] * df['tenuremonths'] - df['totalcharges']).round(2)
assert (diff.abs() < 0.01).all(), "totalcharges does not match monthlycharges * tenuremonths!"

# 5. Save cleaned file
df.to_csv(OUTPUT_PATH, index=False)
print(f"Cleaned file saved to {OUTPUT_PATH}")
print(df.head())