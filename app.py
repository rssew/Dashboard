import streamlit as st
import numpy as np
import pandas as pd

sales_data = np.random.rand(100) * 1000

products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
sales = np.random.rand(5) * 1000
customers = np.random.randint(1, 100, size = 5)

df = pd.DataFrame({
  'Product': products,
  'Sales': sales,
  'Customers': customers
})

st.markdown('### Product Sales and Customer Data')
st.dataframe(df)

st.markdown('### Sales Over Time')
st.line_chart(sales_data)

st.markdown('### Cumulative Sales')
st.area_chart(sales_data)

st.markdown('### Sales by Product')
st.bar_chart(df[['Product', 'Sales']].set_index('Product'))

st.markdown('### Customer Engagement by Product')
st.scatter_chart(df[['Product', 'Customers']].set_index('Product'))
