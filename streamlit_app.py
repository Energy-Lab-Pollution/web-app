"""
This script contains the necessary code for the streamlit app
for the Energy Lab at UChicago
"""

from datetime import datetime

# Global imports
import pytz
import streamlit as st

# Local imports
from data_extraction.data_wrapper import DataWrapper
from util.constants import CITIES, LOGO_URL
from visualizations.create_visualizations import (
    create_annual_plot,
    create_cigarettes_plot,
    create_lineplot,
)

# App layout
st.set_page_config(page_title="Pollution Monitoring App", page_icon=":bar_chart:")

# Date
today = datetime.now(pytz.timezone("America/Chicago"))
str_today = datetime.strftime(today, "%Y-%m-%d")
# Custom CSS for basic styling

# Title and logo
st.title("🌍 UChicago Energy & Environment Lab - Pollution Monitoring App")
st.sidebar.image(LOGO_URL)

# Sidebar: Static vs Interactive plot selector
plot_type = st.sidebar.selectbox("Choose Plot Type:", ("Static", "Interactive"))
view_data_only = st.sidebar.checkbox("View Data Only")
city_choice = st.selectbox("Select a city to fetch data and visualize", CITIES)


if st.button("Run"):
    data_wrapper = DataWrapper(city_choice)

    if view_data_only:
        st.header(f"Data for {city_choice}")

        st.subheader("Daily PM2.5 Data")
        st.dataframe(data_wrapper.air_quality_df)  # Show the dataframe
        st.download_button(
            label="Download Data as CSV",
            data=data_wrapper.air_quality_csv,
            file_name=f"{city_choice}_data_{str_today}.csv",
            mime="text/csv",
        )

        st.subheader("Cigarettes Consumption Data")
        st.dataframe(data_wrapper.cigarettes_df)  # Show the dataframe
        st.download_button(
            label="Download Data as CSV",
            data=data_wrapper.cigarettes_df,
            file_name=f"{city_choice}_data_{str_today}.csv",
            mime="text/csv",
        )

        st.subheader("Annual PM2.5 Data")
        st.dataframe(data_wrapper.annual_df)  # Show the dataframe
        st.download_button(
            label="Download Data as CSV",
            data=data_wrapper.annual_df,
            file_name=f"{city_choice}_annual_data_{str_today}.csv",
            mime="text/csv",
        )

    else:

        if plot_type == "Static":
            # Daily plot
            st.subheader(f"PM2.5 Daily Plot for {city_choice} (Static)")
            st.image(data_wrapper.air_quality_plot)
            st.download_button(
                label="Download Daily Data as CSV",
                data=data_wrapper.air_quality_csv,
                file_name=f"{city_choice}_daily_data_{str_today}.csv",
                mime="text/csv",
            )

            st.subheader(f"Cigarettes Consumption Plot for {city_choice} (Static)")
            # Cigarrete plot
            st.image(data_wrapper.cigarettes_plot)
            st.download_button(
                label="Download Cigarettes Data as CSV",
                data=data_wrapper.cigarettes_csv,
                file_name=f"{city_choice}_cigarettes_data_{str_today}.csv",
                mime="text/csv",
            )

            # Annual plot
            st.subheader(f"Annual PM2.5 Data for {city_choice} (Static)")
            st.image(data_wrapper.annual_plot)
            st.download_button(
                label="Download Annual Data as CSV",
                data=data_wrapper.annual_csv,
                file_name=f"{city_choice}_annual_data_{str_today}.csv",
                mime="text/csv",
            )

        else:
            # Interactive Plotly plots
            st.subheader(f"PM2.5 Daily Plot for {city_choice} (Interactive)")
            lineplot = create_lineplot(data_wrapper.air_quality_csv, city_choice)
            st.plotly_chart(lineplot)
            st.download_button(
                label="Download Daily Data as CSV",
                data=data_wrapper.air_quality_csv,
                file_name=f"{city_choice}_daily_data.csv",
                mime="text/csv",
            )

            st.subheader(f"Cigarettes Consumption for {city_choice} (Interactive)")
            cigarettes_plot = create_cigarettes_plot(
                data_wrapper.air_quality_csv, city_choice
            )
            st.plotly_chart(cigarettes_plot)
            st.download_button(
                label="Download Cigarettes Data as CSV",
                data=data_wrapper.cigarettes_csv,
                file_name=f"{city_choice}_cigarettes_data.csv",
                mime="text/csv",
            )

            st.subheader(f"Annual PM2.5 Data for {city_choice} (Interactive)")
            annual_plot = create_annual_plot(data_wrapper.annual_csv, city_choice)
            st.plotly_chart(annual_plot)
            st.download_button(
                label="Download Annual Data as CSV",
                data=data_wrapper.annual_csv,  # Changed to annual CSV data
                file_name=f"{city_choice}_annual_data.csv",
                mime="text/csv",
            )


st.sidebar.markdown(
    "**Pollution Monitoring App** developed by the Energy Lab at UChicago"
)

st.sidebar.markdown("_Note: We are using daily PM2.5 data provided by PlumeLabs_")
