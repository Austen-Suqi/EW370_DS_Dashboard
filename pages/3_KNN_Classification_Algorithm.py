# Importing the required libraries
import pandas as pd
import streamlit as st

with open('./pages/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)

# title
st.title('K Nearest Neighbors')
st.header('Splitting data into training and test data')
st.write('When we are first building a model we only have a set amount of data. Therefore, we need to save some of that data for testing. In our example we will withold 30\% of the data for testing.')

st.write('Below you\'ll see the first five data points and their labels where zero through 2 represent Setosa, Versicolour, and Virginica respectively. You might wonder why we have a numerical label in addition to the name. That\'s because most models work better with numbers than words.')
# read df.head from './pages/KNN_images/df_head.txt'
with open('./pages/KNN_images/df_head.txt') as f:
    df = pd.read_csv(f)
st.write(df.head())

# Train a KNN model
st.header('Let\'s train a KNN model!')
## Take an input from the user for n
n = st.slider('Select a value for n',1,105,1)

df_accuracies = pd.read_csv('./pages/knn_results.csv')
results_accuracy = df_accuracies.iloc[n-1]
st.write(str(float(results_accuracy*100))[:5]+'% accuracy')
st.image(f'./pages/KNN_images/knn_cm_{n}.png')
st.write('Figure 1: Confusion matrix for KNN model with n='+str(n))