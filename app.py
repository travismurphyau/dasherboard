import streamlit as st
import pandas as pd
import numpy as np

# Generate a time series for the dates
dates = pd.date_range(start="2023-01-01", end="2023-12-31", freq='D')

# Simulate toy production counts
production_counts = np.random.randint(100, 1000, size=len(dates))

# Create a DataFrame
data = pd.DataFrame({'Date': dates, 'Toys_Produced': production_counts})

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
