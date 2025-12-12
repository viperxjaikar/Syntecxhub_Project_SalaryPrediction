# 02_preprocess.py
# Step 2: Preprocessing for Salary Prediction project
# - loads dataset.csv from same folder
# - normalizes column names
# - checks and fills missing numeric values (median)
# - ensures types are numeric
# - saves cleaned CSV as salary_cleaned.csv

import pandas as pd
import os

print("===== STEP 2: PREPROCESSING =====")
print("Working directory:", os.getcwd(), "\n")

# 1) load
df = pd.read_csv("dataset.csv")
print("Original shape:", df.shape, "\n")

# 2) normalize column names
df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]
print("Columns after normalization:", df.columns.tolist(), "\n")

# 3) verify required columns
required = ["experience", "test_score", "salary"]
missing_required = [c for c in required if c not in df.columns]
if missing_required:
    print("ERROR: Missing required columns:", missing_required)
    print("Stop and rename columns in dataset.csv or tell me the printed column names.")
    raise SystemExit(1)

# 4) show a quick peek
print("First 5 rows:\n", df[required].head().to_string(index=False), "\n")
print("Data types:\n", df[required].dtypes, "\n")
print("Missing values BEFORE filling:\n", df[required].isnull().sum(), "\n")

# 5) coerce to numeric if any column is non-numeric (safe)
for c in required:
    if not pd.api.types.is_numeric_dtype(df[c]):
        print(f"Converting '{c}' to numeric (coerce errors -> NaN).")
        df[c] = pd.to_numeric(df[c], errors="coerce")

# 6) fill missing numeric values with median
for c in required:
    if df[c].isnull().any():
        med = df[c].median()
        df[c].fillna(med, inplace=True)
        print(f"Filled missing values in '{c}' with median = {med}")

# 7) final checks
print("\nMissing values AFTER filling:\n", df[required].isnull().sum(), "\n")
print("Final dtypes:\n", df[required].dtypes, "\n")
print("Summary stats (final):\n", df[required].describe().round(3).to_string(), "\n")

# 8) save cleaned CSV
out_path = "salary_cleaned.csv"
df[required].to_csv(out_path, index=False)
print(f"Cleaned dataset saved to: {out_path}")
print("\nSTEP 2 complete. If everything is OK, reply:  Step 2 done")
