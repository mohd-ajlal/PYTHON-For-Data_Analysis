import streamlit as st
import pickle
import numpy as np

with open('student_exam_score_model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("Student Exam Score Predictor")

hours_studied = st.number_input('Hours Studied', min_value=0.0, step=0.5)
practice_tests = st.number_input('Number of Practice Tests', min_value=0, step=1)
attendance_rate = st.number_input('Attendance Rate (in %)', min_value=0.0, max_value=100.0, step=1.0)
sleep_hours = st.number_input('Sleep Hours', min_value=0.0, step=0.5)

# Predict button
if st.button('Predict Exam Score'):
    input_data = np.array([[hours_studied, practice_tests, attendance_rate, sleep_hours]])
    
    predicted_score = model.predict(input_data)[0]
    
    st.write(f"Predicted Exam Score: {predicted_score:.2f}")
