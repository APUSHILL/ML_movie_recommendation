import os
import pickle
import streamlit as st
import pandas as pd

# Check current directory files
st.write("Current directory files:")
st.write(os.listdir('/mnt/data/'))

# Attempt to load the files
try:
    movies = pd.read_csv('/mnt/data/tmdb_5000_movies.csv')
    st.write("tmdb_5000_movies.csv loaded successfully")
except Exception as e:
    st.write(f"Error loading tmdb_5000_movies.csv: {e}")

try:
    similarity = pickle.load(open('/mnt/data/movies.pkl', 'rb'))
    st.write("movies.pkl loaded successfully")
except Exception as e:
    st.write(f"Error loading movies.pkl: {e}")
