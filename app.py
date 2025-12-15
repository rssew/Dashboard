import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title('Welcome to Streamlit')
st.write('Hello! Streamlit!')
st.write(12345)
st.write({'Name': 'Alice', 'Age': 23})
st.write('**Bold Text** and *Italic Script*')

st.header('Section 1: Introduction')
age = st.number_input('Enter your age:',
                      min_value = 0,
                      max_value = 150,
                      value = 25)

st.write(f'Your age is {age}')

option = st.selectbox('Choose your favorite color:', 
                       ['Red', 'Yellow', 'Blue'])
st.write(f'You favorite color is {option}')

if st.button('Click me'):
  st.write('Clicked')
