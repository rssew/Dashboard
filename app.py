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
