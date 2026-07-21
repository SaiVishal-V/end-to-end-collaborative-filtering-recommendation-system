import os
import shutil
import sys

from src.recommender.entity.config_entity import DataIngestionConfig
from src.recommender.exception import CustomException
from src.recommender.logger import logging


class DataIngestion:
    
    
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def initiate_data_ingestion(self):
        try:
            logging.info("Starting Data Ingestion")


            os.makedirs(
                self.config.root_dir,
                exist_ok=True
            )

            logging.info("Artifact Directory created successfully.")

            shutil.copy(
                self.config.movies_path,
                self.config.root_dir
            )

            logging.info("movies.csv copied successfully")

            shutil.copy(
                self.config.ratings_path,
                self.config.root_dir
            )

            logging.info("ratings.csv copied successfully")

            shutil.copy(
                self.config.tags_path,
                self.config.root_dir 
            )

            logging.info("tags.csv copied successfully.")

            shutil.copy(
                self.config.links_path,
                self.config.root_dir
            )

            logging.info("links.csv copied successfully.")

            logging.info("Data Ingestios completed successfully.")

        except Exception as e:
            logging.error(f"Error occured during Data Ingestion: {e}")
            raise CustomException(e, sys)
        
"""
Basically we are trying to log everything for faster debuging.
So the try gives a headsup to be prepared if something goes wrong.
If indeed something goes wrong the except catches the exception and stores it in e.
Then instead of ignoring the exceptions we raise it and wrap it up with our CustomException we built.

"""