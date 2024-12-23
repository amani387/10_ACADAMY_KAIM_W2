# Task Three: Experience Analytics

This module is part of a project analyzing user experience metrics in the telecommunications industry. The focus is on deriving insights and making actionable recommendations for improving user experience.

## Task Overview

### Task 3.1: Aggregate Customer Data
- **Objective**: Compute per-customer averages for:
  - Average TCP Retransmission
  - Average RTT
  - Handset Type
  - Average Throughput
- **Output**: `aggregated_customer_data.csv`

### Task 3.2: Analyze Key Metrics
- **Objective**: Identify:
  - Top 10 values
  - Bottom 10 values
  - Most frequent values
- **Metrics**: 
  - TCP Retransmission
  - RTT
  - Throughput

### Task 3.3: Distribution Analysis
- **Objective**:
  - Analyze average throughput distribution per handset type.
  - Analyze average TCP retransmission distribution per handset type.
- **Output**: Visualizations and interpretation of trends.

### Task 3.4: K-Means Clustering
- **Objective**: Segment users into 3 clusters using k-means clustering on experience metrics.
- **Output**: Cluster descriptions and visualizations.

---

## Features

- **Data Cleaning**: Handles missing values and outliers.
- **Visualizations**: Distribution and clustering plots.
- **Actionable Insights**: Recommendations based on user metrics and trends.

---

## Prerequisites

1. **Python (>= 3.8)**
2. **Required Libraries**:
   - `pandas`
   - `numpy`
   - `matplotlib`
   - `seaborn`
   - `scikit-learn`
3. **Dataset**:
   - Place the dataset in a folder named `data`.
   - Dataset file: `cleaned_data.csv`.

Install dependencies:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
