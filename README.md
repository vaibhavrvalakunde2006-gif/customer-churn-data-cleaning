# Customer Churn Data Cleaning

A Python-based data cleaning project that demonstrates how to inspect, validate, clean, and export a customer churn dataset using the Pandas library.

---

## 📌 Project Overview

The objective of this project is to perform data cleaning on a sample customer churn dataset by identifying data quality issues, standardizing the data, validating its consistency, and exporting a cleaned dataset for further analysis.

---

## 🎯 Objectives

- Load the customer churn dataset
- Inspect the dataset structure
- Check for missing values
- Detect duplicate records
- Verify data types
- Standardize column headers
- Clean and standardize categorical values
- Validate data consistency
- Export the cleaned dataset

---

## 🛠️ Technologies Used

- Python 3
- Pandas
- Visual Studio Code
- Git
- GitHub

---

## 📂 Project Structure

```
customer-churn-data-cleaning/
│
├── customer_churn_sample.csv
├── customer_churn_sample_clean.csv
├── data_cleaning.py
├── README.md
└── .gitignore
```

---

## ⚙️ Data Cleaning Process

The following cleaning steps were performed:

1. Loaded the raw customer churn dataset.
2. Standardized all column names to lowercase.
3. Removed unnecessary whitespace from categorical values.
4. Standardized categorical values:
   - Preserved **UPI** as an uppercase acronym.
   - Standardized contract type formatting.
   - Standardized customer ID formatting.
5. Validated the dataset by checking:
   - Missing values
   - Duplicate rows
   - Duplicate customer IDs
   - Consistency of **Total Charges = Monthly Charges × Tenure Months**
6. Exported the cleaned dataset.

---

## ✅ Data Validation

The script performs the following validation checks before exporting the cleaned dataset:

- No missing values
- No duplicate records
- No duplicate customer IDs
- Total Charges correctly match Monthly Charges × Tenure Months

The script stops execution if any validation fails.

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/vaibhavrvalakunde2006-gif/customer-churn-data-cleaning.git
```

### 2. Navigate to the project folder

```bash
cd customer-churn-data-cleaning
```

### 3. Install the required package

```bash
pip install pandas
```

### 4. Run the script

```bash
python data_cleaning.py
```

---

## 📤 Output

Running the script generates the following cleaned dataset:

```
customer_churn_sample_clean.csv
```

---

## 📋 Sample Output

```text
Dataset loaded successfully.
Rows: 15, Columns: 11

Checking missing values...
No missing values found.

Checking duplicate rows...
0

Validation successful.

Cleaned dataset saved as:
customer_churn_sample_clean.csv
```

---

## 📁 Files Included

| File | Description |
|------|-------------|
| `customer_churn_sample.csv` | Original dataset |
| `customer_churn_sample_clean.csv` | Cleaned dataset |
| `data_cleaning.py` | Python data cleaning script |
| `README.md` | Project documentation |

---

## 👨‍💻 Author

**Vaibhav R Valakunde**

GitHub: https://github.com/vaibhavrvalakunde2006-gif

---

## ⭐ Repository

If you found this project useful, feel free to star the repository.
