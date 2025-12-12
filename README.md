📌 Salary Prediction — Syntecxhub Internship (Project 2)

This repository contains my solution for Project 2: Salary Prediction, completed as part of the Syntecxhub Internship Program.

The project uses experience and test score to build a Salary Prediction Regression Model, compares single vs multiple linear regression models, evaluates with RMSE and R², and saves the best performing model.

✅ Project Requirements (from Syntecxhub)

Use dataset containing experience, test scores, salary

Handle categorical features if present

Perform train/test split

Train multiple linear regression

Evaluate using RMSE & R²

Compare single vs multiple feature models

Save best model

📂 Project Structure
SalaryPrediction_Project/
│── dataset.csv                # original dataset 
│── salary_cleaned.csv         # cleaned dataset after preprocessing
│── 01_load_inspect.py         # Step 1: load + inspect dataset
│── 02_preprocess.py           # Step 2: preprocessing (handle missing data)
│── 03_train.py                # Steps 3–6: training, evaluation, save best model
│── 04_predict.py              # Step 7: example prediction using best model
│── best_salary_model.pkl      # saved best ML model
│── README.md                  # project documentation

🧪 Steps Performed
STEP 1 — Load & Inspect

Checked shape, columns, data types

Verified presence of required columns

Checked missing values

STEP 2 — Preprocess

Normalized column names

Converted non-numeric values

Filled missing values using median

Saved cleaned dataset as salary_cleaned.csv

STEP 3–6 — Train & Evaluate Models

Two models were trained:

1️⃣ Single Feature Regression

Feature: experience

2️⃣ Multiple Feature Regression

Features: experience, test_score

Both models evaluated using:

RMSE (Root Mean Squared Error)

R² Score

Results
Model	RMSE	R²
Single Feature	9743.88	0.5516
Multiple Feature	9651.39	0.5601

👉 Best Model: Multiple Linear Regression
Saved as: best_salary_model.pkl

🎯 STEP 7 — Example Prediction

Using 04_predict.py:

Experience = 5
Test Score = 80
Predicted Salary ≈ 56,000+


(Values may vary slightly.)

▶️ How to Run the Project
Install dependencies:
pip install pandas scikit-learn joblib

Run scripts in order:
python 01_load_inspect.py
python 02_preprocess.py
python 03_train.py
python 04_predict.py

📝 Internship Submission Checklist

 Completed Project 2

 Shared internship status on LinkedIn & tagged @Syntecxhub

 Uploaded full source code to GitHub

 Repository name format:

Syntecxhub_Project_SalaryPrediction

👨‍💻 Author

Your Name
LinkedIn: add your profile link
GitHub: add your link

⭐ Thank You

If you found this project helpful, please ⭐ the repository!
