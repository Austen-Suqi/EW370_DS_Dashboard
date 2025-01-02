# Importing the required libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.decomposition import PCA
from sklearn.cluster import DBSCAN, KMeans
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import streamlit as st
from matplotlib.lines import Line2D

with open('./pages/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)

# Title for streamlit page
st.title('K-Means Clustering Algorithm')
st.header('Let\'s see if we can cluster the data into groups!')
st.write('For this experiment we will not split the data into training and testing data. We will also visualize the data in 2 dimensions using PCA as discussed in the Data Exploration page.')

# Header for creating the kmeans model
st.header('Creating the K-Means Model')
st.write('Select a number of clusters to use for the K-Means model.')
k = st.slider('Number of Clusters', min_value=1, max_value=7, value=3, step=1)

st.image(f'./pages/Kmeans_images/kmeans_plot1_{k}.png')
st.write('Figure 1: K-Means clustering with '+str(k)+' clusters - all features')
st.image(f'./pages/Kmeans_images/kmeans_plot2_{k}.png')
st.write('Figure 2: K-Means clustering with '+str(k)+' clusters - with PCA dimensionality reduction')