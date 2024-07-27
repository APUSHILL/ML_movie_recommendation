import os
import streamlit as st

# Check current directory files
st.write("Current directory files:")
current_dir = os.getcwd()
st.write(f"Current working directory: {current_dir}")
st.write(os.listdir(current_dir))

# Check files in the parent directory
parent_dir = os.path.dirname(current_dir)
st.write(f"Parent directory: {parent_dir}")
st.write(os.listdir(parent_dir))

# Check files in the /mnt directory
mnt_dir = '/mnt'
if os.path.exists(mnt_dir):
    st.write(f"/mnt directory: {mnt_dir}")
    st.write(os.listdir(mnt_dir))
else:
    st.write(f"/mnt directory does not exist: {mnt_dir}")

# Check files in the /mnt/data directory
data_dir = '/mnt/data'
if os.path.exists(data_dir):
    st.write(f"/mnt/data directory: {data_dir}")
    st.write(os.listdir(data_dir))
else:
    st.write(f"/mnt/data directory does not exist: {data_dir}")
    import pickle
import streamlit as st
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters


st.header('Movie Recommender System')
movies = pickle.load(open('model/movie_list.pkl','rb'))
similarity = pickle.load(open('model/similarity.pkl','rb'))

movie_list = movies_list['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.beta_columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
