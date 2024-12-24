import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sqlalchemy import create_engine

# Load the preprocessed dataset
data = pd.read_csv('/data/cleaned_data.csv')  # Replace with your actual dataset

# Identify relevant features for engagement and experience
engagement_features = ['feature1', 'feature2']  # Replace with actual engagement features
experience_features = ['feature3', 'feature4']  # Replace with actual experience features

# Perform KMeans clustering to find centroids
kmeans_engagement = KMeans(n_clusters=3, random_state=42)
engagement_clusters = kmeans_engagement.fit(data[engagement_features])
less_engaged_centroid = kmeans_engagement.cluster_centers_[0]  # Adjust index based on analysis

kmeans_experience = KMeans(n_clusters=3, random_state=42)
experience_clusters = kmeans_experience.fit(data[experience_features])
worst_experience_centroid = kmeans_experience.cluster_centers_[0]  # Adjust index based on analysis

# Task 4.1: Compute Engagement and Experience Scores
def euclidean_distance(point, centroid):
    return np.sqrt(np.sum((point - centroid) ** 2))

data['engagement_score'] = data[engagement_features].apply(
    lambda row: euclidean_distance(row.values, less_engaged_centroid), axis=1
)
data['experience_score'] = data[experience_features].apply(
    lambda row: euclidean_distance(row.values, worst_experience_centroid), axis=1
)

# Task 4.2: Compute Satisfaction Score
data['satisfaction_score'] = (data['engagement_score'] + data['experience_score']) / 2

# Top 10 satisfied customers
top_10_satisfied = data.nlargest(10, 'satisfaction_score')
print("Top 10 Satisfied Customers:")
print(top_10_satisfied[['user_id', 'satisfaction_score']])

# Task 4.3: Regression Model (Predict Satisfaction Score)
X = data[['engagement_score', 'experience_score']]
y = data['satisfaction_score']

reg_model = LinearRegression()
reg_model.fit(X, y)

# Predicted satisfaction scores (optional validation)
data['predicted_satisfaction'] = reg_model.predict(X)
print("Regression Model Coefficients:", reg_model.coef_)
print("Mean Squared Error:", mean_squared_error(y, data['predicted_satisfaction']))

# Task 4.4: K-means Clustering (k=2)
kmeans = KMeans(n_clusters=2, random_state=42)
data['cluster'] = kmeans.fit_predict(data[['engagement_score', 'experience_score']])

# Task 4.5: Aggregate Satisfaction and Experience Scores by Cluster
cluster_aggregation = data.groupby('cluster')[['satisfaction_score', 'experience_score']].mean()
print("Cluster Aggregation:")
print(cluster_aggregation)

# Task 4.6: Export to MySQL
db_connection_string = 'mysql+pymysql://username:password@localhost/dbname'  # Update with actual credentials
engine = create_engine(db_connection_string)

# Export data
data[['user_id', 'engagement_score', 'experience_score', 'satisfaction_score']].to_sql(
    'user_satisfaction', con=engine, if_exists='replace', index=False
)

# Verify export (Example Query)
query_result = pd.read_sql("SELECT * FROM user_satisfaction LIMIT 10", con=engine)
print("Database Export Verification:")
print(query_result)
