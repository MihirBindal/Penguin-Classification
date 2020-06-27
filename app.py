import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.svm import SVC

st.write("""
# Penguin Prediction App
This app predicts the penguin species based on the given inputs!
""")
st.sidebar.header('User Input Features')


def user_input_features():
    island = st.sidebar.selectbox('Island', ('Biscoe', 'Dream', 'Torgersen'))
    if island == "Biscoe":
        island_Biscoe = 1
        island_Dream = 0
        island_Torgersen = 0
    elif island == 'Dream':
        island_Biscoe = 0
        island_Dream = 1
        island_Torgersen = 0
    elif island == 'Torgersen':
        island_Biscoe = 0
        island_Dream = 0
        island_Torgersen = 1
    sex = st.sidebar.selectbox('Sex', ('male', 'female'))
    if sex == "male":
        sex_female = 0
        sex_male = 1
    elif sex == "female":
        sex_female = 1
        sex_male = 0
    bill_length_mm = st.sidebar.slider('Bill length (mm)', 32.1, 59.6, 43.9)
    bill_depth_mm = st.sidebar.slider('Bill depth (mm)', 13.1, 21.5, 17.2)
    flipper_length_mm = st.sidebar.slider('Flipper length (mm)', 172.0, 231.0, 201.0)
    body_mass_g = st.sidebar.slider('Body mass (g)', 2700.0, 6300.0, 4207.0)
    data = {'bill_length_mm': bill_length_mm,
            'bill_depth_mm': bill_depth_mm,
            'flipper_length_mm': flipper_length_mm,
            'body_mass_g': body_mass_g,
            'island_Biscoe': island_Biscoe,
            'island_Dream': island_Dream,
            'island_Torgersen': island_Torgersen,
            'sex_female': sex_female,
            'sex_male': sex_male}
    features = pd.DataFrame(data, index=[0])
    return features


input_df = user_input_features()
st.subheader('User Input features')
st.write(input_df)
load_clf = pickle.load(open(r'model.pkl', 'rb'))
prediction = load_clf.predict(input_df)
st.subheader('Prediction')
st.write("The species of penguin with these features is", prediction[0])
