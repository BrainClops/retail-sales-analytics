"""
Customer Segmentation Module
Computes RFM (Recency, Frequency, Monetary) metrics via SQL, then applies
K-Means clustering to group customers into segments like "Champions",
"At Risk", "Loyal", "New/Low-value".
"""
import sqlite3
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "retail.db")

RFM_QUERY = """
WITH last_order AS (
    SELECT MAX(order_date) AS max_date FROM transactions
)
SELECT
    t.customer_id,
    CAST(julianday((SELECT max_date FROM last_order)) - julianday(MAX(t.order_date)) AS INTEGER) AS recency_days,
    COUNT(t.transaction_id) AS frequency,
    ROUND(SUM(t.total_amount), 2) AS monetary
FROM transactions t
GROUP BY t.customer_id
"""


def get_rfm_data():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query(RFM_QUERY, conn)
    conn.close()
    return df


def segment_customers(rfm_df, n_clusters=4):
    df = rfm_df.copy()

    features = df[["recency_days", "frequency", "monetary"]]
    scaler = StandardScaler()
    scaled = scaler.fit_transform(features)

    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    df["cluster"] = kmeans.fit_predict(scaled)

    # Label clusters based on their average RFM profile (higher monetary/frequency,
    # lower recency = better customer)
    cluster_profile = df.groupby("cluster")[["recency_days", "frequency", "monetary"]].mean()
    cluster_profile["score"] = (
        cluster_profile["monetary"].rank() +
        cluster_profile["frequency"].rank() -
        cluster_profile["recency_days"].rank()
    )
    ranked_clusters = cluster_profile.sort_values("score", ascending=False).index.tolist()

    labels_map = {}
    label_names = ["Champions", "Loyal Customers", "At Risk", "Low Value / New"]
    for i, cluster_id in enumerate(ranked_clusters):
        labels_map[cluster_id] = label_names[i] if i < len(label_names) else f"Segment {i+1}"

    df["segment"] = df["cluster"].map(labels_map)
    return df, cluster_profile


if __name__ == "__main__":
    rfm_df = get_rfm_data()
    segmented_df, profile = segment_customers(rfm_df)

    print("Segment distribution:")
    print(segmented_df["segment"].value_counts())
    print("\nCluster profile (avg RFM per segment):")
    print(profile.round(2))
    print("\nSample customers:")
    print(segmented_df.head(10).to_string(index=False))
