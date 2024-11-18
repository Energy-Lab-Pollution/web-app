"""
File with constants to use throughout the project
"""

from datetime import date

# AWS Constants
BUCKET_NAME = "global-rct-plumelabs"
IMAGE_FOLDER = "plots"
CSV_FOLDER = "plots_data"
REGION_NAME = "us-west-1"


# STREAMLIT CONSTANTS
LOGO_URL = """https://epic.uchicago.edu/wp-content/uploads/2019/04/3.2_UrbanLabs_EnergyEnvironment_Maroon@2x_margin-e1570565607710.png"""
CITIES = ["Chiang Mai", "Kigali", "Kanpur", "Kolkata"]

CIGARETTES_CONSTANT = 22
WHO_STD_ANNUAL = 5
WHO_STD_DAILY = 15


today = date.today()
PRESENT_YEAR = str(today.year)
MINDATE = date(today.year, 1, 1)
