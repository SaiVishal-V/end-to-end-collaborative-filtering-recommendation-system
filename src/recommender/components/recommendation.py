import sys 
import pandas as pd

from src.recommender.exception import CustomException
from src.recommender.logger import logging


class RecommendationEngine:

    def __init__(self):

        self.model_path = "artifacts/model_trainer/model.pkl"
        self.pivot_table_path = "artifacts/data_transformation/pivot_table.pkl"

        self.model = pd.read_pickle(self.model_path)
        self.pivot_table = pd.read_pickle(self.pivot_table_path)

        logging.info("Recommendation engine initialized successfully.")

    def recommend_movies(self, movie_title, n_recommendations = 5):
        try:

            logging.info(
                f"Generating recommendations for: {movie_title}"
            )

            # To confirm if the requested movie exists
            if movie_title not in self.pivot_table.index:

                raise ValueError(
                    f"Movie '{movie_title}' was not found in the dataset"
                )

            # Row number of the selected movie
            movie_index = self.pivot_table.index.get_loc(movie_title)

            # Get the movie's rating vector
            movie_vector = self.pivot_table.iloc[
                movie_index
            ].values.reshape(1, -1)

            # Find similar movies
            distances, indices = self.model.kneighbors(
                movie_vector,
                n_neighbors = n_recommendations + 1
            )

            recommendations = []

            for distance, index in zip(distances[0], indices[0]):

                if index == movie_index:
                    continue

                recommendations.append({
                    "title": self.pivot_table.index[index],
                    "similarity": float(1 - distance)
                })

                if len(recommendations) == n_recommendations:
                    break

            logging.info(
                f"Generated {len(recommendations)} recommendations"
            )

            return recommendations

        except Exception as e:
            logging.error(
                f"Error occured while generating recommendations: {e}"
            )
            raise CustomException(e, sys)