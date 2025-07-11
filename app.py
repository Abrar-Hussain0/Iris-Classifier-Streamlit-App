import streamlit as st
import numpy as np
import pickle
from PIL import Image

# Page setup
st.set_page_config(page_title="Iris Classifier 🌸", layout="centered")

# Load the model
with open("iris_dataset.pkl", "rb") as f:
    model = pickle.load(f)

# Species mapping (according to LabelEncoder in training)
species = ["Iris-setosa", "Iris-versicolor", "Iris-virginica"]

images = {
    "Iris-setosa": "setosa.png",
    "Iris-versicolor": "versicolor.png",
    "Iris-virginica": "virginica.png"
}

descriptions = {
    "Iris-setosa": "🌼 *Iris-setosa* is a small, delicate flower with light-colored petals and broad sepals. It's the most distinct of the three species.",
    "Iris-versicolor": "💐 *Iris-versicolor* features medium-sized petals with hues of violet-blue. It lies between setosa and virginica in terms of size.",
    "Iris-virginica": "🌸 *Iris-virginica* is the largest and most vibrant among the species. It has long, pointed petals and thrives in wet conditions."
}

# Sidebar for inputs
with st.sidebar:
    st.header("🔬 Input Flower Measurements")
    sepal_length = st.slider("Sepal Length (cm)", 4.0, 8.0, 5.0)
    sepal_width = st.slider("Sepal Width (cm)", 2.0, 5.0, 3.0)
    petal_length = st.slider("Petal Length (cm)", 1.0, 7.0, 4.0)
    petal_width = st.slider("Petal Width (cm)", 0.1, 2.5, 1.0)

# Main Title
st.title("🌸 Iris Species Classifier")
st.markdown("### Predict the species of an Iris flower based on its features.")

# Prediction
if st.button("🔍 Predict"):
    features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(features)
    predicted_species = species[prediction[0]]

    # Confidence score
    proba = model.predict_proba(features)
    confidence = np.max(proba) * 100

    # Result display
    st.markdown(f"## 🌺 Predicted species: **{predicted_species}**")
    st.markdown(f"**🔎 Confidence:** {confidence:.2f}%")

    # Image & description
    image = Image.open(images[predicted_species])
    st.image(image, caption=predicted_species, use_container_width=True)
    st.info(descriptions[predicted_species])

# Footer
st.markdown("---")
st.markdown("Made with ❤️ by *Abrar Hussain* | Dataset from [UCI ML Repository](https://archive.ics.uci.edu/ml/datasets/iris)")
