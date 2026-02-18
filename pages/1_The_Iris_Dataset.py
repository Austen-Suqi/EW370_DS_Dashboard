from pathlib import Path

# Setup Path (Since this file is IN /pages, parent is the root)
ROOT_DIR = Path(__file__).parent.parent
IMAGE_PATH = ROOT_DIR / "pages" / "iris-machinelearning.png"

f = load_format('./pages/style.css')
st.markdown(f'<style>{f}</style>',unsafe_allow_html=True)

st.title('Uh, so... What is this "Iris" Dataset?')
if IMAGE_PATH.exists():
    st.image(str(IMAGE_PATH))
else:
    st.error(f"Could not find image at {IMAGE_PATH}")
st.write('This data set is called the Iris dataset. Why? Because it has data about 3 different types of Iris plants. It is a balanced dataset (which is important for many data science and machine learning algorithms) because it has 50 data points for each type of Iris (150 total data points).')
st.write('Conveniently, somebody had the below picture online that shows the three types of Iris plants we will be using. Notice that it labels the petals and sepals, of which we will be using the length and width of each to see if that is enough information to properly label the type of Iris.')
st.image('./pages/iris-machinelearning.png')
