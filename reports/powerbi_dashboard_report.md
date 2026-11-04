# Project 4 — Power BI Dashboard Report

## Project
**ATELIER | Retail Sales & Profit Analytics**

## Purpose
This project demonstrates how retail transaction data can be transformed into an interactive Business Intelligence report. The dashboard is organized into an executive overview and a detailed product/profit analysis page.

## Dataset
- 360 synthetic order-level records
- 2025 date range
- 4 regions: North, South, East and West
- 4 product categories: Electronics, Home & Kitchen, Fashion and Beauty
- 4 payment methods: Card, Cash, UPI and Net Banking
- 1,083 units sold

## Page 1 — Executive Overview
Includes Total Sales, Total Orders, Average Order Value and Units Sold KPI cards, plus visuals for regional sales, category sales, payment-method sales and monthly sales trend.

## Page 2 — Product & Profit Analysis
Includes Total Profit, top products by sales, profit by category, profit by region, category sales volume, a discount-versus-profit scatter visual, and Region and Category slicers.

## Dataset-level results
| KPI | Value |
|---|---:|
| Total sales | ₹1,183,184.10 |
| Total orders | 360 |
| Average order value | ₹3,286.62 |
| Units sold | 1,083 |
| Illustrative estimated profit | ₹511,709.71 |

## Findings
- South is the highest-sales region in the generated sample.
- Electronics is the highest-sales category by revenue.
- June 2025 is the highest-sales month.
- Card is the most frequently used payment method, with 100 orders.

## Tools
Microsoft Power BI Desktop, Power Query and DAX, supported by a Python/pandas validation and summary workflow and SQL analysis queries.

## Important limitations
The dataset is synthetic. Profit is a practice estimate based on assumed category cost ratios, not verified accounting profit. The findings describe only this generated dataset and should not be generalized to a real retailer.

## Reproducibility
The dataset, dictionary, Python script, SQL queries, tests, generated summaries and DAX starter measures are stored in this repository. Open the PBIX in Power BI Desktop and reconnect the source to `data/retail_sales.csv` if prompted.
