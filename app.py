import pickle
import streamlit as st
import pandas as pd
import os

# Function to recommend movies
def recommend(movie, movies, similarity):
    try:
        index = movies[movies['title'] == movie].index[0]
    except IndexError:
        st.error(f"Movie '{movie}' not found in the dataset.")
        return []

    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = [movies.iloc[i[0]].title for i in distances[1:6]]

    return recommended_movie_names

# Function to download files using gdown
def download_file_from_google_drive(file_id, dest_path):
    try:
        import gdown
        url = f'https://drive.google.com/uc?id={1gzYVPG0WorxjKUk-27T9nWYrzeF9d6R0}'
        gdown.download(url, dest_path, quiet=False)
    except ModuleNotFoundError:
        st.error("gdown module is not installed. Please install it by running `pip install gdown`.")
        st.stop()

# Streamlit app header
st.header('Movie Recommender System')

# Ensure model directory exists
os.makedirs('model', exist_ok=True)

# File paths
movie_list_path = 'movie_list.pkl'
similarity_path = 'similarity.pkl'

# Google Drive file IDs
movie_list_file_id = 'YOUR_MOVIE_LIST_FILE_ID'
similarity_file_id = 'YOUR_SIMILARITY_FILE_ID'

# Download movie_list.pkl if it doesn't exist
if not os.path.exists(movie_list_path):
    st.warning("Movie list file not found. Downloading it now...")
    download_file_from_google_drive(movie_list_file_id, movie_list_path)

# Download similarity.pkl if it doesn't exist
if not os.path.exists(similarity_path):
    st.warning("Similarity file not found. Downloading it now...")
    download_file_from_google_drive(similarity_file_id, similarity_path)

# Load movie list
try:
    movies_dict = pickle.load(open(movie_list_path, 'rb'))
    movies = pd.DataFrame(movies_dict)
except FileNotFoundError:
    st.error("Movie list file still not found after attempting download.")
    st.stop()

# Load similarity data
try:
    similarity = pickle.load(open(similarity_path, 'rb'))
except FileNotFoundError:
    st.error("Similarity file still not found after attempting download.")
    st.stop()

# Extract movie titles from the movies DataFrame
movie_list = movies['title'].values

# Select movie from dropdown
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

# Show recommendations when button is clicked
if st.button('Show Recommendation'):
    recommended_movie_names = recommend(selected_movie, movies, similarity)
    if recommended_movie_names:
        st.write("Recommended Movies:")
        for name in recommended_movie_names:
            st.text(name)
