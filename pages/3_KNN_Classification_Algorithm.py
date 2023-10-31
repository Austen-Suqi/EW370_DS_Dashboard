# Importing the required libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import streamlit as st

with open('./pages/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)
    
# Functions to train knn and get predictions
def train_knn(n, X_train, y_train):
  knn = KNeighborsClassifier(n_neighbors=n)
  knn.fit(X_train, y_train)
  return knn

def results_knn(knn, X_test, y_test):
  y_pred = knn.predict(X_test)
  cm = confusion_matrix(y_test, y_pred)
  cm_display = ConfusionMatrixDisplay(cm, display_labels=['Iris-Setosa','Iris-Versicolour','Iris-Virginica']).plot(cmap=plt.cm.Blues)

  return y_pred, accuracy_score(y_test,y_pred), cm

# import the iris dataset
iris = datasets.load_iris()
X = iris.data
Y = iris.target

# splitting X and y into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, Y, test_size=0.3, random_state=15)

# title
st.title('K Nearest Neighbors')
st.header('Splitting data into training and test data')
st.write('When we are first building a model we only have a set amount of data. Therefore, we need to save some of that data for testing. In our example we will withold 30\% of the data for testing.')

# put X_train and y_train in a dataframe to display
df = pd.DataFrame(X_train, columns = ['Sepal Length','Sepal Width', 'Petal Length', 'Petal Width'])
df = df.assign(Iris_label=y_train)
## Get iris types
iris_types = []
for y in y_train:
    if y == 0:
      iris_types.append('Setosa')
    elif y == 1:
      iris_types.append('Versicolour')
    else:
      iris_types.append('Virginica')
df = df.assign(iris_type=iris_types)

df.columns = ['Sepal Length','Sepal Width', 'Petal Length', 'Petal Width', 'Iris Label', 'Iris Type']

st.write('Below you\'ll see the first five data points and their labels where zero through 2 represent Setosa, Versicolour, and Virginica respectively. You might wonder why we have a numerical label in addition to the name. That\'s because most models work better with numbers than words.')
st.write(df.head())

# Train a KNN model
st.header('Let\'s train a KNN model!')
## Take an input from the user for n
n = st.slider('Select a value for n',1,105,1)
## Create model and find results
knn = train_knn(n,X_train,y_train)
results, results_accuracy, cm = results_knn(knn,X_test,y_test)

st.write(str(float(results_accuracy*100))[:5]+'% accuracy')
st.image(f'./pages/KNN_images/knn_cm_{n}.png')
st.write('Figure 1: Confusion matrix for KNN model with n='+str(n))