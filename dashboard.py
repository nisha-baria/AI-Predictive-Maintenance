import streamlit as st
import requests

st.title("AI Predictive Maintenance System")

temp = st.number_input("Temperature")
vib = st.number_input("Vibration")
curr = st.number_input("Current")

if st.button("Predict"):
    response = requests.post("http://127.0.0.1:5000/predict", json={
        "temperature": temp,
        "vibration": vib,
        "current": curr
    })

    st.success(response.json()["prediction"])