import streamlit as st
import pandas as pd

from src.recommender.components.recommendation import RecommendationEngine

# Page Config
st.set_page_config(
    page_title = "Movie Recommendation System",
    page_icon = "🎬",
    layout = "centered"
)

# Application title
st.title("🎬 Movie Recommendation System")
st.write(
    "Select a movie and get recommendations based on "
    "collaborative filtering."
)

# Load recommendation engine
@st.cache_resource
def load_recommendation_engine():

    return RecommendationEngine()

engine = load_recommendation_engine()

# Fetching available movie titles
movie_titles = engine.pivot_table.index.tolist()

# Movie selection
selected_movie = st.selectbox(
    "Select a movie",
    movie_titles
)

# Number of recommendations
number_of_recommendations = st.slider(
    "Number of recommendations",
    min_value=1,
    max_value=10,
    value=5
)

# Recommendation button
if st.button("Recommend Movies"):

    recommendations = engine.recommend_movies(
        selected_movie,
        number_of_recommendations
    )

    st.subheader("Recommended Movies")

    for i, recommendation in enumerate(recommendations, start=1):

        title = recommendation["title"]
        similarity = recommendation["similarity"]

        st.write(
            f"**{i})  {title}**"
        )

        st.caption(
            f"Similarity: {similarity:.2%}"
        )