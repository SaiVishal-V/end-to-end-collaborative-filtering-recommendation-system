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

            required_files = {
                                "movies.csv": ["movieId", "title", "genres"],
                                "ratings.csv": ["userId", "movieId", "rating", "timestamp"],
                                "tags.csv": ["userId", "movieId", "tag", "timestamp"],
                                "links.csv": ["movieId", "imdbId", "tmdbId"]
                            }

            for file, expected_columns in required_files:

                path = os.path.join(
                    "artifacts/data_ingestion", #Replce if not working [ self.config.data_ingestion_dir ]
                    file
                )

                if not os.path.exists(path):
                    logging.error(f"{file} not found")
                    status = False
                    continue 
                #Check file is not empty
                if os.path.getsize(path)==0:

                    logging.error(f"{file} is empty.")
                    status = False
                    continue
                # Read file
                df = pd.read_csv(path)

                # Validate Columns
                missing_columns = [
                    col for col in expected_columns
                    if col not in df.columns
                ]

                if missing_columns:

                    logging.error(f"{file} missing columns: {missing_columns}")
                status = False
                
            if status:
                logging.info("Data Validation completed successfully")
            else:
                logging.error("Data Validation Failed")
                
        except Exception as e:
            raise CustomException(e, sys)
