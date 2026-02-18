import pandas as pd


def generate_report(df: pd.DataFrame, metrics: dict, output_path: str):
    with pd.ExcelWriter(output_path, engine="xlsxwriter") as writer:
        df.to_excel(writer, sheet_name="Shipments", index=False)

        metrics_df = pd.DataFrame(
            list(metrics.items()),
            columns=["Metric", "Value"]
        )

        metrics_df.to_excel(
            writer,
            sheet_name="Summary",
            index=False
        )
