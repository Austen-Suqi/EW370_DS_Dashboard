import streamlit as st
from pathlib import Path

# 1. Setup a robust path to the current folder
# This ensures the app always finds your images/data
BASE_DIR = Path(__file__).parent

# 2. Hero Image
# Using BASE_DIR / "pages" / "WRC3.png" makes it bulletproof
img_path = BASE_DIR / "pages" / "WRC3.png"

if img_path.exists():
    st.image(str(img_path))
else:
    # This prevents the app from crashing if the image is missing
    st.warning("Logo image not found in the pages folder.")

# 3. Content
st.title("Welcome to the EW370 Data Science Dashboard!")
st.header("This dashboard will walk you through classification and clustering examples")

# Optional: If you still want the style.css for extra tweaks (like font sizes)
# you can keep this, otherwise you can delete these 3 lines:
css_path = BASE_DIR / "pages" / "style.css"
if css_path.exists():
    st.markdown(f'<style>{css_path.read_text()}</style>', unsafe_allow_html=True)
