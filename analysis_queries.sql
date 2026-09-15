-- ============================================================
-- Retail Analytics: Key Business SQL Queries
-- ============================================================

-- 1. Monthly Revenue Trend
SELECT
    strftime('%Y-%m', order_date) AS month,
    ROUND(SUM(total_amount), 2) AS revenue,
    COUNT(DISTINCT transaction_id) AS num_orders
FROM transactions
GROUP BY month
ORDER BY month;


-- 2. Top 5 Best-Selling Products by Revenue
SELECT
    p.product_name,
    p.category,
    SUM(t.quantity) AS units_sold,
    ROUND(SUM(t.total_amount), 2) AS total_revenue
FROM transactions t
JOIN products p ON t.product_id = p.product_id
GROUP BY p.product_id
ORDER BY total_revenue DESC
LIMIT 5;


-- 3. Revenue by Category
SELECT
    p.category,
    ROUND(SUM(t.total_amount), 2) AS revenue,
    ROUND(100.0 * SUM(t.total_amount) / (SELECT SUM(total_amount) FROM transactions), 2) AS pct_of_total
FROM transactions t
JOIN products p ON t.product_id = p.product_id
GROUP BY p.category
ORDER BY revenue DESC;


-- 4. Customer Lifetime Value (CLV) with ranking (window function)
WITH customer_totals AS (
    SELECT
        c.customer_id,
        c.city,
        ROUND(SUM(t.total_amount), 2) AS lifetime_value,
        COUNT(t.transaction_id) AS num_orders
    FROM transactions t
    JOIN customers c ON t.customer_id = c.customer_id
    GROUP BY c.customer_id
)
SELECT
    *,
    RANK() OVER (ORDER BY lifetime_value DESC) AS clv_rank
FROM customer_totals
ORDER BY clv_rank
LIMIT 10;


-- 5. RFM Base Query (Recency, Frequency, Monetary) — feeds into Python segmentation
WITH last_order AS (
    SELECT MAX(order_date) AS max_date FROM transactions
)
SELECT
    t.customer_id,
    CAST(julianday((SELECT max_date FROM last_order)) - julianday(MAX(t.order_date)) AS INTEGER) AS recency_days,
    COUNT(t.transaction_id) AS frequency,
    ROUND(SUM(t.total_amount), 2) AS monetary
FROM transactions t
GROUP BY t.customer_id;


-- 6. Month-over-Month Revenue Growth (window function: LAG)
WITH monthly AS (
    SELECT
        strftime('%Y-%m', order_date) AS month,
        SUM(total_amount) AS revenue
    FROM transactions
    GROUP BY month
)
SELECT
    month,
    ROUND(revenue, 2) AS revenue,
    ROUND(revenue - LAG(revenue) OVER (ORDER BY month), 2) AS mom_change,
    ROUND(100.0 * (revenue - LAG(revenue) OVER (ORDER BY month)) / LAG(revenue) OVER (ORDER BY month), 2) AS mom_pct_change
FROM monthly
ORDER BY month;


-- 7. City-wise Customer Count and Average Order Value
SELECT
    c.city,
    COUNT(DISTINCT c.customer_id) AS num_customers,
    ROUND(AVG(t.total_amount), 2) AS avg_order_value,
    ROUND(SUM(t.total_amount), 2) AS total_revenue
FROM customers c
JOIN transactions t ON c.customer_id = t.customer_id
GROUP BY c.city
ORDER BY total_revenue DESC;
