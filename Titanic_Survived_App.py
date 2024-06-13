#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st
import joblib
import pandas as pd

# Load the trained model
model = joblib.load('logistic_regression_model.pkl')

# Define function to get user input
def get_user_input():
    pclass = st.sidebar.selectbox('Passenger Class', (1, 2, 3))
    age = st.sidebar.slider('Age', 0, 100, 30)
    sibsp = st.sidebar.slider('Number of Siblings/Spouses Aboard', 0, 8, 0)
    parch = st.sidebar.slider('Number of Parents/Children Aboard', 0, 6, 0)
    fare = st.sidebar.slider('Fare', 0, 513, 50)
    sex = st.sidebar.selectbox('Sex', ('male', 'female'))
    embarked = st.sidebar.selectbox('Port of Embarkation', ('C', 'Q', 'S'))

    # Create a dictionary to hold the input values
    user_data = {
        'Pclass': pclass,
        'Age': age,
        'SibSp': sibsp,
        'Parch': parch,
        'Fare': fare,
        'Sex_male': 1 if sex == 'male' else 0,
        'Embarked_Q': 1 if embarked == 'Q' else 0,
        'Embarked_S': 1 if embarked == 'S' else 0,
    }

    # Convert the dictionary into a DataFrame
    features = pd.DataFrame(user_data, index=[0])
    return features

# Set up the Streamlit app
st.title('Titanic Survival Prediction')
st.write("This app predicts if a passenger would survive the Titanic disaster.")

# Get user input
user_input = get_user_input()

# Display the user input
st.subheader('User Input:')
st.write(user_input)

# Make predictions using the trained model
prediction = model.predict(user_input)
prediction_proba = model.predict_proba(user_input)

# Display the prediction result
st.subheader('Prediction:')
st.write('Survived' if prediction[0] == 1 else 'Not Survived')

# Display the prediction probability
st.subheader('Prediction Probability:')
st.write(prediction_proba)

