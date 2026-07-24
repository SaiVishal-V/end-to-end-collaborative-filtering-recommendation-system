import os 
import pandas as pd
import sys


from src.recommender.entity.config_entity import DataValidationConfig
from src.recommender.exception import CustomException
from src.recommender.logger import logging

class DataValidation:

    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_files(self):

        try:
            logging.info("Starting Data Validation")

            status = True

            required_files = [
                "movies.csv",
                "ratings.csv",
                "tags.csv",
                "links.csv"
            ]

            for file in required_files:

                path = os.path.join(
                    "artifacts/data_ingestion",
                    file
                )

                if not os.path.exists(path):
                    logging.error(f"{file} not found")
                    status = False 

                if status:
                    logging.info("All required files found.")

                return status
        except Exception as e:
            raise CustomException(e, sys)
