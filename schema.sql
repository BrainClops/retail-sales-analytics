-- Retail Analytics Database Schema

DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    city TEXT NOT NULL,
    signup_date DATE NOT NULL
);

CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    category TEXT NOT NULL,
    unit_price REAL NOT NULL
);

CREATE TABLE transactions (
    transaction_id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    unit_price REAL NOT NULL,
    total_amount REAL NOT NULL,
    order_date DATE NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

CREATE INDEX idx_transactions_customer ON transactions(customer_id);
CREATE INDEX idx_transactions_date ON transactions(order_date);
CREATE INDEX idx_transactions_product ON transactions(product_id);
