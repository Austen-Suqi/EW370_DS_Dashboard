import streamlit as st

@st.cache_resource
def load_format(file_path):
    with open(file_path) as f:
        return f.read()

f = load_format('./pages/style.css')
st.markdown(f'<style>{f}</style>',unsafe_allow_html=True)

st.image("./pages/WRC3.png")
st.title("Welcoome to the EW370 Data Science Dashboard!")
st.header("This dashboard will walk you through classification and clustering examples")