import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

def perform_clustering(file_path):
        # Calculate total TCP retransmission (downlink + uplink) for analysis
    data['Total TCP Retransmission (Bytes)'] = data['TCP DL Retrans. Vol (Bytes)'] + data['TCP UL Retrans. Vol (Bytes)']

    # Group data by 'Handset Type' and compute average TCP retransmission
    tcp_retransmission = data.groupby('Handset Type')['Total TCP Retransmission (Bytes)'].mean()

    # Display the result sorted by retransmission values
    tcp_retransmission.sort_values(ascending=False).head()

    # Load the dataset
    data = pd.read_csv(file_path)

    # Selecting relevant experience metrics for clustering
    experience_metrics = data[["Total DL (Bytes)", "Total UL (Bytes)", "Avg RTT DL (ms)", 
                            "Avg RTT UL (ms)", "TCP DL Retrans. Vol (Bytes)", 
                            "TCP UL Retrans. Vol (Bytes)"]]

    # Handling missing values (fill with mean)
    experience_metrics.fillna(experience_metrics.mean(), inplace=True)

    # Feature scaling
    scaler = StandardScaler()
    scaled_metrics = scaler.fit_transform(experience_metrics)

    # Apply k-means clustering
    kmeans = KMeans(n_clusters=3, random_state=42)
    clusters = kmeans.fit_predict(scaled_metrics)

    # Add cluster labels to the original data
    data["Cluster"] = clusters

    # Compute cluster characteristics
    cluster_summary = data.groupby("Cluster")[
        ["Total DL (Bytes)", "Total UL (Bytes)", "Avg RTT DL (ms)", 
        "Avg RTT UL (ms)", "TCP DL Retrans. Vol (Bytes)", 
        "TCP UL Retrans. Vol (Bytes)"]
    ].mean()

    cluster_summary

