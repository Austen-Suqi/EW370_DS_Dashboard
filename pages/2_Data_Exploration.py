# Importing the required libraries
import streamlit as st

with open('./pages/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)

st.title('Data Exploration')
st.header('Checking for correlations between our four variables')
st.write('''This plot shows every combination of our different 
         measurements (sepal length, sepal width, petal length, and petal width).
         We will call these the data **attributes**.''')
st.write('**Can you pick out which Iris type is easiest to distinguish from the other two?** (Answer question 1)')

st.image(f'./pages/data_exploration_images/plot1.png')

st.header('Can we simplify the view of our data?')
st.write('''Yes! There are methods to reduce dimensionality of data.
         How this works is not important to the course, but it will make
         it much easier to view our data! The below plot shows our data in two 
         dimensions (so instead of our four attributes we have two).''')

st.image(f'./pages/data_exploration_images/plot2.png')

st.write('Does this simplified plot still have a single Iris type that is easiest to identify?')