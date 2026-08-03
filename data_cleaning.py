

import pandas as pd

INPUT_PATH = "customer_churn_sample.csv"
OUTPUT_PATH = "customer_churn_sample_clean.csv"
raw = pd.read_csv(INPUT_PATH)
df = raw.copy()
df.columns = [c.lower() for c in df.columns]
df['paymentmethod'] = df['paymentmethod'].str.strip()
df['paymentmethod'] = df['paymentmethod'].replace({'Upi': 'UPI', 'upi': 'UPI'})
df['customerid'] = df['customerid'].str.upper().str.strip()
df['contracttype'] = (
    df['contracttype']
    .str.strip()
    .str.replace('Month-To-Month', 'Month-to-Month', regex=False)
    .str.replace('Month-to-month', 'Month-to-Month', regex=False)
)
for col in ['gender', 'subscriptiontype', 'churn']:
    df[col] = df[col].str.strip()
assert df.isnull().sum().sum() == 0, "Unexpected nulls found!"
assert df.duplicated().sum() == 0, "Duplicate rows found!"
assert df['customerid'].duplicated().sum() == 0, "Duplicate customer IDs found!"
diff = (df['monthlycharges'] * df['tenuremonths'] - df['totalcharges']).round(2)
assert (diff.abs() < 0.01).all(), "totalcharges does not match monthlycharges * tenuremonths!"
df.to_csv(OUTPUT_PATH, index=False)
print(f"Cleaned file saved to {OUTPUT_PATH}")
print(df.head())