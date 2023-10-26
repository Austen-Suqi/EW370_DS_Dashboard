import streamlit as st

with open('./pages/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)

st.image("./pages/WRC3.png")
st.title("Welcoome to the EW370 Data Science Dashboard!")
st.header("This dashboard will walk you through classification and clustering examples")