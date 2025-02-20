import streamlit as st
import pandas as pd
from layout import setup_layout
from sidebar import setup_sidebar
from data import load_data, save_data
from model import predict_salary, train_model
from plots import create_interactive_plot, create_static_plot

# Main Title and Image
st.title("Salary Predictor")
st.image("data/sal.jpg", width=800)

# Sidebar Navigation
nav = setup_sidebar()  # Sidebar options from sidebar.py

# Load Data and Train Model
data = load_data("data/Salary_Data.csv")
lr_model = train_model(data)

# Layout Setup Based on Navigation
if nav == "Home":
    setup_layout(data, lr_model)
elif nav == "Prediction":
    years_exp = st.number_input("Enter your experience in years", 0.00, 20.00, step=0.25)
    prediction = predict_salary(lr_model, years_exp)
    if st.button("Predict"):
        st.success(f"Your predicted salary is {round(prediction)}")
elif nav == "Contribute":
    st.header("Contribute to our dataset")
    exp = st.number_input("Enter your Experience", 0.0, 20.0)
    sal = st.number_input("Enter your Salary", 0.0, 1000000.0, step=1000.0)
    if st.button("Submit"):
        save_data(exp, sal, "data/Salary_Data.csv")
        st.success("Submitted")
