from src.recommender.entity.config_entity import DataIngestionConfig

import yaml

class ConfigurationManager:

    def __init__(self):
        with open("config/config.yaml", "r") as file:
            self.config = yaml.safe_load(file)

    def get_data_ingestion_config(self):

        config = self.config["data_ingestion"]

        return DataIngestionConfig(

            root_dir=config["root_dir"],

            movies_path=config["local_data_file"]["movies"],

            ratings_path=config["local_data_file"]["ratings"],

            tags_path=config["local_data_file"]["tags"],

            links_path=config["local_data_file"]["links"]

        )   