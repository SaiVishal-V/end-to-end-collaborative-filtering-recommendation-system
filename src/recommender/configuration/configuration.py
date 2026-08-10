from src.recommender.entity.config_entity import (
    DataIngestionConfig,
    DataValidationConfig, 
    DataTransformationConfig,
    ModelTrainerConfig
)

import yaml

class ConfigurationManager:

    def __init__(self):
        with open("config/config.yaml", "r") as file:
            self.config = yaml.safe_load(file)

    def get_data_ingestion_config(self):

        config = self.config["data_ingestion"] #Self.config stores the entire configuration dictionary after reading the YAML file

        return DataIngestionConfig(

            root_dir=config["root_dir"],

            movies_path=config["local_data_file"]["movies"],

            ratings_path=config["local_data_file"]["ratings"],

            tags_path=config["local_data_file"]["tags"],

            links_path=config["local_data_file"]["links"]

        )  

    def get_data_validation_config(self):

        validation_config = self.config["data_validation"]

        return DataValidationConfig(

            root_dir=validation_config["root_dir"],

            status_file=validation_config["status_file"],

            data_ingestion_dir=validation_config["data_ingestion_dir"],

            schema_file=validation_config["schema_file"]

    )

    def get_data_transformation_config(self):

        transformation_config = self.config["data_transformation"]

        return DataTransformationConfig(

            root_dir = transformation_config["root_dir"],
            merged_data_path = transformation_config["merged_data_path"],
            pivot_table_path = transformation_config["pivot_table_path"]
        )

    def get_model_trainer_config(self):

        model_trainer_config = self.config["model_trainer"]

        return ModelTrainerConfig(
            root_dir= model_trainer_config["root_dir"],
            model_path=model_trainer_config["model_path"]
        )