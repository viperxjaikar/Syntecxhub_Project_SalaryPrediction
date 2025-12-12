import pandas as pd
import joblib

print("===== STEP 7: EXAMPLE PREDICTION =====\n")

# Load the saved best model
model = joblib.load("best_salary_model.pkl")

# Example input (you can change these values)
input_data = pd.DataFrame({
    "experience": [5],
    "test_score": [80]
})

print("Input Data:")
print(input_data, "\n")

# Predict salary
prediction = model.predict(input_data)[0]

print("Predicted Salary:", round(prediction, 2))
