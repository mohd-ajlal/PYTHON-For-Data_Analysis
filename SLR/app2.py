import streamlit as st
import pickle
import numpy as np

with open('data.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("Fan Loyalty Predictor")

age = st.number_input("Age 10-100", min_value=10, max_value=100)
income = st.number_input("Income 0-1000000", min_value=0, max_value=1000000)
years_as_fan = st.number_input("Years as Fan 0-50", min_value=0, max_value=50)
games_attended = st.number_input("Number of Games Attended 0-100", min_value=0, max_value=100)
team_performance = st.number_input("Team Performance Rating 0.0-10.0", min_value=0.0, max_value=10.0)
engagement = st.selectbox("Engagement with Team", options=[0, 1, 2])


user_data = np.array([[age, income, years_as_fan, games_attended, team_performance, engagement]])


if st.button("Predict"):
    prediction = model.predict(user_data)
    st.write(f"The predicted loyalty is: {'Loyal' if prediction[0] == 1 else 'Not Loyal'}")
