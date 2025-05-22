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
LOGO_PATH = """eel-logo.png"""
CITIES = ["Chiang Mai", "Kigali", "Kanpur", "Kolkata", "Guatemala City"]

CIGARETTES_CONSTANT = 22
WHO_STD_ANNUAL = 5
WHO_STD_DAILY = 15


today = date.today()
PRESENT_YEAR = str(today.year)
MINDATE = date(today.year, 1, 1)
