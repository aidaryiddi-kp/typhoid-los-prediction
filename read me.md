# Typhoid Length of Stay (LOS) Prediction — Bugando Medical Centre

A machine learning system that predicts the expected hospital Length of Stay 
for typhoid patients, built during an internship with the ICT Department at 
Bugando Medical Centre.

## Project Overview
This project uses patient demographic and clinical data to predict how many 
days a typhoid patient is likely to remain hospitalized, supporting bed 
capacity and resource planning.

## Features
- Data cleaning and exploratory data analysis (EDA)
- Model comparison: Linear Regression, Random Forest, XGBoost
- Hyperparameter tuning with GridSearchCV
- Interactive web application built with Streamlit

## Model Performance
| Model | MAE | RMSE | R² |
|---|---|---|---|
| Linear Regression | 0.94 | 1.20 | 0.773 |
| Random Forest (Tuned) | 0.90 | 1.14 | 0.795 |
| XGBoost | 0.97 | 1.23 | 0.762 |

## Note on Data
This project currently uses synthetic/simulated data modeled on typical 
hospital HMIS structure, due to patient data privacy considerations. 

## Tech Stack
Python, Pandas, Scikit-learn, XGBoost, Streamlit, Seaborn/Matplotlib

## Author
Aidary Iddi — Bachelor of Engineering in Data Science, Mbeya University of Science and Technology