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

# import the iris dataset
iris = datasets.load_iris()
X = iris.data
Y = iris.target

# PCA function
pca = PCA(n_components=2, random_state=15)
pca.fit(X)
X_2D = pca.transform(X)

# Function to create kmeans plot
def kmeans_plot(kmeans, x, Y):
    label = []

    for i in range(len(X)):
        temp = ''
        cluster = kmeans.labels_[i]
        iris = Y[i]
        colors = 'rgbykmc'

        temp += colors[cluster]

        if iris == 0:
            temp += 'o'
        elif iris == 1:
            temp += 'x'
        else:
            temp += '^'

        label.append(temp)

    fig2, ax2 = plt.subplots()
    fig2.set_figheight(8)
    fig2.set_figwidth(8)

    for l in list(set(label)):
        ax2.plot([x[j][0] for j in range(len(x)) if label[j]==l],[x[j][1] for j in range(len(x)) if label[j]==l], l)

    ax2.set_title(f'Dimensionality Reduction')
    ax2.set_xlabel(f'New Attribute 1')
    ax2.set_ylabel(f'New Attribute 2')

    legend_elements = [Line2D([0], [0], marker='o', color='w', label='Iris-Setosa', markerfacecolor='k',markersize=10),
                    Line2D([0], [0], marker='X', color='w', label='Iris-Versicolour', markerfacecolor='k',markersize=10),
                    Line2D([0], [0], marker='^', color='w', label='Iris-Virginica', markerfacecolor='k',markersize=10)]

    ax2.legend(handles=legend_elements, loc='best')

    # Show the results without pca
    # Plot results
    fig1, ax1 = plt.subplots(3,2)
    fig1.set_figheight(15)
    fig1.set_figwidth(15)

    # Data Exploration
    ## Split X into four categories
    sepal_length = X[:,0]
    sepal_width = X[:,1]
    petal_length = X[:,2]
    petal_width = X[:,3]

    # Create combinations and labels 
    all= [sepal_length,sepal_width,petal_length,petal_width]
    label = ['Sepal Length','Sepal Width', 'Petal Length','Petal Width']
    combos = []
    labels = []
    for i in range(len(all)):
        for j in range(i+1,len(all)):
            combos.append((all[i],all[j]))
            labels.append((label[i],label[j]))

    for i in range(len(combos)):
        ax1=plt.subplot(321+int(i))
        x=combos[i][0]
        y=combos[i][1]
        xlabel=labels[i][0]
        ylabel=labels[i][1]
        for j in range(len(X)):
            cluster = kmeans.labels_[j]
            iris = Y[j]
            temp = ''
            temp += colors[cluster]
            if iris == 0:
                temp += 'o'
            elif iris == 1:
                temp += 'x'
            else:
                temp += '^'
            ax1.plot(x[j],y[j], temp)

        ax1.set_title(f'{xlabel} vs {ylabel}')
        ax1.set_xlabel(f'{xlabel} (cm)')
        ax1.set_ylabel(f'{ylabel} (cm)')
    
    ax2.legend(handles=legend_elements, loc='best')
                       
    return fig1, fig2

# Title for streamlit page
st.title('K-Means Clustering Algorithm')
st.header('Let\'s see if we can cluster the data into groups!')
st.write('For this experiment we will not split the data into training and testing data. We will also visualize the data in 2 dimensions using PCA as discussed in the Data Exploration page.')

# Header for creating the kmeans model
st.header('Creating the K-Means Model')
st.write('Select a number of clusters to use for the K-Means model.')
k = st.slider('Number of Clusters', min_value=1, max_value=7, value=3, step=1)

fig1, fig2 = kmeans_plot(KMeans(n_clusters=k, random_state=15,n_init='auto').fit(X), X_2D, Y)
st.pyplot(fig1)
st.pyplot(fig2)