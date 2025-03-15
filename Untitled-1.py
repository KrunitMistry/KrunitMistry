import streamlit as st
import pandas as pd
import numpy as np 

# Input fields
a = st.text_input("Product Category:")
b = st.text_input("Customer Location:")
c = st.text_input("Shipping Method:")

if st.button("Predict Values"):
    # Placeholder for ML prediction logic (Replace this with actual model)
    pred = "Sample Prediction Output"  # Replace this with actual prediction
    st.write(f"This is your Prediction: {pred}")

# Load CSV data
try:
    data = pd.read_csv("Final.csv")
    st.write("### Dataset Preview:")
    st.write(data.head())  # Show only the first few rows
except FileNotFoundError:
    st.error("Error: 'Final.csv' not found. Please check the file path.")

# Generate random chart data
chart_data = pd.DataFrame(np.random.rand(20, 3), columns=["A", "B", "C"])

# Display bar chart
st.write("### Random Data Visualization")
st.bar_chart(chart_data)
