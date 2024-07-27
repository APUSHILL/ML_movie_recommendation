import pickle
import streamlit as st
import requests
import pandas as pd

# Function to fetch movie posters from TMDB
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    data = requests.get(url).json()
    poster_path = data.get('poster_path')
    if poster_path:
        return f"https://image.tmdb.org/t/p/w500/{poster_path}"
    return ""

# Function to get movie recommendations
def recommend(movie):
    try:
        index = movies[movies['title'] == movie].index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        recommended_movie_names = []
        recommended_movie_posters = []
        for i in distances[1:6]:
            movie_id = movies.iloc[i[0]].movie_id
            recommended_movie_posters.append(fetch_poster(movie_id))
            recommended_movie_names.append(movies.iloc[i[0]].title)
        return recommended_movie_names, recommended_movie_posters
    except KeyError as e:
        st.write(f"KeyError: {e}")
    except Exception as e:
        st.write(f"Error: {e}")

# Streamlit app
st.header('Movie Recommender System')

# Load data
movies = pd.read_csv('/mount/src/ml_movie_recommendation/tmdb_5000_movies.csv')
similarity = pickle.load(open('/mount/src/ml_movie_recommendation/movies.pkl', 'rb'))

# Display the structure of the movies DataFrame
st.write("Movies DataFrame columns:")
st.write(movies.columns)

# Display the first few rows of the movies DataFrame
st.write("First few rows of the Movies DataFrame:")
st.write(movies.head())

# Display the shape of the similarity matrix
st.write("Shape of the similarity matrix:")
st.write(similarity.shape)

# Movie list
movie_list = movies['title'].values
selected_movie = st.selectbox("Type or select a movie from the dropdown", movie_list)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    if recommended_movie_names and recommended_movie_posters:
        cols = st.columns(5)
        for col, name, poster in zip(cols, recommended_movie_names, recommended_movie_posters):
            col.text(name)
            col.image(poster)


