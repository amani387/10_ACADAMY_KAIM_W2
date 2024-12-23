import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_distributions(file_path):
    # Load the dataset
    data = pd.read_csv(file_path)

    # Plot distribution of throughput per handset type
    plt.figure(figsize=(10, 6))
    sns.boxplot(x="Handset_Type", y="Throughput", data=data)
    plt.title("Distribution of Throughput per Handset Type")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Plot average TCP retransmission per handset type
    avg_tcp = data.groupby("Handset_Type")["TCP_Retransmission"].mean().reset_index()
    plt.figure(figsize=(10, 6))
    sns.barplot(x="Handset_Type", y="TCP_Retransmission", data=avg_tcp)
    plt.title("Average TCP Retransmission per Handset Type")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    return avg_tcp
