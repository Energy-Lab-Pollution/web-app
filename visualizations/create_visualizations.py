"""
Script to create Plotly Visualizations
"""

import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

from util.constants import CIGARETTES_CONSTANT, MINDATE, WHO_STD_ANNUAL


def create_lineplot(daily_df, city):
    """
    Creates an interactive line plot for a given city from a certain date using Plotly.
    """
    # Filter the data for the specific city and date range
    city_daily = daily_df[
        (daily_df["city"] == city)
        & (daily_df["date"] >= MINDATE)
    ]

    # Count the number of violations
    num_violate_nat = city_daily[city_daily["violate_daily_nat"]].shape[0]
    num_violate_who = city_daily[city_daily["violate_daily_who"]].shape[0]

    # Create interactive Plotly line plot
    fig = px.line(
        city_daily,
        x="date",
        y="pm2.5",
        title=(
            f"In 2024, {city} experienced air quality exceeding the national standard "
            f"for {num_violate_nat} days and WHO standards for {num_violate_who} days"
        ),
        labels={"pm2.5": "PM2.5 Levels", "date": "Date"}
    )

    # Add horizontal lines for national and WHO standards
    fig.add_hline(
        y=city_daily["nat_std_daily"].iloc[0],
        line_dash="dash",
        line_color="blue",
        annotation_text="Nat. Std. - Daily",
        annotation_position="top left"
    )
    fig.add_hline(
        y=15,
        line_dash="dash",
        line_color="red",
        annotation_text="WHO Std. - Daily",
        annotation_position="bottom left"
    )

    return fig


def create_cigarettes_plot(daily_df, city):
    """
    Creates an interactive bar plot with weekly cigarettes consumption using Plotly.
    """
    # Filter the data for the specific city and date range
    city_daily = daily_df[
        (daily_df["city"] == city)
        & (daily_df["date"] >= MINDATE)
    ]
    city_daily["cigarettes"] = city_daily["pm2.5"] / CIGARETTES_CONSTANT
    annual_total = round(city_daily["cigarettes"].sum(), 1)

    # Group by week and summarize
    city_daily["week"] = (
        city_daily["date"].dt.to_period("W").apply(lambda r: r.start_time)
    )
    weekly_summary = city_daily.groupby("week").agg({"cigarettes": "sum"}).reset_index()

    # Create interactive Plotly bar chart
    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=weekly_summary["week"],
            y=weekly_summary["cigarettes"],
            name="Cigarettes",
            marker_color="#e41a1c"
        )
    )

    fig.update_layout(
        title=f"In {city}, exposure to PM2.5 in 2024 has been the equivalent of smoking {annual_total} cigarettes",
        xaxis_title="Week",
        yaxis_title="Cigarettes",
        xaxis_tickformat="%B",
        xaxis_tickangle=-45
    )

    return fig


def create_annual_plot(annual_df, city):
    """
    Function to plot annual PM2.5 data for a given city and add horizontal lines
    for national and WHO standards using Plotly.

    Returns:
    - fig: The Plotly figure object to be used in the Streamlit app.
    """
    city_annual = annual_df[annual_df["city"] == city]
  
    # Check if there's data for the city
    if city_annual.empty:
        st.warning(f"No data available for city: {city}")
        return

    # Extract national standard value
    nat_std_annual = city_annual["nat_std_daily"].iloc[0]

    # Create interactive Plotly bar chart
    fig = go.Figure()

    # Create the bar chart for PM2.5 levels
    fig.add_trace(
        go.Bar(
            x=city_annual["year"],
            y=city_annual["pm2.5"],
            name="PM2.5",
            marker_color="#ff7f00"
        )
    )

    # Add horizontal lines for national and WHO standards
    fig.add_hline(
        y=nat_std_annual,
        line_dash="dash",
        line_color="blue",
        annotation_text="Nat. Std. - Annual",
        annotation_position="top left"
    )
    fig.add_hline(
        y=WHO_STD_ANNUAL,
        line_dash="dash",
        line_color="red",
        annotation_text="WHO Std. - Annual",
        annotation_position="bottom left"
    )

    # Customize layout
    fig.update_layout(
        title=f"Annual Historical Data for {city}",
        xaxis_title="Year",
        yaxis_title="PM2.5",
        xaxis=dict(tickmode='linear', tick0=city_annual["year"].min(), dtick=5),  # Tick every 5 years
        showlegend=True,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )


    # Return the Plotly figure
    return fig