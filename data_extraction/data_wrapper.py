"""
File with class to extract csv files and data from AWS
"""
import io

import pandas as pd

from util.constants import CSV_FOLDER, IMAGE_FOLDER
from util.utils import extract_from_s3


class DataWrapper:
    def __init__(self, city):

        self.cigarettes_plot = extract_from_s3(
            f"{IMAGE_FOLDER}/{city}_cigarettes_2024.png"
        )
        self.air_quality_plot = extract_from_s3(
            f"{IMAGE_FOLDER}/{city}_air_quality_2024.png"
        )
        self.annual_plot = extract_from_s3(
            f"{IMAGE_FOLDER}/{city}_annual_2024.png"
        )

        self.cigarettes_csv = extract_from_s3(
            f"{CSV_FOLDER}/{city}_cigarettes_2024.csv"
        )
        self.air_quality_csv = extract_from_s3(f"{CSV_FOLDER}/{city}_daily_2024.csv")
        self.annual_csv = extract_from_s3(f"{CSV_FOLDER}/{city}_annual.csv")

        # Convert to dataframe
        self.cigarettes_df = pd.read_csv(io.StringIO(self.cigarettes_csv))
        self.air_quality_df = pd.read_csv(io.StringIO(self.air_quality_csv))
        self.annual_df = pd.read_csv(io.StringIO(self.annual_csv))

