import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Set page config to wide mode
# st.set_page_config(layout="wide")

st.set_page_config(
    page_title="Dasherboard: Santa's Dashboard",
    page_icon="🎄",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.northpole.com/',
        'Report a bug': "https://www.northpole.com/",
        'About': "# Welcome to Santa's performance system. This is an *AWESOME* cool dashboard!"
    }
)


# Create a main container for the layout
main_container = st.container()

# Use the main container to create three columns
with main_container:
    # Create three columns
    logo_col, title_col, header_col = st.columns([1, 3, 3])

    # Place a container with the logo in the first column
    with logo_col:
        with st.container(border=True):
            st.image('/workspaces/dasherboard/reindeer.png')  # Logo image URL

    # Place a container with the title in the second column
    with title_col:
        with st.container(border=True):
            st.title('The DasherBoard')

    # Place a container with the header in the third column
    with header_col:
        with st.container(border=True):
            st.header("Santa's performance management dashboard 2018")


# Create a main container
main_container = st.container(border=True)

# Use the main container to create columns
with main_container:
    # Create 4 columns
    col1, col2, col3, col4 = st.columns(4)

    # Place a container and then a metric in each column
    with col1:
        with st.container(border=True):
            st.metric(label="Temperature", value="70 °F", delta="1.2 °F")

    with col2:
        with st.container(border=True):
            st.metric(label="Humidity", value="50%", delta="-3%")

    with col3:
        with st.container(border=True):
            st.metric(label="Wind Speed", value="15 mph", delta="Travis M", delta_color="off")
    with col4:
        with st.container(border=True):
            st.metric(label="Employee of Month", value="Travis M", delta="First Time Wiiner", delta_color="off")

# # KPIs at the top using columns
# kpi1, kpi2, kpi3 = st.columns(3)
# kpi1.metric(label="KPI: Prod P/D%", value="67")
# kpi2.metric(label="KPI: Days to Go", value="18")
# kpi3.metric(label="KPI: Gifts to Go", value="5K")
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

# MAP SECTION data frame for maps

# df3 = pd.DataFrame({
#     "Latitude": np.random.randn(1000) / 50 + 37.76,
#     "Longitude": np.random.randn(1000) / 50 + -122.4,
#     "Presents": np.random.randn(1000) * 100,
#     "Naughty_Nice_Index": np.random.rand(1000, 4).tolist(),
# })
        
# Creating the DataFrame
df3 = pd.DataFrame({
    "City": ["New York", "London", "Paris", "Tokyo", "Sydney", "Cape Town", "Moscow", "Rio de Janeiro", "Beijing", "Mumbai"],
    "Latitude": [40.7128, 51.5074, 48.8566, 35.6895, -33.8688, -33.9249, 55.7558, -22.9068, 39.9042, 19.0760],
    "Longitude": [-74.0060, -0.1278, 2.3522, 139.6917, 151.2093, 18.4241, 37.6173, -43.1729, 116.4074, 72.8777],
    "Presents": [1,2,3,4,5,6,7,8,9,10],  # Random number of presents
    "Naughty_Nice_Index": ['#de1a24', '#00ff00','#de1a24', '#00ff00','#de1a24', '#00ff00','#de1a24', '#00ff00','#de1a24', '#00ff00' ]
})

# st.map(df3,
# latitude='Latitude',
# longitude='Longitude',
# size='Presents',
# color='Naughty_Nice_Index'
# )

st.map(df3,
latitude='Latitude',
longitude='Longitude',
size='Presents',
color='Naughty_Nice_Index'

)


# Footer Section


# Create a container
container = st.container(border=True)

# Use the container to display the metric
with container:
    st.metric(label="Temperature", value="70 °F", delta="1.2 °F")
