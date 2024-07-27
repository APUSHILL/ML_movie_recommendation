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
