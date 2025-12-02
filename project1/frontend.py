import streamlit as st
import requests

st.title("🌸 Iris Flower Prediction App")

# Input fields
sepal_length = st.number_input("Sepal Length (cm)", min_value=0.0, format="%.2f")
sepal_width = st.number_input("Sepal Width (cm)", min_value=0.0, format="%.2f")
petal_length = st.number_input("Petal Length (cm)", min_value=0.0, format="%.2f")
petal_width = st.number_input("Petal Width (cm)", min_value=0.0, format="%.2f")

API_URL = "http://127.0.0.1:8000/predict"

# Flower name mapping logic
flower_names = {
    0: "setosa",
    1: "versicolor",
    2: "virginica"
}

if st.button("Predict Flower Type"):
    payload = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width
    }

    try:
        response = requests.post(API_URL, json=payload)
        result = response.json()

        model_output = result["predicted_flower"]  # expecting 0, 1, or 2
        flower_name = flower_names[model_output]   # convert to flower name

        st.success(f"🌼 Predicted Flower: {flower_name}")

    except Exception as e:
        st.error("Error: Could not get prediction from FastAPI")
        st.write(e)
