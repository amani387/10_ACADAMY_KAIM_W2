import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

def perform_clustering(file_path):
    # Load the dataset
    data = pd.read_csv(file_path)

    # Select metrics for clustering
    metrics = data[["TCP_Retransmission", "RTT", "Throughput"]]

    # Fill missing values
    metrics = metrics.fillna(metrics.mean())

    # Standardize the data
    scaler = StandardScaler()
    metrics_scaled = scaler.fit_transform(metrics)

    # Apply K-means clustering
    kmeans = KMeans(n_clusters=3, random_state=42)
    data["Cluster"] = kmeans.fit_predict(metrics_scaled)

    # Analyze clusters
    cluster_summary = data.groupby("Cluster").mean()

    # Visualize clusters
    plt.figure(figsize=(10, 6))
    plt.scatter(metrics_scaled[:, 0], metrics_scaled[:, 1], c=data["Cluster"], cmap="viridis", alpha=0.5)
    plt.title("K-Means Clustering (k=3)")
    plt.xlabel("Scaled TCP Retransmission")
    plt.ylabel("Scaled RTT")
    plt.colorbar(label="Cluster")
    plt.tight_layout()
    plt.show()

    return cluster_summary
