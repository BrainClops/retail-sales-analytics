"""
Loads CSV data (customers, products, transactions) into a SQLite database
using the schema defined in schema.sql.
"""
import sqlite3
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "retail.db")
DATA_DIR = os.path.join(BASE_DIR, "data")
SCHEMA_PATH = os.path.join(BASE_DIR, "database", "schema.sql")


def load_database():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Create tables from schema
    with open(SCHEMA_PATH, "r") as f:
        cursor.executescript(f.read())

    # Load CSVs
    customers_df = pd.read_csv(os.path.join(DATA_DIR, "customers.csv"))
    products_df = pd.read_csv(os.path.join(DATA_DIR, "products.csv"))
    transactions_df = pd.read_csv(os.path.join(DATA_DIR, "transactions.csv"))

    customers_df.to_sql("customers", conn, if_exists="append", index=False)
    products_df.to_sql("products", conn, if_exists="append", index=False)
    transactions_df.to_sql("transactions", conn, if_exists="append", index=False)

    conn.commit()

    # Quick sanity check
    for table in ["customers", "products", "transactions"]:
        count = cursor.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
        print(f"{table}: {count} rows loaded")

    conn.close()
    print(f"\nDatabase created at: {DB_PATH}")


if __name__ == "__main__":
    load_database()
