# Task Two: User Engagement Analytics

This module focuses on analyzing user engagement metrics for a telecommunications dataset. The objective is to derive insights into user behavior and activity patterns.

---

## Task Overview

### Task 2.1: Analyze User Engagement
- **Objective**: Analyze the following metrics for each user:
  - Session Frequency
  - Total Session Duration
  - Total Traffic (Download + Upload)
- **Output**: Top 10 users for each metric.

### Task 2.2: Clustering Based on Engagement
- **Objective**:
  - Normalize engagement metrics.
  - Perform K-Means clustering to group users into three engagement clusters.
  - Optimize the number of clusters using the Elbow Method.

### Task 2.3: Insights and Recommendations
- **Objective**:
  - Provide data-driven recommendations based on engagement patterns.

---

## Features

- **Data Aggregation**: Computes engagement metrics per user.
- **Clustering**: Groups users into engagement clusters using K-Means.
- **Visualizations**: Elbow plots, scatter plots, and histograms.
- **Actionable Insights**: Highlights top users and recommends strategies.

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
