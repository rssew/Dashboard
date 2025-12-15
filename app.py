import streamlit as st
import time

st.title('Business Performance Dashboard')
st.write('Objective: To demonstrate the usage of columns, tabs, and dynamic containers in a business dashboard.')

col1, col2, col3 = st.columns(3)
with col1:
  st.header('Q1 2024')
  st.write('Revenue: $1.2M')
with col2:
  st.header('Q2 2024')
  st.write('Revenue: $1.5M')
with col3:
  st.header('Q3 2024')
  st.write('Revenue: $1.3M')

tab1, tab2, tab3 = st.tabs(['Sales Data', 'Customer Insights', 'Market Trends'])
with tab1:     
  st.write("Content for Sales Data")
  sales_data = {
        "Q1 2024": "$1.2M",
        "Q2 2024": "$1.5M",
        "Q3 2024": "$1.3M",
        "Q4 2024": "$1.6M"
  }
  for quarter, revenue in sales_data.items():
    st.write(f'{quarter}: {revenue}')

with tab2: 
  st.write("Content for Customer Insights")
  customer_feedback = [
        "Great service!",
        "Very satisfied with the product quality.",
        "Quick delivery and excellent support."
  ]
  for i in customer_feedback:
    st.write(f' - {i}')

with tab3:
  st.write('content for Market Trends')
  market_trends = {
        "Eco-friendly products": "Increasing demand",
        "Online shopping": "Continued growth",
        "Subscription services": "Rising popularity"
  }
  for item, trend in market_trends.items():
    st.write(f'{item}: {trend}')

with st.expander('More information'):
  st.write('Yap')
  st.write('Yap')

placeholder = st.empty()
for i in range(5):
  placeholder.write(f'Loading data...{20*i}% complete')
  time.sleep(1)
placeholder.write('Data loading complete')

business_insights = [
    "Revenue increased by 15% in Q1 2024.",
    "Customer satisfaction improved by 10%.",
    "Market trends show a growing demand for eco-friendly products."
]

# Display insights one by one with delay
for insight in business_insights:
    placeholder.write(insight)
    time.sleep(2)

# -------------------------------
# 6. Add Interactivity
# -------------------------------
st.subheader("Interactive Revenue Checker")
quarters = ["Q1 2024", "Q2 2024", "Q3 2024", "Q4 2024"]
selected_quarter = st.selectbox("Select a quarter:", quarters)

# Display revenue dynamically
st.write(f"Revenue for {selected_quarter}: {sales_data[selected_quarter]}")

# Bonus: Growth adjustment
growth = st.slider("Adjust growth percentage:", 0, 50, 10)
base_revenue = float(sales_data[selected_quarter].strip("$M"))
adjusted_revenue = base_revenue * (1 + growth / 100)
st.write(f"Adjusted Revenue for {selected_quarter}: ${adjusted_revenue:.2f}M")

# -------------------------------
# 7. Motivational Button
# -------------------------------
if st.button("Show Motivation"):
    st.success("Keep pushing for growth! 🚀")
