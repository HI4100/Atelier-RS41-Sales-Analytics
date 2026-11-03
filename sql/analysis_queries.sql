-- Atelier Retail Sales Analytics | SQLite-compatible SQL
-- Load data/retail_sales.csv into a table named retail_sales first.
-- Dataset is synthetic. Profit fields are illustrative estimates only.

-- 1. Overall performance KPIs
SELECT COUNT(DISTINCT order_id) AS orders,
       SUM(quantity) AS units_sold,
       ROUND(SUM(sales_amount_inr), 2) AS sales_inr,
       ROUND(SUM(profit_amount_inr), 2) AS estimated_profit_inr,
       ROUND(SUM(sales_amount_inr) / COUNT(DISTINCT order_id), 2) AS average_order_value_inr
FROM retail_sales;

-- 2. Regional performance and sales contribution
SELECT region, COUNT(DISTINCT order_id) AS orders,
       ROUND(SUM(sales_amount_inr), 2) AS sales_inr,
       ROUND(100.0 * SUM(sales_amount_inr) / (SELECT SUM(sales_amount_inr) FROM retail_sales), 2) AS sales_share_pct
FROM retail_sales GROUP BY region ORDER BY sales_inr DESC;

-- 3. Category performance
SELECT category, SUM(quantity) AS units_sold,
       ROUND(SUM(sales_amount_inr), 2) AS sales_inr,
       ROUND(SUM(profit_amount_inr), 2) AS estimated_profit_inr
FROM retail_sales GROUP BY category ORDER BY sales_inr DESC;

-- 4. Monthly sales trend (SQLite)
SELECT strftime('%Y-%m', order_date) AS month,
       COUNT(DISTINCT order_id) AS orders,
       ROUND(SUM(sales_amount_inr), 2) AS sales_inr
FROM retail_sales GROUP BY month ORDER BY month;

-- 5. Payment-method adoption
SELECT payment_method, COUNT(DISTINCT order_id) AS orders,
       ROUND(SUM(sales_amount_inr), 2) AS sales_inr
FROM retail_sales GROUP BY payment_method ORDER BY orders DESC;

-- 6. Top 10 products by sales
SELECT product, SUM(quantity) AS units_sold,
       ROUND(SUM(sales_amount_inr), 2) AS sales_inr
FROM retail_sales GROUP BY product ORDER BY sales_inr DESC LIMIT 10;

-- 7. Discount-band analysis
SELECT CASE WHEN discount_pct = 0 THEN '0%'
            WHEN discount_pct <= 0.05 THEN '>0-5%'
            WHEN discount_pct <= 0.10 THEN '>5-10%'
            WHEN discount_pct <= 0.15 THEN '>10-15%'
            ELSE '>15-20%' END AS discount_band,
       COUNT(*) AS order_lines,
       ROUND(SUM(sales_amount_inr), 2) AS sales_inr,
       ROUND(AVG(profit_amount_inr), 2) AS avg_estimated_profit_per_order
FROM retail_sales GROUP BY discount_band ORDER BY MIN(discount_pct);

-- 8. Region x category sales matrix
SELECT region, category, ROUND(SUM(sales_amount_inr), 2) AS sales_inr
FROM retail_sales GROUP BY region, category ORDER BY region, sales_inr DESC;
