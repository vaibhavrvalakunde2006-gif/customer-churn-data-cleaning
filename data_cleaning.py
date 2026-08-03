import pandas as pd
df = pd.read_csv("customer_churn_sample.csv")
print(df.head())
print("Dataset Shape:")
print(df.shape)
print("\nColumn Names:")
print(df.columns)
print("\nData Types:")
print(df.dtypes)
print("\nDataset Information:")
df.info()
# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())
# Check duplicate rows
print("\nDuplicate Records:")
print(df.duplicated().sum())
# Standardize column names
df.columns = (
    df.columns
      .str.strip()          # Remove leading/trailing spaces
      .str.lower()          # Convert to lowercase
      .str.replace(" ", "_") # Replace spaces with underscores
)

print("\nUpdated Column Names:")
print(df.columns)
# Clean text columns
for col in df.select_dtypes(include=["object", "string"]):
    df[col] = df[col].str.strip()

# Standardize text formatting
for col in df.select_dtypes(include=["object", "string"]):
    df[col] = df[col].str.title()
# Preview cleaned dataset
print("\nCleaned Dataset:")
print(df.head())
# Export cleaned dataset
df.to_csv("customer_churn_sample_clean.csv", index=False)

print("\n✅ Cleaned dataset exported successfully!")
