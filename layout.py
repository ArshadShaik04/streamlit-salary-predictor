import streamlit as st
from plots import create_static_plot, create_interactive_plot

def setup_layout(data, model):
    if st.checkbox("Show Table"):
        st.table(data)

    graph_type = st.selectbox("Choose Graph Type", ["Non-Interactive", "Interactive"])
    years_filter = st.slider("Filter data by experience", 0, 20)
    filtered_data = data[data["YearsExperience"] >= years_filter]

    if graph_type == "Non-Interactive":
        create_static_plot(filtered_data)
    else:
        create_interactive_plot(filtered_data)
