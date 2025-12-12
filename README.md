# Salary Prediction Project

Simple linear regression example to predict salary from experience and test scores.

Files
- `01_load_inspect.py` — load and inspect dataset
- `02_preprocess.py` — data cleaning and preprocessing
- `03_train.py` — train and save the best model
- `04_predict.py` — example prediction using saved model
- `dataset.csv`, `salary_cleaned.csv` — data files

Requirements
- Python 3.8+
- pandas
- scikit-learn
- joblib

Install

```powershell
python -m pip install -r requirements.txt
# or
python -m pip install pandas scikit-learn joblib
```

Quick usage

1. Inspect and preprocess data
```powershell
python 01_load_inspect.py
python 02_preprocess.py
```
2. Train model
```powershell
python 03_train.py
```
3. Make a prediction
```powershell
python 04_predict.py
```

Notes
- Pushing to GitHub requires you to have git installed and authentication set up (HTTPS with PAT or SSH key).
- If `requirements.txt` is not present, install the packages listed under Requirements manually.
