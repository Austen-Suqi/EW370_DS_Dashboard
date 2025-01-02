import streamlit as st

@st.cache_resource
def load_format(file_path):
    with open(file_path) as f:
        return f.read()

f = load_format('./pages/style.css')
st.markdown(f'<style>{f}</style>',unsafe_allow_html=True)

st.title('Uh, so... What is this "Iris" Dataset?')
st.write('This data set is called the Iris dataset. Why? Because it has data about 3 different types of Iris plants. It is a balanced dataset (which is important for many data science and machine learning algorithms) because it has 50 data points for each type of Iris (150 total data points).')
st.write('Conveniently, somebody had the below picture online that shows the three types of Iris plants we will be using. Notice that it labels the petals and sepals, of which we will be using the length and width of each to see if that is enough information to properly label the type of Iris.')
st.image('./pages/iris-machinelearning.png')