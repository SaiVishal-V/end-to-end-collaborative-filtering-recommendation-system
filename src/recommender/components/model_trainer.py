import os
import sys
import pandas as pd

from sklearn.neighbors import NearestNeighbors

from src.recommender.entity.config_entity import ModelTrainerConfig
from src.recommender.exception import CustomException
from src.recommender.logger import logging

class ModelTrainer:

    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def initiate_model_training(self):

        try :

            logging.info("Starting Model Training")

            #Create model artifact directory
            os.makedirs(
                self.config.root_dir,
                exist_ok=True
            )

            # Load the transformed user-movies matrix
            pivot_table = pd.read_pickle(
                 "artifacts/data_transformation/pivot_table.pkl"
            )

            # KNN Model
            model = NearestNeighbors(
                metric="cosine",
                algorithm="brute"
            )

            # Training the KNN with matrx
            model.fit(pivot_table.values)

            # Save the trained model
            pd.to_pickle(
                model,
                self.config.model_path
            )

            logging.info(
                f"Model saved successfully at {self.config.model_path}"
            )

            logging.info("Model Training completed successfully")

            return self.config.model_path


        except Exception as e:

            logging.error(
                f"Error occured during model training: {e}"
            )

            raise CustomException(e, sys)