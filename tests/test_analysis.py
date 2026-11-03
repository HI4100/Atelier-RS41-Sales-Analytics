import unittest
import pandas as pd
from analysis import build_summaries, load_data


class RetailAnalysisTests(unittest.TestCase):
    def test_dataset_loads_and_has_360_unique_orders(self):
        df = load_data()
        self.assertEqual(len(df), 360)
        self.assertEqual(df["order_id"].nunique(), 360)

    def test_sales_reconcile_to_source_rows(self):
        df = load_data()
        expected = (df["quantity"] * df["unit_price_inr"] * (1 - df["discount_pct"])).round(2)
        self.assertTrue((expected == df["sales_amount_inr"].round(2)).all())

    def test_kpis_reconcile(self):
        df = load_data()
        kpis = build_summaries(df)["kpis"].iloc[0]
        self.assertEqual(kpis["orders"], 360)
        self.assertEqual(kpis["units_sold"], 1083)
        self.assertAlmostEqual(kpis["total_sales_inr"], 1183184.10, places=2)
        self.assertAlmostEqual(kpis["average_order_value_inr"], 3286.62, places=2)

    def test_monthly_summary_has_12_months(self):
        self.assertEqual(len(build_summaries(load_data())["monthly_sales"]), 12)

    def test_duplicate_order_ids_are_rejected(self):
        df = load_data()
        duplicated = pd.concat([df, df.iloc[[0]]], ignore_index=True)
        # Exercise the validator through a temporary CSV file.
        import tempfile
        from pathlib import Path
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "duplicate.csv"
            duplicated.to_csv(path, index=False)
            with self.assertRaisesRegex(ValueError, "Duplicate order IDs"):
                load_data(path)


if __name__ == "__main__":
    unittest.main()
