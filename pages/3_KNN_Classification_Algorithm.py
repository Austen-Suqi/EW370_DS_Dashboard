import pandas as pd
import streamlit as st
from pathlib import Path

# 1. Setup Paths
ROOT_DIR = Path(__file__).parent.parent
DATA_DIR = ROOT_DIR / "pages"
KNN_IMG_DIR = ROOT_DIR / "pages" / "KNN_images"

# 2. Smart Data Loading
@st.cache_data
def load_data(file_name):
    path = DATA_DIR / file_name
    if path.exists():
        return pd.read_csv(path)
    return None

df = load_data('KNN_images/df_head.csv')
df_accuracies = load_data('knn_results.csv')

# title
st.title('K Nearest Neighbors')
st.header('Splitting data into training and test data')
st.write('When we are first building a model we only have a set amount of data. Therefore, we need to save some of that data for testing. In our example we will withold 30\% of the data for testing.')

if df is not None and df_accuracies is not None:
    st.write('Below you\'ll see the first five data points and their labels where zero through 2 represent Setosa, Versicolour, and Virginica respectively. You might wonder why we have a numerical label in addition to the name. That\'s because most models work better with numbers than words.')
    st.write(df.head())

    st.header('Let\'s train a KNN model!')
    # Use the actual length of your results file to prevent index errors
    max_n = len(df_accuracies)
    n = st.slider('Select a value for n', 1, max_n, 1)

    # Calculate accuracy
    acc = float(df_accuracies.iloc[n-1].iloc[0]) * 100
    st.write(f"**{acc:.2f}% accuracy**")

    # Dynamic Image Loading
    knn_img = KNN_IMG_DIR / f"knn_cm_{n}.png"
    if knn_img.exists():
        st.image(str(knn_img), caption=f'Figure 1: Confusion matrix (n={n})')
    else:
        st.error(f"Image for n={n} not found.")
else:
    st.error("Data files (CSVs) were not found. Please check your /pages folder.")
st.write('Figure 1: Confusion matrix for KNN model with n='+str(n))
