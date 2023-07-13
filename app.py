import streamlit as st
import pandas as pd
import numpy as np
import tensorflow
from tensorflow import keras
from keras.models import load_model
import folium


st.title('Food Delivery Time Prediction app')

a = st.text_input('Age of Delivery Partner:', 0.0)
b = st.text_input('Ratings of Previous Deliveries:', 0.0)
lat1 = st.text_input('Restaurant Latitude:', 0.0)
lon1 = st.text_input('Restaurant Longitude:', 0.0)
lat2 = st.text_input('Delivery Location Latitude:', 0.0)
lon2 = st.text_input('Delivery Location Longitude:', 0.0)

def calculate_distance(lat1, lon1, lat2, lon2):
    radius = 6371 

    lat1_rad = np.radians(float(lat1))
    lon1_rad = np.radians(float(lon1))
    lat2_rad = np.radians(float(lat2))
    lon2_rad = np.radians(float(lon2))

    delta_lat = lat2_rad - lat1_rad
    delta_lon = lon2_rad - lon1_rad

    a = np.sin(delta_lat / 2) ** 2 + np.cos(lat1_rad) * np.cos(lat2_rad) * np.sin(delta_lon / 2) ** 2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    distance = radius * c

    return distance

c = calculate_distance(lat1, lon1, lat2, lon2)
submit_button = st.button('Submit')

if submit_button:
    features = np.array([[float(a), float(b), float(c)]])
    model = tensorflow.keras.models.load_model('E:\Github Projects\Delivery time\Model\Model_train.h5', compile=False)
    model.compile(optimizer='adam', loss='mean_squared_error')
    prediction = model.predict(features)
    st.text(f"Predicted Delivery Time: {prediction[0][0]}")

    data = pd.DataFrame({
        'latitude': [float(lat1), float(lat2)],
        'longitude': [float(lon1), float(lon2)]
    })

    st.map(data=data)




