"""Reproducible retail sales analysis for synthetic portfolio data."""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent
DATA_FILE = ROOT / "data" / "retail_sales.csv"
OUTPUT_DIR = ROOT / "outputs"
CHART_DIR = OUTPUT_DIR / "charts"
REQUIRED_COLUMNS = {
    "order_id", "order_date", "region", "category", "product", "quantity",
    "unit_price_inr", "discount_pct", "payment_method", "sales_amount_inr",
    "profit_amount_inr",
}
NUMERIC_COLUMNS = ["quantity", "unit_price_inr", "discount_pct", "sales_amount_inr", "profit_amount_inr"]


def load_data(path: Path = DATA_FILE) -> pd.DataFrame:
    """Load and validate the order-line CSV; fail loudly on data-quality issues."""
    df = pd.read_csv(path)
    missing_columns = REQUIRED_COLUMNS.difference(df.columns)
    if missing_columns:
        raise ValueError(f"Missing required columns: {sorted(missing_columns)}")
    if df.empty:
        raise ValueError("Dataset is empty")
    if df.isna().any().any():
        raise ValueError("Missing values found")
    if df["order_id"].duplicated().any():
        raise ValueError("Duplicate order IDs found; expected one row per order")
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
    if df["order_date"].isna().any():
        raise ValueError("Invalid order_date values found")
    for column in NUMERIC_COLUMNS:
        df[column] = pd.to_numeric(df[column], errors="coerce")
        if df[column].isna().any():
            raise ValueError(f"Non-numeric values found in {column}")
    if (df[["quantity", "unit_price_inr", "sales_amount_inr"]] <= 0).any().any():
        raise ValueError("Quantity, unit price and sales must be positive")
    if (df["profit_amount_inr"] < 0).any():
        raise ValueError("Negative estimated profit found")
    if not df["discount_pct"].between(0, 1).all():
        raise ValueError("discount_pct must be between 0 and 1")
    expected_sales = (df["quantity"] * df["unit_price_inr"] * (1 - df["discount_pct"])).round(2)
    mismatches = (expected_sales - df["sales_amount_inr"].round(2)).abs() > 0.01
    if mismatches.any():
        raise ValueError(f"Sales formula mismatch in {int(mismatches.sum())} rows")
    return df


def build_summaries(df: pd.DataFrame) -> dict[str, pd.DataFrame]:
    """Build KPI, regional, category, product, monthly and payment summaries."""
    data = df.copy()
    data["month"] = data["order_date"].dt.to_period("M").astype(str)
    order_count = data["order_id"].nunique()
    kpis = pd.DataFrame([{
        "orders": order_count,
        "units_sold": int(data["quantity"].sum()),
        "total_sales_inr": round(data["sales_amount_inr"].sum(), 2),
        "estimated_profit_inr": round(data["profit_amount_inr"].sum(), 2),
        "average_order_value_inr": round(data["sales_amount_inr"].sum() / order_count, 2),
        "estimated_profit_margin_pct": round(data["profit_amount_inr"].sum() / data["sales_amount_inr"].sum() * 100, 2),
    }])
    return {
        "kpis": kpis,
        "sales_by_region": data.groupby("region", as_index=False).agg(orders=("order_id", "nunique"), sales_inr=("sales_amount_inr", "sum"), estimated_profit_inr=("profit_amount_inr", "sum")).sort_values("sales_inr", ascending=False).round(2),
        "sales_by_category": data.groupby("category", as_index=False).agg(units_sold=("quantity", "sum"), sales_inr=("sales_amount_inr", "sum"), estimated_profit_inr=("profit_amount_inr", "sum")).sort_values("sales_inr", ascending=False).round(2),
        "monthly_sales": data.groupby("month", as_index=False).agg(orders=("order_id", "nunique"), sales_inr=("sales_amount_inr", "sum"), estimated_profit_inr=("profit_amount_inr", "sum")).sort_values("month").round(2),
        "top_products": data.groupby("product", as_index=False).agg(units_sold=("quantity", "sum"), sales_inr=("sales_amount_inr", "sum")).sort_values("sales_inr", ascending=False).head(10).round(2),
        "payment_methods": data.groupby("payment_method", as_index=False).agg(orders=("order_id", "nunique"), sales_inr=("sales_amount_inr", "sum")).sort_values("orders", ascending=False).round(2),
    }


def create_charts(summaries: dict[str, pd.DataFrame]) -> None:
    """Export PNG charts. Matplotlib is listed in requirements.txt."""
    import matplotlib.pyplot as plt
    CHART_DIR.mkdir(parents=True, exist_ok=True)
    chart_specs = [
        ("sales_by_region", "region", "sales_inr", "Sales by Region", "Sales (INR)", "bar"),
        ("sales_by_category", "category", "sales_inr", "Sales by Category", "Sales (INR)", "bar"),
        ("monthly_sales", "month", "sales_inr", "Monthly Sales Trend", "Sales (INR)", "line"),
        ("payment_methods", "payment_method", "orders", "Orders by Payment Method", "Orders", "bar"),
    ]
    for key, x_col, y_col, title, ylabel, kind in chart_specs:
        frame = summaries[key]
        fig, ax = plt.subplots(figsize=(9, 5))
        if kind == "line":
            ax.plot(frame[x_col], frame[y_col], marker="o")
            ax.tick_params(axis="x", rotation=45)
        else:
            ax.bar(frame[x_col], frame[y_col])
            ax.tick_params(axis="x", rotation=25)
        ax.set_title(title)
        ax.set_xlabel(x_col.replace("_", " ").title())
        ax.set_ylabel(ylabel)
        ax.grid(axis="y", alpha=0.25)
        fig.tight_layout()
        fig.savefig(CHART_DIR / f"{key}.png", dpi=160)
        plt.close(fig)


def main() -> None:
    df = load_data()
    summaries = build_summaries(df)
    OUTPUT_DIR.mkdir(exist_ok=True)
    for name, frame in summaries.items():
        frame.to_csv(OUTPUT_DIR / f"{name}.csv", index=False)
        print(f"\n{name.upper()}\n{frame.to_string(index=False)}")
    create_charts(summaries)
    print(f"\nValidated {len(df)} rows and generated {len(summaries)} summary CSV files plus 4 charts.")
    print("NOTE: dataset is synthetic; profit and profit margin are illustrative estimates.")


if __name__ == "__main__":
    main()
