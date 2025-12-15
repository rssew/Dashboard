import streamlit as st

st.title('Retail Business Dashboard')

st.header('Manager Input Section')

st.write('Please enter the monthly sales target and select the region.')

target = st.number_input('Enter Monthly Sales Target (in USD)', value = 0)

region = st.selectbox('Select Region:', ['North', 'South', 'West', 'East'])

if st.button('Submit'):
  st.write(f'Monthly Target Sales: {target}\nRegion: {region}')
  
