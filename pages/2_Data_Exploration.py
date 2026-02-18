import streamlit as st
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent
IMG_DIR = ROOT_DIR / "pages" / "data_exploration_images"

st.title('Data Exploration')
st.header('Checking for correlations between our four variables')
st.write('''This plot shows every combination of our different 
         measurements (sepal length, sepal width, petal length, and petal width).
         We will call these the data **attributes**.''')
st.write('**Can you pick out which Iris type is easiest to distinguish from the other two?** (Answer question 1)')

# Robust Plot 1 Loading
plot1 = IMG_DIR / "plot1.png"
if plot1.exists():
    st.image(str(plot1))
else:
    st.warning("Plot 1 image missing.")

st.header('Can we simplify the view of our data?')
st.write('''Yes! There are methods to reduce dimensionality of data.
         How this works is not important to the course, but it will make
         it much easier to view our data! The below plot shows our data in two 
         dimensions (so instead of our four attributes we have two).''')

# Robust Plot 2 Loading
plot2 = IMG_DIR / "plot2.png"
if plot2.exists():
    st.image(str(plot2))

st.write('Does this simplified plot still have a single Iris type that is easiest to identify?')
