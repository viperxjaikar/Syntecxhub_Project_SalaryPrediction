💰 Salary Prediction Model
Syntecxhub Internship Project 2
Predict salary based on experience and test scores using linear regression.

📊 Results
Model	RMSE	R² Score
Single Feature	9,743.88	0.5516
Multiple Feature	9,651.39	0.5601
🚀 Quick Start
bash
# Install dependencies
pip install pandas scikit-learn joblib

# Run all steps
python 01_load_inspect.py
python 02_preprocess.py
python 03_train.py
python 04_predict.py
📁 Files
dataset.csv - Original data

salary_cleaned.csv - Processed data

best_salary_model.pkl - Trained model

01-04_*.py - Step-by-step scripts

📝 Example Prediction
python
Input: Experience=5, Test Score=80
Output: Salary ≈ $56,000+
