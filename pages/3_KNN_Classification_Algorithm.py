# Importing the required libraries
import pandas as pd
import streamlit as st

@st.cache_data
def load_data(file_path):
    return pd.read_csv(file_path)

df = load_data('./pages/KNN_images/df_head.csv')
df_accuracies = load_data('./pages/knn_results.csv')

@st.cache_resource
def load_format(file_path):
    with open(file_path) as f:
        return f.read()

f = load_format('./pages/style.css')
st.markdown(f'<style>{f}</style>',unsafe_allow_html=True)

# title
st.title('K Nearest Neighbors')
st.header('Splitting data into training and test data')
st.write('When we are first building a model we only have a set amount of data. Therefore, we need to save some of that data for testing. In our example we will withold 30\% of the data for testing.')

st.write('Below you\'ll see the first five data points and their labels where zero through 2 represent Setosa, Versicolour, and Virginica respectively. You might wonder why we have a numerical label in addition to the name. That\'s because most models work better with numbers than words.')
# read df.head from './pages/KNN_images/df_head.txt'
st.write(df.head())

# Train a KNN model
st.header('Let\'s train a KNN model!')
## Take an input from the user for n
n = st.slider('Select a value for n',1,105,1)

st.write(str(float(df_accuracies.iloc[n-1]*100))[:5]+'% accuracy')
st.image(f'./pages/KNN_images/knn_cm_{n}.png')
st.write('Figure 1: Confusion matrix for KNN model with n='+str(n))