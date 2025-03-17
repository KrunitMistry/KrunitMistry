# Import necessary libraries
import streamlit as st
import joblib
import pandas as pd

# Load your pre-trained model
model = joblib.load('voting_model.pkl')

# Function to predict delivery time
def predict_delivery_time(product_category, customer_location, shipping_method):
    # Create a DataFrame with user input for model prediction
    input_data = pd.DataFrame({
        'product_category': [product_category],
        'customer_location': [customer_location],
        'shipping_method': [shipping_method]
    })
    
    # Make prediction
    prediction = model.predict(input_data)
    return prediction[0]

# Streamlit user interface
st.title("Order Delivery Time Prediction")

# User inputs
product_category = st.selectbox("Select Product Category", ["Electronics", "Books", "Clothing", "Home Goods"])
customer_location = st.text_input("Enter Customer Location")
shipping_method = st.selectbox("Select Shipping Method", ["Standard", "Express"])

# When user presses the 'Predict' button
if st.button("Predict Delivery Time"):
    prediction = predict_delivery_time(product_category, customer_location, shipping_method)
    st.success(f"The predicted delivery time is: {prediction} hours")

# Footer
st.sidebar.header("About")
st.sidebar.text("This application predicts the delivery time based on your order details.")