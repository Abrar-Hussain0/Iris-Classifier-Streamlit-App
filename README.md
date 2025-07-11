# 🌸 Iris Species Classifier - Streamlit App

This is an interactive web application built with Streamlit that classifies the species of an Iris flower based on its sepal and petal measurements. It uses a Logistic Regression model trained on the classic Iris dataset.

---

## 🚀 Project Overview

The Iris Species Classifier predicts one of three species of the Iris flower:

- **Setosa**  
- **Versicolor**  
- **Virginica**

The app allows users to input sepal length, sepal width, petal length, and petal width using sliders, then displays the predicted species along with an image and description of the flower.

---

## 🧠 Model and Data

- The model is a Logistic Regression classifier trained on the Iris dataset.
- The dataset includes 150 samples with 4 features each.
- The target classes are encoded as integers and mapped back to species names.
- Model training and evaluation are done using scikit-learn.
- Achieved 100% accuracy on the test set.

---

## 🖥️ Demo & Usage

Try out the live app here:  
[Live Demo - Iris Species Classifier](https://iris-classifier-app-app-fp9hnuvcxxmpteq2yxwrsy.streamlit.app/)

---

### Run Locally

1. Clone this repository:
   ```bash
   git clone https://github.com/Abrar-Hussain0/Iris-Classifier-Streamlit-App.git
   cd Iris-Classifier-Streamlit-App

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   
3. Run the Streamlit app:
   ```bash
  streamlit run app.py

4. The app will open in your browser. Use the sliders to input flower features and click Predict to see the result.

---

## 📁 Project Structure

├── app.py # Streamlit app script <br>
├── iris_dataset.pkl # Serialized trained model<br>
├── iris_dataset.ipynb # Jupyter notebook with data preprocessing and model training<br>
├── requirements.txt # Required Python packages<br>
├── setosa.png # Image of Iris Setosa<br>
├── versicolor.png # Image of Iris Versicolor<br>
├── virginica.png # Image of Iris Virginica<br>
├── README.md # Project documentation<br>

---

## 🛠️ Technologies Used

Python<br>
Streamlit (for interactive UI)<br>
scikit-learn (for model training and prediction)<br>
Pandas & NumPy (for data handling)<br>
Pillow (for image display)<br>

---


## 📸 Screenshots


Sample UI with prediction and flower image

---


## 🙌 Acknowledgments

The classic Iris dataset from the UCI Machine Learning Repository.<br>
Streamlit for providing an easy-to-use web app framework.

---

## 📬 Contact

Feel free to reach out for questions or collaborations!

GitHub: Abrar-Hussain0
Email: abrarhussa

