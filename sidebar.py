import streamlit as st

def setup_sidebar():
    st.sidebar.header("Navigation")
    return st.sidebar.radio("Choose an option", ["Home", "Prediction", "Contribute"])
