# Power BI Dashboard

## Project
**ATELIER | Retail Sales & Profit Analytics**

The Power BI report contains two interactive report pages built from the retail sales dataset.

---

## Page 1 — Executive Overview

### KPI Cards
- Total Sales
- Total Orders
- Average Order Value
- Units Sold

### Visuals
- Sales by Region
- Sales by Category
- Sales by Payment Method
- Monthly Sales Trend

---

## Page 2 — Product & Profit Analysis

### KPI
- Total Profit

### Visuals
- Top Products by Sales
- Profit by Category
- Profit by Region
- Category Sales Volume
- Discount vs Profit Analysis

### Interactive Filters
- Region
- Category

---

## Core Measures

Example DAX measures:

```DAX
Total Sales = SUM(retail_sales[sales_amount_inr])

Total Orders = DISTINCTCOUNT(retail_sales[order_id])

Average Order Value = DIVIDE([Total Sales], [Total Orders])

Units Sold = SUM(retail_sales[quantity])

Total Profit = SUM(retail_sales[profit_amount_inr])
```

---

## Opening the Report

1. Open the `.pbix` file in **Microsoft Power BI Desktop**.
2. Refresh the dataset if required.
3. Use the Region and Category slicers on Page 2 to interact with the analysis.

> The PBIX file should be added to this folder after the final local report file is uploaded to the repository.
