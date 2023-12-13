import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Set page config to wide mode
st.set_page_config(layout="wide")

# Title and header
st.title('The DasherBoard')
st.header("Santa's performance management dashboard 2018")

# KPIs at the top using columns
kpi1, kpi2, kpi3 = st.columns(3)
kpi1.metric(label="KPI: Prod P/D%", value="67")
kpi2.metric(label="KPI: Days to Go", value="18")
kpi3.metric(label="KPI: Gifts to Go", value="5K")

# Sample data for the reindeer performance
reindeer_performance_data = {
    'Reindeer': ['Dasher', 'Dancer', 'Rudolph'],
    'Speed': [5.9, 4.5, 4.0],
    'Agility': [7.0, 9.5, 6.5],
    'Luminosity': [100, 70, 60],
}

# Convert dictionary to DataFrame
reindeer_df = pd.DataFrame(reindeer_performance_data)

# Reindeer performance sections using columns within container
with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("Fastest Reindeer")
        fig, ax = plt.subplots()
        ax.barh(reindeer_df['Reindeer'], reindeer_df['Speed'], color='skyblue')
        ax.set_xlabel('Speed')
        st.pyplot(fig)
    with col2:
        st.subheader("Most Agile")
        fig, ax = plt.subplots()
        ax.barh(reindeer_df['Reindeer'], reindeer_df['Agility'], color='lightgreen')
        ax.set_xlabel('Agility')
        st.pyplot(fig)
    with col3:
        st.subheader("Most Luminous")
        fig, ax = plt.subplots()
        ax.barh(reindeer_df['Reindeer'], reindeer_df['Luminosity'], color='lightcoral')
        ax.set_xlabel('Luminosity')
        st.pyplot(fig)

# Footer or additional sections can be added here
# ...

# Make sure to save this script as a .py file and run it using the Streamlit command
# To run: streamlit run your_script_name.py
