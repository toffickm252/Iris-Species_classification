import streamlit as st
import joblib
import numpy as np

# Load the trained model (adjust path if needed)
# model = joblib.load('C:\\Users\\Surface\\OneDrive\\Documentos\\GitHub\\Iris-Species_classification\\models\\svm_model.pkl')
import os # Make sure os is imported
# Construct a relative path to the model file
model_path = os.path.join(os.path.dirname(__file__), '..', 'models', 'svm_model.pkl')
model = joblib.load(model_path)

st.title('Iris Flower Classification')

st.sidebar.header('Input Features')

# Note: Model is trained on only sepal length and width; using only those for prediction
sepal_length = st.sidebar.slider('Sepal Length (cm)', 4.0, 8.0, 5.4)
sepal_width = st.sidebar.slider('Sepal Width (cm)', 2.0, 4.5, 3.4)
# petal_length = st.sidebar.slider('Petal Length (cm)', 1.0, 7.0, 1.3)  # Commented out since model doesn't use it
# petal_width = st.sidebar.slider('Petal Width (cm)', 0.1, 2.5, 0.2)    # Commented out since model doesn't use it

if st.button('Predict'):
    # Use only sepal length and width (2 features)
    input_data = np.array([[sepal_length, sepal_width]])
    prediction = model.predict(input_data)
    
    # Map numerical prediction to Iris species names
    iris_species = {0: 'Setosa', 1: 'Versicolor', 2: 'Virginica'}
    predicted_species = iris_species[prediction[0]]
    
    st.success(f'The predicted Iris species is: **{predicted_species}**')