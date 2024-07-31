from controller.model import LoadModel
from controller.prediction import GetPrediction
from controller.scalar import LoadScalar
import numpy as np
import pandas as pd
import streamlit as st

st.title("Diabetic Prediction")
# Gender
gender_options = ["Male", "Female"]
gender = st.selectbox("Gender: ", gender_options)
if gender == "Male":
    gender = 1
else:
    gender = 0
# Age
age = np.log(st.number_input('Age', min_value=0.080, max_value=80.0, step=1.0))
# hypertension
hypertension_options = ["Yes", "No"]
hypertension = st.selectbox("Do you have hypertension? ", hypertension_options)
if hypertension == "Yes":
    hypertension = 1
else:
    hypertension = 0
# Heart Disease
heart_disease_options = ["Yes", "No"]
heart_disease = st.selectbox("Do you have heart disease? ", heart_disease_options)
if heart_disease == "Yes":
    heart_disease = 1
else:
    heart_disease = 0
# Smoking
smoking_dict = {
    'never': 4,
    'no info': 0,
    'former': 3,
    'current': 1,
    'not current': 5,
    'ever': 2
}
# hypertension
smoking_options = ["never", "no info", 'former', 'current', 'not current', 'ever']
smoking = st.selectbox("Do you have hypertension? ", smoking_options)
smoking = smoking_dict[smoking]
# BMI
bmi = np.log(st.number_input('bmi', min_value=10.010000, max_value=95.690000, step=1.0))
# HbA1c_level
hba1c_level = np.log(st.number_input('HbA1c_level', min_value=3.5, max_value=9.0, step=1.0))
# blood_glucose_level
blood_glucose_level = np.log(st.number_input('blood glucose level', min_value=80.0, max_value=300.0, step=1.0))

new_data = pd.DataFrame({
    'age': [age],
    'bmi': [bmi],
    'HbA1c_level': [hba1c_level],
    'blood_glucose_level': [blood_glucose_level]
})
lr = LoadScalar()
transformed_data = lr.transform(new_data)
data = pd.DataFrame({
    'gender': [gender],
    'age': transformed_data[0][0],
    'hypertension': [hypertension],
    'heart_disease': [heart_disease],
    'smoking_history': [smoking],
    'bmi': transformed_data[0][1],
    'HbA1c_level': transformed_data[0][2],
    'blood_glucose_level': transformed_data[0][3]
})
model = LoadModel()
if st.button("Predict"):
    prediction = GetPrediction(model, data)
    st.write(f"{prediction}")
