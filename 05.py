# Import the required libraries: Streamlit, NumPy, and Pillow (PIL).
import streamlit as st
import pickle
import numpy as np
from PIL import Image
import pandas as pd

# Set the page configuration of the app, including the page title, icon, and layout.
st.set_page_config(page_title="Timelytics", page_icon="📦", layout="wide")

# Display the title and captions for the app.
st.title("Timelytics: Optimize your supply chain with advanced forecasting techniques.")

st.caption(
    "Timelytics is an ensemble model that utilizes three powerful machine learning algorithms - XGBoost, Random Forests, and Support Vector Machines (SVM) - to accurately forecast Order to Delivery (OTD) times. By combining the strengths of these three algorithms, Timelytics provides a robust and reliable prediction of OTD times, helping businesses to optimize their supply chain operations."
)

st.caption(
    "With Timelytics, businesses can identify potential bottlenecks and delays in their supply chain and take proactive measures to address them, reducing lead times and improving delivery times. The model utilizes historical data on order processing times, production lead times, shipping times, and other relevant variables to generate accurate forecasts of OTD times. These forecasts can be used to optimize inventory management, improve customer service, and increase overall efficiency in the supply chain."
)

# Load the trained ensemble model from the saved pickle file.
modelfile = "KrunitMistry/voting_model.pkl"

# Caching the model for faster loading
@st.cache_resource
def load_model():
    with open(modelfile, "rb") as f:
        model = pickle.load(f)
    return model

voting_model = load_model()

# Define the function for the wait time predictor using the loaded model.
def waitime_predictor(
    purchase_dow,
    purchase_month,
    year,
    product_size_cm3,
    product_weight_g,
    geolocation_state_customer,
    geolocation_state_seller,
    distance,
):
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

# Define the input parameters using Streamlit's sidebar.
with st.sidebar:
    
    img = Image.open("KrunitMistry/supply_chain_optimisation.jpg")
    st.image(img)
    st.header("Input Parameters")
    purchase_dow = st.number_input(
        "Purchased Day of the Week", min_value=0, max_value=6, step=1, value=3
    )
    purchase_month = st.number_input(
        "Purchased Month", min_value=1, max_value=12, step=1, value=1
    )
    year = st.number_input("Purchased Year", value=2018)
    product_size_cm3 = st.number_input("Product Size in cm^3", value=9328)
    product_weight_g = st.number_input("Product Weight in grams", value=1800)
    geolocation_state_customer = st.number_input(
        "Geolocation State of the Customer", value=10
    )
    geolocation_state_seller = st.number_input(
        "Geolocation State of the Seller", value=20
    )
    distance = st.number_input("Distance", value=475.35)

# Define the submit button for the input parameters.
submit = st.button("Submit")

# Define the output container for the predicted wait time.
st.header("Output: Wait Time in Days")

# When the submit button is clicked, call the wait time predictor function and display the predicted wait time in the output container.
if submit:
    with st.spinner(text="This may take a moment..."):
        prediction = waitime_predictor(
            purchase_dow,
            purchase_month,
            year,
            product_size_cm3,
            product_weight_g,
            geolocation_state_customer,
            geolocation_state_seller,
            distance,
        )
        st.write(f"Predicted Wait Time: {prediction} days")

# Define a sample dataset for demonstration purposes.
data = {
    "Purchased Day of the Week": ["0", "3", "1"],
    "Purchased Month": ["6", "3", "1"],
    "Purchased Year": ["2018", "2017", "2018"],
    "Product Size in cm^3": ["37206.0", "63714", "54816"],
    "Product Weight in grams": ["16250.0", "7249", "9600"],
}
