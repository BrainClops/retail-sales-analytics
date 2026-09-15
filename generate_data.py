"""
Generates a realistic synthetic retail sales dataset.
Simulates 2 years of transaction data for an online retail store.
"""
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

np.random.seed(42)
random.seed(42)

# --- Config ---
NUM_CUSTOMERS = 500
NUM_PRODUCTS = 40
NUM_TRANSACTIONS = 12000
START_DATE = datetime(2024, 1, 1)
END_DATE = datetime(2025, 12, 31)

CATEGORIES = ["Electronics", "Clothing", "Home & Kitchen", "Books", "Sports", "Beauty"]

PRODUCT_NAMES = {
    "Electronics": ["Wireless Earbuds", "Bluetooth Speaker", "Phone Case", "USB Cable", "Power Bank", "Smartwatch"],
    "Clothing": ["Cotton T-Shirt", "Denim Jeans", "Hoodie", "Formal Shirt", "Sneakers", "Jacket"],
    "Home & Kitchen": ["Non-stick Pan", "Coffee Maker", "Table Lamp", "Storage Box", "Cushion Cover", "Water Bottle"],
    "Books": ["Fiction Novel", "Self-Help Book", "Cookbook", "Biography", "Comic Book", "Notebook Set"],
    "Sports": ["Yoga Mat", "Resistance Bands", "Football", "Dumbbell Set", "Sports Cap", "Water Bottle - Sports"],
    "Beauty": ["Face Wash", "Moisturizer", "Lipstick", "Sunscreen", "Shampoo", "Perfume"],
}

CITIES = ["Kolkata", "Mumbai", "Delhi", "Bangalore", "Chennai", "Pune", "Hyderabad", "Ahmedabad"]


def build_products():
    rows = []
    pid = 1
    for cat, names in PRODUCT_NAMES.items():
        for name in names:
            rows.append({
                "product_id": pid,
                "product_name": name,
                "category": cat,
                "unit_price": round(np.random.uniform(150, 4000), 2)
            })
            pid += 1
    return pd.DataFrame(rows)


def build_customers():
    rows = []
    for cid in range(1, NUM_CUSTOMERS + 1):
        signup_date = START_DATE + timedelta(days=random.randint(0, 500))
        rows.append({
            "customer_id": cid,
            "city": random.choice(CITIES),
            "signup_date": signup_date.strftime("%Y-%m-%d")
        })
    return pd.DataFrame(rows)


def build_transactions(products_df, customers_df):
    rows = []
    date_range_days = (END_DATE - START_DATE).days

    # give some customers higher purchase frequency (realistic skew)
    customer_weights = np.random.exponential(scale=1.5, size=NUM_CUSTOMERS) + 0.2

    for i in range(1, NUM_TRANSACTIONS + 1):
        cust_id = np.random.choice(customers_df["customer_id"], p=customer_weights / customer_weights.sum())
        product = products_df.sample(1).iloc[0]
        quantity = np.random.choice([1, 1, 1, 2, 2, 3], p=[0.35, 0.25, 0.15, 0.15, 0.07, 0.03])

        # seasonal boost in Nov-Dec (festive/holiday sales)
        day_offset = random.randint(0, date_range_days)
        order_date = START_DATE + timedelta(days=day_offset)
        if order_date.month in [11, 12]:
            if random.random() < 0.3:
                day_offset = random.randint(300, 340)  # bias more into festive window
                order_date = START_DATE + timedelta(days=day_offset)

        rows.append({
            "transaction_id": i,
            "customer_id": int(cust_id),
            "product_id": int(product["product_id"]),
            "quantity": int(quantity),
            "unit_price": product["unit_price"],
            "total_amount": round(quantity * product["unit_price"], 2),
            "order_date": order_date.strftime("%Y-%m-%d")
        })

    return pd.DataFrame(rows).sort_values("order_date").reset_index(drop=True)


if __name__ == "__main__":
    products_df = build_products()
    customers_df = build_customers()
    transactions_df = build_transactions(products_df, customers_df)

    products_df.to_csv("/home/claude/retail-analytics-project/data/products.csv", index=False)
    customers_df.to_csv("/home/claude/retail-analytics-project/data/customers.csv", index=False)
    transactions_df.to_csv("/home/claude/retail-analytics-project/data/transactions.csv", index=False)

    print(f"Products: {len(products_df)} rows")
    print(f"Customers: {len(customers_df)} rows")
    print(f"Transactions: {len(transactions_df)} rows")
