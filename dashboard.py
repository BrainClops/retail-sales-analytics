"""
Retail Analytics Dashboard
Run with: streamlit run app/dashboard.py
"""
import streamlit as st
import sqlite3
import pandas as pd
import sys
import os

# Allow importing from ml/ folder
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ml.forecasting import get_monthly_revenue, forecast_next_months
from ml.segmentation import get_rfm_data, segment_customers

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "retail.db")

st.set_page_config(page_title="Retail Analytics Dashboard", layout="wide")


def run_query(query):
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df


st.title("🛒 Retail Sales Analytics & Forecasting Dashboard")
st.caption("SQL-driven analytics + ML forecasting + customer segmentation")

tab1, tab2, tab3 = st.tabs(["📊 Overview (SQL)", "📈 Sales Forecast (ML)", "👥 Customer Segments (ML)"])

# ---------------- TAB 1: SQL OVERVIEW ----------------
with tab1:
    col1, col2, col3 = st.columns(3)

    total_revenue = run_query("SELECT ROUND(SUM(total_amount),2) AS v FROM transactions")["v"][0]
    total_orders = run_query("SELECT COUNT(*) AS v FROM transactions")["v"][0]
    total_customers = run_query("SELECT COUNT(DISTINCT customer_id) AS v FROM transactions")["v"][0]

    col1.metric("Total Revenue", f"₹{total_revenue:,.0f}")
    col2.metric("Total Orders", f"{total_orders:,}")
    col3.metric("Unique Customers", f"{total_customers:,}")

    st.subheader("Monthly Revenue Trend")
    monthly = run_query("""
        SELECT strftime('%Y-%m', order_date) AS month, SUM(total_amount) AS revenue
        FROM transactions GROUP BY month ORDER BY month
    """)
    st.line_chart(monthly.set_index("month"))

    col_a, col_b = st.columns(2)
    with col_a:
        st.subheader("Revenue by Category")
        cat_rev = run_query("""
            SELECT p.category, ROUND(SUM(t.total_amount),2) AS revenue
            FROM transactions t JOIN products p ON t.product_id = p.product_id
            GROUP BY p.category ORDER BY revenue DESC
        """)
        st.bar_chart(cat_rev.set_index("category"))

    with col_b:
        st.subheader("Top 5 Products by Revenue")
        top_products = run_query("""
            SELECT p.product_name, ROUND(SUM(t.total_amount),2) AS revenue
            FROM transactions t JOIN products p ON t.product_id = p.product_id
            GROUP BY p.product_id ORDER BY revenue DESC LIMIT 5
        """)
        st.dataframe(top_products, use_container_width=True, hide_index=True)

    st.subheader("City-wise Performance")
    city_perf = run_query("""
        SELECT c.city, COUNT(DISTINCT c.customer_id) AS num_customers,
               ROUND(AVG(t.total_amount),2) AS avg_order_value,
               ROUND(SUM(t.total_amount),2) AS total_revenue
        FROM customers c JOIN transactions t ON c.customer_id = t.customer_id
        GROUP BY c.city ORDER BY total_revenue DESC
    """)
    st.dataframe(city_perf, use_container_width=True, hide_index=True)

# ---------------- TAB 2: FORECASTING ----------------
with tab2:
    st.subheader("Revenue Forecast — Next 3 Months")
    n_future = st.slider("Months to forecast", 1, 6, 3)

    monthly_df = get_monthly_revenue()
    forecast_df, metrics = forecast_next_months(monthly_df, n_future=n_future)

    st.line_chart(forecast_df.pivot(index="month", columns="type", values="revenue"))

    m1, m2 = st.columns(2)
    m1.metric("Model MAE", f"₹{metrics['mae']:,.0f}")
    m2.metric("R² Score", metrics["r2"])

    st.caption("Model: Polynomial Regression (degree 2) on monthly revenue trend, "
               "trained with scikit-learn. Fetches historical data via SQL.")

    st.dataframe(forecast_df.tail(n_future + 3), use_container_width=True, hide_index=True)

# ---------------- TAB 3: CUSTOMER SEGMENTATION ----------------
with tab3:
    st.subheader("Customer Segmentation (RFM + K-Means)")

    rfm_df = get_rfm_data()
    segmented_df, profile = segment_customers(rfm_df)

    seg_counts = segmented_df["segment"].value_counts().reset_index()
    seg_counts.columns = ["segment", "count"]

    col_x, col_y = st.columns([1, 1.3])
    with col_x:
        st.write("**Segment Distribution**")
        st.bar_chart(seg_counts.set_index("segment"))

    with col_y:
        st.write("**Average RFM per Segment**")
        profile_display = profile.copy()
        profile_display.index = [segmented_df[segmented_df["cluster"] == i]["segment"].iloc[0]
                                  for i in profile.index]
        st.dataframe(profile_display.round(1), use_container_width=True)

    st.write("**Segment meaning**")
    st.markdown("""
    - **Champions** — bought recently, buy often, spend the most
    - **Loyal Customers** — consistent buyers, good spend
    - **At Risk** — used to buy, activity slowing down
    - **Low Value / New** — infrequent or newly acquired customers
    """)

    st.write("**Customer-level detail**")
    selected_segment = st.selectbox("Filter by segment", ["All"] + sorted(segmented_df["segment"].unique().tolist()))
    display_df = segmented_df if selected_segment == "All" else segmented_df[segmented_df["segment"] == selected_segment]
    st.dataframe(
        display_df[["customer_id", "recency_days", "frequency", "monetary", "segment"]].sort_values("monetary", ascending=False),
        use_container_width=True, hide_index=True
    )
