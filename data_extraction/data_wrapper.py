"""
File with class to extract csv files and data from AWS
"""
import io

import pandas as pd

from util.constants import CSV_FOLDER, IMAGE_FOLDER, PRESENT_YEAR
from util.utils import extract_from_s3


class DataWrapper:
    def __init__(self, city):

        self.cigarettes_plot = extract_from_s3(
            f"{IMAGE_FOLDER}/{city}_cigarettes_{PRESENT_YEAR}.png"
        )
        self.air_quality_plot = extract_from_s3(
            f"{IMAGE_FOLDER}/{city}_air_quality_{PRESENT_YEAR}.png"
        )
        self.annual_plot = extract_from_s3(
            f"{IMAGE_FOLDER}/{city}_annual_{PRESENT_YEAR}.png"
        )

        self.cigarettes_csv = extract_from_s3(
            f"{CSV_FOLDER}/{city}_cigarettes_{PRESENT_YEAR}.csv"
        )
        self.air_quality_csv = extract_from_s3(f"{CSV_FOLDER}/{city}_daily_{PRESENT_YEAR}.csv")
        self.annual_csv = extract_from_s3(f"{CSV_FOLDER}/{city}_annual.csv")

        # Convert to dataframe
        self.cigarettes_df = pd.read_csv(io.StringIO(self.cigarettes_csv))
        self.air_quality_df = pd.read_csv(io.StringIO(self.air_quality_csv))
        self.annual_df = pd.read_csv(io.StringIO(self.annual_csv))

