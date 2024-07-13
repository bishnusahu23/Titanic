

#bmi=weight in kgs/height2 in meters

import streamlit as st
import pandas as pd
import numpy as np

import streamlit as st

st.title('Welcome to the BMI calculator')


weight=st.number_input('Enter your weight (in kgs):')
status= st.radio('Select your height format:',('cms','meters','feet'))

if (status== 'cms'):
    height= st.number_input('Centimeters')
    try:
        bmi= weight/((height/100)**2)
    except:
        st.text('Enter height:')
elif(status== 'meters'):
    height=st.number_input('Meters')
    try:
        bmi=weight/(height**2)
    except:
        st.text('Enter height')
        
else:
    height = st.number_input('Feet')
    try:
        bmi = weight / (((height/3.28))**2)
    except:
        st.text("Enter height")

if (st.button('Caluculate BMI')):
    st.write(f'Your BMI is {bmi}')
    if(bmi < 16):
        st.error("You are Extremely Underweight")
    elif(bmi >= 16 and bmi < 18.5):
        st.warning("You are Underweight")
    elif(bmi >= 18.5 and bmi < 25):
        st.success("Healthy")
    elif(bmi >= 25 and bmi < 30):
        st.warning("Overweight")
    elif(bmi >= 30):
        st.error("Extremely Overweight")

























