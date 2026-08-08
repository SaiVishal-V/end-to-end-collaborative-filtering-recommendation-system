import os
import sys 
import pandas as pd

from src.recommender.entity.config_entity import DataTransformationConfig
from src.recommender.exception import CustomException
from src.recommender.logger import logging

class DataTransformation:

    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def initiate_data_transformation(self):

        try:
            logging.info("Start Data Transformation")

            #Create transformation artifact directory

            os.makedirs(
                self.config.root_dir,
                exist_ok=True
            )

            # Paths to ingested datasets

            movies_path = "artifacts/data_ingestions/movies.csv"
            ratings_path = "artifacts/data_ingestions/ratings.csv"

            # Read the datasets

            movies = pd.read_csv(movies_path)
            ratings = pd.read_csv(ratings_path)

            logging.info("Movies and Ratings datasets are loaded successfully")

            # Merge movies and ratings datasets using the movieID

            merged_data = pd.merge(
                ratings,
                movies,
                on="movieId",
                how="inner"
            )

            logging.info(f"Merged dataset created with {merged_data.shape[0]} rows")

            # Save the merged dataset

            merged_data.to_csv(
                self.config.merged_data_path,
                index=False
            )

            logging.info("Merged dataset saved successfully")

            # Creating user-movie interaction matrix
            pivot_table = merged_data.pivot_table(
                index="title",
                columns="userId",
                values="rating"
            )

            #Replace missing ratings with 0 (handling nulls)
            pivot_table = pivot_table.fillna(0)

            logging.info(
                f"Pivot table created with shape {pivot_table.shape}"
            )

            # Save the pivot table
            pivot_table.to_pickle(
                self.config.pivot_table_path
            )

            logging.info("Pivot table saved successfully")

            logging.info("Data Transformation completed successfully")

            return self.config.pivot_table_path

        except Exception as e:
            logging.error(
                f"Error occured during Data Transformation: {e}"
            )

            raise CustomException(e, sys)

