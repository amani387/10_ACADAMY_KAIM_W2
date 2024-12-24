import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st

# Load the preprocessed dataset
data = pd.read_csv('user_engagement_experience.csv')  # Replace with your actual dataset

# Identify relevant features for engagement and experience
engagement_features = ['feature1', 'feature2']  # Replace with actual engagement features
experience_features = ['feature3', 'feature4']  # Replace with actual experience features

# Define centroids from clustering analysis
less_engaged_centroid = [0.5, 0.6]  # Replace with actual values from clustering
worst_experience_centroid = [0.7, 0.8]  # Replace with actual values from clustering

# Compute Engagement and Experience Scores
def euclidean_distance(point, centroid):
    return np.sqrt(np.sum((point - centroid) ** 2))

data['engagement_score'] = data[engagement_features].apply(
    lambda row: euclidean_distance(row.values, less_engaged_centroid), axis=1
)
data['experience_score'] = data[experience_features].apply(
    lambda row: euclidean_distance(row.values, worst_experience_centroid), axis=1
)

# Compute Satisfaction Score
data['satisfaction_score'] = (data['engagement_score'] + data['experience_score']) / 2

# Streamlit App
st.set_page_config(page_title="User Data Dashboard", layout="wide")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to", 
    ["User Overview Analysis", "User Engagement Analysis", "Experience Analysis", "Satisfaction Analysis"]
)

# Dashboard Pages
if page == "User Overview Analysis":
    st.title("User Overview Analysis")
    st.plotly_chart(px.histogram(data, x='satisfaction_score', title='Satisfaction Score Distribution'), use_container_width=True)

elif page == "User Engagement Analysis":
    st.title("User Engagement Analysis")
    st.plotly_chart(px.scatter(data, x='feature1', y='feature2', color='engagement_score', title='Engagement Analysis'), use_container_width=True)

elif page == "Experience Analysis":
    st.title("Experience Analysis")
    st.plotly_chart(px.scatter(data, x='feature3', y='feature4', color='experience_score', title='Experience Analysis'), use_container_width=True)

elif page == "Satisfaction Analysis":
    st.title("Satisfaction Analysis")
    st.plotly_chart(px.scatter(data, x='engagement_score', y='experience_score', color='satisfaction_score', title='Satisfaction Analysis'), use_container_width=True)

# Deployment Ready
st.sidebar.info("Use the sidebar to navigate between different analyses.")
