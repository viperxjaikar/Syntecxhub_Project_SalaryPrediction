import pandas as pd
import os

print("Running Step 1 — Load & Inspect dataset\n")
print("Working directory:", os.getcwd(), "\n")


df = pd.read_csv("dataset.csv")

print("1) SHAPE (rows, columns):", df.shape, "\n")

print("2) COLUMN NAMES:")
print(df.columns.tolist(), "\n")

print("3) DTYPEs:")
print(df.dtypes, "\n")

print("4) FIRST 10 ROWS:")
print(df.head(10).to_string(index=False), "\n")

print("5) SUMMARY STATISTICS (numeric):")
print(df.describe().round(3).to_string(), "\n")

print("6) MISSING VALUES PER COLUMN:")
print(df.isnull().sum(), "\n")

# Quick check for required columns
required = ["experience", "test_score", "salary"]
found = [c.lower().strip().replace(" ", "_") for c in df.columns.tolist()]
print("Normalized column names (for matching):", found, "\n")

missing_required = [c for c in required if c not in found]
if missing_required:
    print("WARNING: the following required columns are NOT present:", missing_required)
    print("If your column names are different (e.g., 'YearsExperience' or 'interview_score'), rename them or tell me the printed column names.")
else:
    print("All required columns are present (experience, test_score, salary).")

print("\nStep 1 complete. If everything looks fine, reply with:  Step 1 done")
