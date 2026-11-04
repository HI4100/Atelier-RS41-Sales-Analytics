# ATELIER | Retail Sales & Profit Analytics

An end-to-end retail analytics portfolio project combining **Python, pandas, SQL, data validation and Microsoft Power BI**.

The project analyses a 2025 retail sales dataset and presents the results through a two-page interactive Power BI dashboard focused on executive performance, products and profit.

> **Data transparency:** The 360-row dataset used in this portfolio is synthetic practice data. It does not represent a real company's customer or financial records. Profit values are illustrative estimates for analytical practice.

---

## Dashboard

### Page 1 — Executive Overview
The executive dashboard provides a high-level view of business performance:

- **Total Sales:** ₹1.18M
- **Total Orders:** 360
- **Average Order Value:** ₹3.29K
- **Units Sold:** 1K+
- Sales by Region
- Sales by Category
- Sales by Payment Method
- Monthly Sales Trend

### Page 2 — Product & Profit Analysis
The second page focuses on product, category and profitability performance:

- **Total Profit:** ₹511.71K
- Top Products by Sales
- Profit by Category
- Profit by Region
- Category Sales Volume
- Discount vs Profit Analysis
- Interactive Region and Category slicers

---

## Key Dataset Findings

| Metric | Result |
|---|---:|
| Records / Unique Orders | 360 / 360 |
| Date Coverage | Jan 1, 2025 – Dec 31, 2025 |
| Missing Values | 0 |
| Duplicate Order IDs | 0 |
| Sales Formula Mismatches | 0 |
| Units Sold | 1,083 |
| Total Sales | ₹11,83,184.10 |
| Estimated Profit | ₹5,11,709.71 |
| Average Order Value | ₹3,286.62 |

### Sample insights

- **South** generated the highest sales among regions.
- **Electronics** generated the highest category sales.
- **June 2025** was the strongest month by sales.
- **Card** was the most frequently used payment method in the dataset.

These findings describe the synthetic dataset only.

---

## Technology Stack

- **Microsoft Power BI Desktop** — interactive dashboard and DAX measures
- **Python** — analysis workflow
- **pandas** — data processing and validation
- **Matplotlib** — chart generation
- **SQL** — analytical queries
- **Git & GitHub** — version control and portfolio presentation

---

## Repository Structure

```text
Atelier-RS41-Sales-Analytics/
├── analysis.py                 # Python validation and analysis workflow
├── requirements.txt            # Python dependencies
├── data/                       # Source dataset and documentation
├── outputs/                    # Generated summaries and charts
├── powerbi/                    # Power BI project documentation / PBIX
├── reports/                    # Business analysis reports
├── sql/                        # SQL analysis queries
├── tests/                      # Validation tests
└── README.md
```

---

## Power BI Measures

The dashboard uses measures for core KPIs such as:

- **Total Sales**
- **Total Orders**
- **Average Order Value**
- **Units Sold**
- **Total Profit**

The report also uses interactive filtering to analyse results by **region** and **category**.

---

## Run the Python Analysis

1. Install Python 3.10 or newer.
2. Create a virtual environment:

```bash
python -m venv .venv
```

3. Activate it.

**Windows**

```bash
.venv\Scripts\activate
```

**macOS / Linux**

```bash
source .venv/bin/activate
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Run the analysis:

```bash
python analysis.py
```

6. Run tests:

```bash
python -m unittest discover -s tests -v
```

---

## Data Quality Checks

The Python workflow validates:

- Required columns
- Empty datasets
- Missing values
- Duplicate order IDs
- Date validity
- Numeric data types
- Positive quantities and sales values
- Discount ranges
- Sales calculation consistency

---

## Project Limitations

- The dataset is synthetic and intended for portfolio practice.
- The project does not include customer-level or personally identifiable data.
- Profit is illustrative and should not be treated as audited net profit.
- Results are descriptive and should not be interpreted as forecasts.

---

## Author

**Humza Warsi**

GitHub: https://github.com/HI4100

LinkedIn: https://www.linkedin.com/in/humza-warsi-910aa941b/

---

⭐ If you found this project useful, feel free to explore the repository and dashboard.
