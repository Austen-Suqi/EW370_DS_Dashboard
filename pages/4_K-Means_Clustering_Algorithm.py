import streamlit as st
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent
KMEANS_DIR = ROOT_DIR / "pages" / "Kmeans_images"

# Title for streamlit page
st.title('K-Means Clustering Algorithm')
st.header('Let\'s see if we can cluster the data into groups!')
st.write('For this experiment we will not split the data into training and testing data. We will also visualize the data in 2 dimensions using PCA as discussed in the Data Exploration page.')

# Header for creating the kmeans model
st.header('Creating the K-Means Model')
st.write('Select a number of clusters to use for the K-Means model.')
k = st.slider('Number of Clusters', min_value=1, max_value=7, value=3, step=1)

# Load Plot 1
p1 = KMEANS_DIR / f"kmeans_plot1_{k}.png"
if p1.exists():
    st.image(str(p1), caption=f'K-Means clustering with {k} clusters - all features')

# Load Plot 2
p2 = KMEANS_DIR / f"kmeans_plot2_{k}.png"
if p2.exists():
    st.image(str(p2), caption=f'K-Means clustering with {k} clusters - with PCA')
