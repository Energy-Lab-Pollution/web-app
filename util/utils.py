"""
Script with util functions
"""

import logging
from io import StringIO

import boto3
import botocore
import botocore.exceptions
import pandas as pd

from util.constants import BUCKET_NAME, REGION_NAME

# Set logger

logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3_client = boto3.client("s3", region_name=REGION_NAME)


def extract_dataframe(filename):
    """
    Parses a dataframe from S3
    """
    try:
        object = s3_client.get_object(Bucket=BUCKET_NAME, Key=filename)
        logger.info("Getting .csv file")
        csv_string = object["Body"].read()
        df = pd.read_csv(StringIO(csv_string))

    except botocore.exceptions.ClientError as error:
        logger.error(error)
        df = pd.DataFrame([])

    return df


def extract_image(object, filename):
    """
    Extracts an image from S3
    """
    try:
        object = s3_client.get_object(Bucket=BUCKET_NAME, Key=filename)
        logger.info("Getting image")
        data = object["Body"].read()

    except botocore.exceptions.ClientError as error:
        logger.error(error)
        data = None

    return data


def extract_from_s3(filename):
    """
    Extracts data from S3
    """
    if ".csv" in filename:
        data = extract_dataframe(filename)

    else:
        data = extract_image(filename)

    return data


def upload_to_s3(local_filename, s3_filename):
    """
    Uploads a given file to S3
    """

    try:
        s3_client.upload_file(
            Filename=local_filename, Bucket=BUCKET_NAME, Key=s3_filename
        )

    except botocore.exceptions.ClientError:
        logger.info("Upload unsuccessful")
