"""
Sales Forecasting Module
Pulls monthly revenue from SQL database and forecasts the next 3 months
using a polynomial regression model (captures trend + seasonality better
than plain linear regression, while staying simple enough to explain).
"""
import sqlite3
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_absolute_error, r2_score
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "retail.db")


def get_monthly_revenue():
    conn = sqlite3.connect(DB_PATH)
    query = """
        SELECT strftime('%Y-%m', order_date) AS month, SUM(total_amount) AS revenue
        FROM transactions
        GROUP BY month
        ORDER BY month
    """
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df


def forecast_next_months(df, n_future=3, degree=2):
    df = df.copy()
    df["month_index"] = np.arange(len(df))

    X = df[["month_index"]].values
    y = df["revenue"].values

    poly = PolynomialFeatures(degree=degree)
    X_poly = poly.fit_transform(X)

    model = LinearRegression()
    model.fit(X_poly, y)

    # in-sample fit quality
    y_pred = model.predict(X_poly)
    mae = mean_absolute_error(y, y_pred)
    r2 = r2_score(y, y_pred)

    # forecast future months
    future_index = np.arange(len(df), len(df) + n_future).reshape(-1, 1)
    future_poly = poly.transform(future_index)
    future_preds = model.predict(future_poly)

    last_month = pd.to_datetime(df["month"].iloc[-1])
    future_months = [
        (last_month + pd.DateOffset(months=i + 1)).strftime("%Y-%m")
        for i in range(n_future)
    ]

    forecast_df = pd.DataFrame({
        "month": future_months,
        "revenue": future_preds,
        "type": "forecast"
    })

    history_df = df[["month", "revenue"]].copy()
    history_df["type"] = "actual"

    combined = pd.concat([history_df, forecast_df], ignore_index=True)
    metrics = {"mae": round(mae, 2), "r2": round(r2, 3)}

    return combined, metrics


if __name__ == "__main__":
    monthly_df = get_monthly_revenue()
    result_df, metrics = forecast_next_months(monthly_df)
    print(result_df.to_string(index=False))
    print(f"\nModel fit -> MAE: {metrics['mae']}, R2: {metrics['r2']}")
