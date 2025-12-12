# 03_train.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib

print("===== STEP 3–6: TRAINING & EVALUATION =====\n")

# Load cleaned dataset (from Step 2)
df = pd.read_csv("salary_cleaned.csv")

# -------------------------
# FEATURES AND TARGET
# -------------------------
# MULTIPLE FEATURE MODEL
X_multi = df[["experience", "test_score"]]
y = df["salary"]

# SINGLE FEATURE MODEL
X_single = df[["experience"]]

# -------------------------
# TRAIN / TEST SPLIT
# -------------------------
X_train_m, X_test_m, y_train, y_test = train_test_split(
    X_multi, y, test_size=0.2, random_state=42)

X_train_s, X_test_s, _, _ = train_test_split(
    X_single, y, test_size=0.2, random_state=42)

# -------------------------
# MODEL 1: SINGLE FEATURE
# -------------------------
model_single = LinearRegression()
model_single.fit(X_train_s, y_train)

pred_single = model_single.predict(X_test_s)

# FIXED: manually compute RMSE
rmse_single = mean_squared_error(y_test, pred_single) ** 0.5
r2_single = r2_score(y_test, pred_single)

print("Single Feature Model (experience only)")
print("RMSE:", rmse_single)
print("R²:", r2_single, "\n")

# -------------------------
# MODEL 2: MULTIPLE FEATURES
# -------------------------
model_multi = LinearRegression()
model_multi.fit(X_train_m, y_train)

pred_multi = model_multi.predict(X_test_m)

# FIXED: manually compute RMSE
rmse_multi = mean_squared_error(y_test, pred_multi) ** 0.5
r2_multi = r2_score(y_test, pred_multi)

print("Multiple Feature Model (experience + test_score)")
print("RMSE:", rmse_multi)
print("R²:", r2_multi, "\n")

# -------------------------
# COMPARE & SAVE BEST MODEL
# -------------------------
print("===== MODEL COMPARISON =====")
print("Single Feature RMSE:", rmse_single)
print("Multiple Feature RMSE:", rmse_multi)

if rmse_multi < rmse_single:
    joblib.dump(model_multi, "best_salary_model.pkl")
    print("\nBEST MODEL: Multiple Linear Regression (saved as best_salary_model.pkl)")
else:
    joblib.dump(model_single, "best_salary_model.pkl")
    print("\nBEST MODEL: Single Linear Regression (saved as best_salary_model.pkl)")

print("\nTraining Complete!")
