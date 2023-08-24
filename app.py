import streamlit as st
import pandas as pd
import numpy as np
import pickle
import sklearn

pickle_in = open('logisticregression.pkl','rb')
model = pickle.load(pickle_in)

st.title("Diabetes predictions for pregnant woman")
st.write("Developed by Ornella")

### Inputing Variables

longitude       = st.number_input("Longitude")   
latitude         = st.number_input("Latitude")
housing_median_age = st.number_input("Housing Median Age")
total_rooms         = st.number_input("Total rooms")
total_bedrooms      = st.number_input("Total bedrooms")
population          = st.number_input("Population")
households         = st.number_input("HouseHolds")
median_income       = st.number_input("Median Income")
ocean_proximity  = st.number_input("Ocean Proximity")

button = st.button("Predict")

### make predictions
if button:
    predictions = model.predict([[longitude,latitude,housing_median_age,total_rooms,total_bedrooms,population,households,median_income,ocean_proximity]]) 
if predictions == 0:
    st.write("Oooooooooooooops")
else:
    st.write("Oooooooooooooops")