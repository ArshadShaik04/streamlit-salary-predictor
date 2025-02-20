import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def create_static_plot(data):
    fig, ax = plt.subplots()  # ✅ Fix: Create a figure object
    ax.scatter(data["YearsExperience"], data["Salary"])
    ax.set_xlabel("Years of Experience")
    ax.set_ylabel("Salary")
    ax.set_title("Experience vs Salary")
    st.pyplot(fig)  # ✅ Fix: Pass figure to st.pyplot()

def create_interactive_plot(data):
    import plotly.express as px
    fig = px.scatter(data, x="YearsExperience", y="Salary", title="Experience vs Salary")
    st.plotly_chart(fig)
