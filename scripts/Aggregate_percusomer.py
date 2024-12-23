import pandas as pd
from scipy.stats import zscore

def aggregate_per_customer(file_path):
    # Load the dataset
    data = pd.read_csv(file_path)
    
    # Handle missing values
    data["TCP DL Retrans. Vol (Bytes)"] = data["TCP DL Retrans. Vol (Bytes)"].fillna(data["TCP DL Retrans. Vol (Bytes)"].mean())
    data["TCP UL Retrans. Vol (Bytes)"] = data["TCP UL Retrans. Vol (Bytes)"].fillna(data["TCP UL Retrans. Vol (Bytes)"].mean())
    data["Avg RTT DL (ms)"] = data["Avg RTT DL (ms)"].fillna(data["Avg RTT DL (ms)"].mean())
    data["Avg RTT UL (ms)"] = data["Avg RTT UL (ms)"].fillna(data["Avg RTT UL (ms)"].mean())
    data["Avg Bearer TP DL (kbps)"] = data["Avg Bearer TP DL (kbps)"].fillna(data["Avg Bearer TP DL (kbps)"].mean())
    data["Avg Bearer TP UL (kbps)"] = data["Avg Bearer TP UL (kbps)"].fillna(data["Avg Bearer TP UL (kbps)"].mean())
    data["Handset Type"] = data["Handset Type"].fillna(data["Handset Type"].mode()[0])
    
    # Handle outliers using z-score
    for column in ["TCP DL Retrans. Vol (Bytes)", "TCP UL Retrans. Vol (Bytes)", 
                   "Avg RTT DL (ms)", "Avg RTT UL (ms)", 
                   "Avg Bearer TP DL (kbps)", "Avg Bearer TP UL (kbps)"]:
        z_scores = zscore(data[column])
        data[column] = data[column][(z_scores < 3)]
        data[column] = data[column].fillna(data[column].mean())  # Replace outliers with mean
    
    # Calculate additional metrics
    data["TCP Retransmission"] = (data["TCP DL Retrans. Vol (Bytes)"] + data["TCP UL Retrans. Vol (Bytes)"]) / 2
    data["Average RTT"] = (data["Avg RTT DL (ms)"] + data["Avg RTT UL (ms)"]) / 2
    data["Average Throughput"] = (data["Avg Bearer TP DL (kbps)"] + data["Avg Bearer TP UL (kbps)"]) / 2
    
    # Aggregate per customer
    aggregated_data = data.groupby("MSISDN/Number").agg({
        "TCP Retransmission": "mean",
        "Average RTT": "mean",
        "Average Throughput": "mean",
        "Handset Type": lambda x: x.mode()[0]  # Most common handset type
    }).reset_index()
    
    return aggregated_data

