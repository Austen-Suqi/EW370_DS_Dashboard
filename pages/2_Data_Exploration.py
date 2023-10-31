# Importing the required libraries
from sklearn import datasets
from sklearn.decomposition import PCA
import streamlit as st
import matplotlib.pyplot as plt

with open('./pages/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)

# import the iris dataset
iris = datasets.load_iris()
X = iris.data
Y = iris.target

# Data Exploration
## Split X into four categories
sepal_length = X[:,0]
sepal_width = X[:,1]
petal_length = X[:,2]
petal_width = X[:,3]

# Create combinations and labels 
all= [sepal_length,sepal_width,petal_length,petal_width]
label = ['Sepal Length','Sepal Width', 'Petal Length','Petal Width']
combos = []
labels = []
for i in range(len(all)):
  for j in range(i+1,len(all)):
    combos.append((all[i],all[j]))
    labels.append((label[i],label[j]))

# Plot results
fig, ax = plt.subplots(3,2)
fig.set_figheight(15)
fig.set_figwidth(15)

for i in range(len(combos)):
  ax1=plt.subplot(321+int(i))
  x=combos[i][0]
  y=combos[i][1]
  xlabel=labels[i][0]
  ylabel=labels[i][1]
  ax1.plot([x[j] for j in range(len(sepal_length)) if Y[j]==0],[y[j] for j in range(len(sepal_width)) if Y[j]==0], 'ro',
          [x[j] for j in range(len(sepal_length)) if Y[j]==1],[y[j] for j in range(len(sepal_width)) if Y[j]==1], 'bx',
          [x[j] for j in range(len(sepal_length)) if Y[j]==2],[y[j] for j in range(len(sepal_width)) if Y[j]==2], 'g^')
  ax1.set_title(f'{xlabel} vs {ylabel}')
  ax1.set_xlabel(f'{xlabel} (cm)')
  ax1.set_ylabel(f'{ylabel} (cm)')


fig.legend(['Iris-Setosa','Iris-Versicolour','Iris-Virginica'])

st.title('Data Exploration')
st.header('Checking for correlations between our four variables')
st.write('''This plot shows every combination of our different 
         measurements (sepal length, sepal width, petal length, and petal width).
         We will call these the data **attributes**.''')
st.write('**Can you pick out which Iris type is easiest to distinguish from the other two?** (Answer question 1)')

st.pyplot(fig)

st.header('Can we simplify the view of our data?')
st.write('''Yes! There are methods to reduce dimensionality of data.
         How this works is not important to the course, but it will make
         it much easier to view our data! The below plot shows our data in two 
         dimensions (so instead of our four attributes we have two).''')

# Create PCA instance
pca = PCA(n_components=3)
pca.fit(X)
X_2D = pca.transform(X)

# Plot PCA results
fig, ax = plt.subplots()
fig.set_figheight(8)
fig.set_figwidth(8)

x = X_2D
y = Y

ax.plot([x[j][0] for j in range(len(x)) if Y[j]==0],[x[j][1] for j in range(len(x)) if Y[j]==0], 'ro',
          [x[j][0] for j in range(len(x)) if Y[j]==1],[x[j][1] for j in range(len(x)) if Y[j]==1], 'bx',
          [x[j][0] for j in range(len(x)) if Y[j]==2],[x[j][1] for j in range(len(x)) if Y[j]==2], 'g^')
ax.set_title(f'Dimensionality Reduction')
ax.set_xlabel(f'New Attribute 1')
ax.set_ylabel(f'New Attribute 2')


fig.legend(['Iris-Setosa','Iris-Versicolour','Iris-Virginica'])

st.pyplot(fig)

st.write('Does this simplified plot still have a single Iris type that is easiest to identify?')