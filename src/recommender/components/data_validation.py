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

            for file, expected_columns in required_files.items():

                path = os.path.join(
                    self.config.data_ingestion_dir, 
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

            os.makedirs(
                    self.config.root_dir,
                    exist_ok=True
                )
                
            if status:

                logging.info("Data Validation completed successfully")
                with open(self.config.status_file, "w") as file:
                    file.write( "Validation Status: PASS\n"
                                "All validation checks completed successfully.")

            else:

                logging.error("Data Validation Failed")
                with open(self.config.status_file, "w") as file:
                    file.write( "Validation Status: FAIL\n"
                                "Please check the log file for details.")
            return status

        
        except Exception as e:
            raise CustomException(e, sys)
