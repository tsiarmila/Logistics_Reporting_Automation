import pandas as pd


def clean_shipments(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    date_cols = ["ship_date", "delivery_date", "planned_date"]
    for col in date_cols:
        df[col] = pd.to_datetime(df[col])

    df = df.drop_duplicates(subset="shipment_id")

    #  FIX cost
    df["cost"] = (
        df["cost"]
        .astype(str)
        .str.replace(",", "")
        .str.replace("$", "")
        .str.strip()
    )

    df["cost"] = pd.to_numeric(df["cost"], errors="coerce")

    df["cost"] = df["cost"].fillna(0)

    return df
