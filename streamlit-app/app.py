import streamlit as st
import numpy as np
import pickle
import os

# -----------------------------
# Load Model
# -----------------------------
def load_model():
    base_dir = os.path.dirname(__file__)
    model_file = os.path.join(base_dir, "..", "models", "svm_model.pkl")

    try:
        with open(model_file, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        st.error("Model file not found. Check the folder structure.")
        st.stop()
    except Exception as e:
        st.error(f"Error loading model: {e}")
        st.stop()


model = load_model()

# -----------------------------
# UI Layout
# -----------------------------
st.title("Iris Flower Classification")

st.sidebar.header("Input Features")
sepal_length = st.sidebar.slider("Sepal Length (cm)", 4.0, 8.0, 5.4)
sepal_width = st.sidebar.slider("Sepal Width (cm)", 2.0, 4.5, 3.4)

# -----------------------------
# Prediction Logic
# -----------------------------
def predict_species(length, width):
    data = np.array([[length, width]])
    prediction = model.predict(data)[0]

    species_map = {
        0: "Setosa",
        1: "Versicolor",
        2: "Virginica"
    }
    return species_map.get(prediction, "Unknown")


if st.button("Predict"):
    species = predict_species(sepal_length, sepal_width)
    st.success(f"Predicted species: **{species}**")
