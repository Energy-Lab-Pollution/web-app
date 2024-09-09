"""
This script contains the necessary code for the streamlit app
for the Energy Lab at UChicago
"""

# Global imports
import streamlit as st

# Local imports
from util.constants import CITIES, LOGO_URL
from data_extraction.data_wrapper import DataWrapper


# App layout
st.set_page_config(
    page_title="Pollution Monitoring App", page_icon=":bar_chart:"
)

# Custom CSS for basic styling

# Title and logo
st.title("UChicago Energy & Environment Lab - Pollution Monitoring App")
st.sidebar.image(LOGO_URL)

# Add a selector for the user to choose a city
city_choice = st.selectbox("Select a city to fetch data and visualize", CITIES)

if st.button("Run"):
    data_wrapper = DataWrapper(city_choice)
