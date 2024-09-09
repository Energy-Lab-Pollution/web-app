"""
File with class to extract csv files and data from AWS
"""

from util.constants import IMAGE_FOLDER, CSV_FOLDER
from util.utils import extract_from_s3


class DataWrapper:
    def __init__(self, city):

        self.cigarettes_plot = extract_from_s3(
            f"/{IMAGE_FOLDER}/{city}_cigarrettes_2024_python.png"
        )
        self.air_quality_plot = extract_from_s3(
            f"/{IMAGE_FOLDER}/{city}_air_quality_2024_python.png"
        )
        self.annual_plot = extract_from_s3(
            f"/{IMAGE_FOLDER}/{city}_annual_2024_python.png"
        )

        self.cigarettes_csv = extract_from_s3(
            f"/{CSV_FOLDER}/{city}_cigarrettes_2024.csv"
        )
        self.air_quality_csv = extract_from_s3(
            f"/{CSV_FOLDER}/{city}_air_quality_2024.csv"
        )
        self.annual_csv = extract_from_s3(
            f"/{CSV_FOLDER}/{city}_annual_2024.csv"
        )
