import streamlit as st

st.title('Retail Business Dashboard')

st.header('Manager Input Section')

st.write('Please enter the monthly sales target and select the region.')



target = st.number_input('Enter Monthly Sales Target (in USD)')
