import pandas as pd
import streamlit as st

@st.cache_data
def load_data(filepath):
    return pd.read_csv(filepath)

def save_data(experience, salary, filepath="data/Salary_Data.csv"):
    new_data = pd.DataFrame({"YearsExperience": [experience], "Salary": [salary]})
    new_data.to_csv(filepath, mode='a', header=False, index=False)
