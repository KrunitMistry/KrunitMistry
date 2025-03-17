# Import required libraries
import streamlit as st
import pickle
import numpy as np
import pandas as pd
import joblib
import os
from PIL import Image

# Set the page configuration
st.set_page_config(page_title="Timelytics", page_icon="📦", layout="wide")

# Display the title and captions
st.title("Timelytics: Optimize your supply chain with advanced forecasting techniques.")

st.caption(
    "Timelytics is an ensemble model that utilizes three powerful machine learning algorithms - XGBoost, Random Forests, and Support Vector Machines (SVM) - to accurately forecast Order to Delivery (OTD) times. By combining the strengths of these three algorithms, Timelytics provides a robust and reliable prediction of OTD times, helping businesses to optimize their supply chain operations."
)

st.caption(
    "With Timelytics, businesses can identify potential bottlenecks and delays in their supply chain and take proactive measures to address them, reducing lead times and improving delivery times. The model utilizes historical data on order processing times, production lead times, shipping times, and other relevant variables to generate accurate forecasts of OTD times. These forecasts can be used to optimize inventory management, improve customer service, and increase overall efficiency in the supply chain."
)

# Define the model file path
modelfile = "voting_model.pkl"

# Load the trained model with caching for faster performance
@st.cache_resource
def load_model():
    if os.path.exists(modelfile):
        with open(modelfile, "rb") as f:
            return pickle.load(f)
    else:
        st.error(f"Model file not found: {modelfile}")
        return None

# Load the model
voting_model = load_model()

# Define the wait time predictor function
def wait_time_predictor(
    purchase_dow,
    purchase_month,
    year,
    product_size_cm3,
    product_weight_g,
    geolocation_state_customer,
    geolocation_state_seller,
    distance,
):
    if voting_model:
        prediction = voting_model.predict(
            np.array(
                [
                    [
                        purchase_dow,
                        purchase_month,
                        year,
                        product_size_cm3,
                        product_weight_g,
                        geolocation_state_customer,
                        geolocation_state_seller,
                        distance,
                    ]
                ]
            )
        )
        return round(prediction[0])
    else:
        return "Error: Model not loaded."

# Sidebar input parameters
with st.sidebar:
    img_path = "supply_chain_optimisation.jpg"
    if os.path.exists(img_path):
        img = Image.open(img_path)
        st.image(img)
    else:
        st.warning(f"Image file not found: {img_path}")

    st.header("Input Parameters")
    purchase_dow = st.number_input("Purchased Day of the Week", min_value=0, max_value=6, step=1, value=3)
    purchase_month = st.number_input("Purchased Month", min_value=1, max_value=12, step=1, value=1)
    year = st.number_input("Purchased Year", value=2018)
    product_size_cm3 = st.number_input("Product Size in cm³", value=9328)
    product_weight_g = st.number_input("Product Weight in grams", value=1800)
    geolocation_state_customer = st.number_input("Geolocation State of the Customer", value=10)
    geolocation_state_seller = st.number_input("Geolocation State of the Seller", value=20)
    distance = st.number_input("Distance", value=475.35)

# Submit button
submit = st.button("Submit")

# Output section
with st.container():
    st.header("Output: Wait Time in Days")

    if submit:
        with st.spinner("This may take a moment..."):
            prediction = wait_time_predictor(
                purchase_dow,
                purchase_month,
                year,
                product_size_cm3,
                product_weight_g,
                geolocation_state_customer,
                geolocation_state_seller,
                distance,
            )
            st.write(prediction)

# Define a sample dataset
data = {
    "Purchased Day of the Week": [0, 3, 1],
    "Purchased Month": [6, 3, 1],
    "Purchased Year": [2018, 2017, 2018],
    "Product Size in cm³": [37206.0, 63714, 54816],
    "Product Weight in grams": [16250.0, 7249, 9600],
    "Geolocation State Customer": [25, 25, 25],
    "Geolocation State Seller": [20, 7, 20],
    "Distance": [247.94, 250.35, 4.915],
}

# Create and display the DataFrame
df = pd.DataFrame(data)
st.header("Sample Dataset")
st.write(df)
