# Power BI Dashboard Build Guide

## Goal
Build a clean, interactive, one-page executive retail sales dashboard from the project's synthetic CSV. The dashboard is a portfolio demonstration, not a report about a real retailer.

## 1. Load the data

1. Open Power BI Desktop.
2. Select **Get data → Text/CSV**.
3. Choose `data/retail_sales.csv` from this repository.
4. Select **Transform Data**.
5. In Power Query, rename the query to `retail_sales`.
6. Set data types:
   - `order_id`, `region`, `category`, `product`, `payment_method`: Text
   - `order_date`: Date
   - `quantity`: Whole number
   - `unit_price_inr`, `discount_pct`, `sales_amount_inr`, `profit_amount_inr`: Decimal number
7. Confirm there are 360 rows and no errors, then **Close & Apply**.

## 2. Create measures and calendar

Open `powerbi/measures.dax`. Create each measure with **Modeling → New measure**. Create the Calendar calculated table separately with **Modeling → New table**. The file contains both definitions and relationship instructions.

Create this relationship in Model view:

- `Calendar[Date]` → `retail_sales[order_date]`
- One-to-many, single direction, active.

Mark Calendar as the date table using `Calendar[Date]`. Sort Calendar[Month] by Calendar[Month Number].

## 3. Page design — Executive Overview

Canvas: 16:9. Suggested title: **ATELIER | RETAIL SALES PERFORMANCE**. Add a small subtitle: **Synthetic dataset · Jan–Dec 2025 · INR**.

### Top row — KPI cards

1. Total Sales — `[Total Sales]`
2. Total Orders — `[Total Orders]`
3. Units Sold — `[Units Sold]`
4. Average Order Value — `[Average Order Value]`
5. Estimated Profit — `[Estimated Profit]` (label clearly as estimated)

### Middle row — trends and mix

- Line chart: Axis `Calendar[Year Month]`, Values `[Total Sales]`.
- Clustered bar chart: Axis `retail_sales[region]`, Values `[Total Sales]`.
- Donut chart: Legend `retail_sales[category]`, Values `[Total Sales]`.

### Bottom row — product and payment detail

- Bar chart: Axis `retail_sales[product]`, Values `[Total Sales]`; apply Top N = 10 by Total Sales.
- Bar chart: Axis `retail_sales[payment_method]`, Values `[Total Orders]`.
- Optional matrix: Rows `region`, Columns `category`, Values `[Total Sales]`.

### Slicers

Add slicers for Calendar[Year Month], region, category and payment_method. Use dropdown style for compact filters. Ensure all visuals respond to slicers.

## 4. Formatting checklist

- Use a restrained dark navy / white / teal visual theme with consistent spacing.
- Use INR currency formatting with two decimals for monetary measures.
- Display sales labels in compact units (₹K / ₹L) where appropriate; retain exact values in tooltips.
- Sort monthly chart chronologically, not alphabetically.
- Use descriptive chart titles and axis labels.
- Avoid 3D charts and excessive borders.
- Add a visible footer: **Practice dataset — synthetic data; estimated profit is assumption-based and not actual accounting profit.**

## 5. Validate dashboard values

Expected source-data checks:

| Metric | Expected |
|---|---:|
| Orders | 360 |
| Units sold | 1,083 |
| Total sales | ₹1,183,184.10 |
| Average order value | ₹3,286.62 |
| Estimated profit | ₹511,709.71 |

Segment checks:

- Highest sales region: South — ₹326,299.00.
- Highest sales category: Electronics — ₹358,636.45.
- Highest sales month: 2025-06 — ₹121,253.65.
- Most frequent payment method: Card — 100 orders.

If values do not match, verify data types, filters, the Calendar relationship and whether the entire CSV was imported.

## 6. Save and publish portfolio evidence

1. Save as `Atelier_Retail_Sales_Dashboard.pbix` in a local `powerbi/` folder.
2. Export the report page to PDF or capture a clear screenshot for the repository.
3. Save screenshot as `powerbi/dashboard_overview.png`.
4. Do not commit the PBIX unless you intend to share the editable Power BI file publicly; review it first for metadata and file size.
5. Update the README with the screenshot and note that the dashboard was built in Power BI Desktop.

## Deliverables checklist

- [ ] CSV imported and typed correctly
- [ ] Calendar table and relationship created
- [ ] DAX measures created
- [ ] KPI cards built
- [ ] Monthly, regional and category charts built
- [ ] Product and payment visuals built
- [ ] Slicers interact correctly
- [ ] KPI values reconcile to source CSV
- [ ] Dashboard screenshot exported
- [ ] PBIX saved locally

**Important:** this guide and the DAX starter measures are prepared in the repository. The actual PBIX must be created and checked in Power BI Desktop; a PBIX file has not been generated or tested here.
