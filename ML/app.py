import streamlit as st
import pickle
import pandas as pd

# Load the trained model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Function to make predictions
def predict_class(flight_number, date, booster_version, payload_mass, orbit,
                  launch_site, outcome, flights, grid_fins, reused, legs,
                  landing_pad, block, reused_count, serial, longitude, latitude):
    # Prepare input data for the model (ensure it matches the training data shape)
    input_data = pd.DataFrame({
        'FlightNumber': [flight_number],
        'Date': [date],
        'BoosterVersion': [booster_version],
        'PayloadMass': [payload_mass],
        'Orbit': [orbit],
        'LaunchSite': [launch_site],
        'Outcome': [outcome],
        'Flights': [flights],
        'GridFins': [grid_fins],
        'Reused': [reused],
        'Legs': [legs],
        'LandingPad': [landing_pad],
        'Block': [block],
        'ReusedCount': [reused_count],
        'Serial': [serial],
        'Longitude': [longitude],
        'Latitude': [latitude]
    })
    
    # Make predictions
    prediction = model.predict(input_data)
    return prediction[0]

# Streamlit UI components
st.title("Falcon 9 Landing Prediction")

# User input fields
flight_number = st.number_input("Flight Number", min_value=1, max_value=90)
date = st.date_input("Date")
booster_version = st.text_input("Booster Version")
payload_mass = st.number_input("Payload Mass (kg)", min_value=0)
orbit = st.text_input("Orbit")
launch_site = st.text_input("Launch Site")
outcome = st.text_input("Outcome")
flights = st.number_input("Flights")
grid_fins = st.selectbox("Grid Fins", options=[0, 1])
reused = st.selectbox("Reused", options=[0, 1])
legs = st.selectbox("Legs", options=[0, 1])
landing_pad = st.text_input("Landing Pad")
block = st.number_input("Block", min_value=0)
reused_count = st.number_input("Reused Count", min_value=0)
serial = st.text_input("Serial")
longitude = st.number_input("Longitude")
latitude = st.number_input("Latitude")

# Prediction button
if st.button("Predict"):
    result = predict_class(flight_number, date, booster_version, payload_mass, orbit,
                           launch_site, outcome, flights, grid_fins, reused, legs,
                           landing_pad, block, reused_count, serial, longitude, latitude)
    st.success(f'The predicted class is: {result}')