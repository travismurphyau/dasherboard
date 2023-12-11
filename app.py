import streamlit as st
import pandas as pd

# Load data from CSV file
data = pd.read_csv('santa_toy_data.csv')
data['Date'] = pd.to_datetime(data['Date'])  # Ensure 'Date' is in datetime format

# Calculate total production
total_production = data['Toys_Produced'].sum()

# Streamlit app layout
st.title('Santa Toy Production Dashboard')

# Display total production as a metric
st.metric(label="Total Toys Produced", value=f"{total_production:,}")

# Display the data as a table
st.write("Toy Production Data:")
st.dataframe(data)

# Create a line chart
st.line_chart(data.set_index('Date'))

