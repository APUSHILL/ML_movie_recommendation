import pickle
import streamlit as st
import pandas as pd


def recommend(movie):
    try:
        index = movies[movies['title'] == movie].index[0]
    except IndexError:
        st.error(f"Movie '{movie}' not found in the dataset.")
        return []

    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = [movies.iloc[i[0]].title for i in distances[1:6]]

    return recommended_movie_names


st.header('Movie Recommender System')

# Ensure the loaded movies data is a DataFrame
try:
    movies_dict = pickle.load(open('model/movie_list.pkl', 'rb'))
    movies = pd.DataFrame(movies_dict)
except FileNotFoundError:
    st.error("Movie list file not found.")
    st.stop()

# Load similarity data
try:
    similarity = pickle.load(open('model/similarity.pkl', 'rb'))
except FileNotFoundError:
    st.error("Similarity file not found.")
    st.stop()

# Extract movie titles from the movies DataFrame
movie_list = movies['title'].values

selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names = recommend(selected_movie)
    if recommended_movie_names:
        for name in recommended_movie_names:
            st.text(name)

