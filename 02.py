# Import necessary libraries
import streamlit as st
import joblib  # or any other library you used for model saving

# Load the pre-trained model
model = joblib.load('your_model_path/model.pkl')

# Set up the Streamlit app title
st.title("Order to Delivery Time Prediction")

# Create input fields for user to enter order details
product_category = st.selectbox("Product Category", ["Electronics", "Clothing", "Groceries", "Books", "Other"])
customer_location = st.text_input("Customer Location (e.g., city/state)")
shipping_method = st.selectbox("Shipping Method", ["Standard", "Express", "Next Day"])

# Create a button to submit the input
if st.button("Predict Delivery Time"):
    # Prepare the input data for prediction
    input_data = [[product_category, customer_location, shipping_method]]
    
    # Make the prediction using the loaded model
    prediction = model.predict(input_data)

    # Show the prediction result to the user
    st.write(f"Predicted Delivery Time: {prediction[0]} hours")

# Run the app: Save this file as app.py and run the following command in your terminal
# streamlit run app.py