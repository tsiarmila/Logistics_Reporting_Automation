import pandas as pd


def calculate_kpis(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["delivery_time_days"] = (
        df["delivery_date"] - df["ship_date"]
    ).dt.days

    df["planned_time_days"] = (
        df["planned_date"] - df["ship_date"]
    ).dt.days

    df["delay_days"] = (
        df["delivery_date"] - df["planned_date"]
    ).dt.days

    df["is_delayed"] = df["delay_days"] > 0

    return df


def summary_metrics(df: pd.DataFrame) -> dict:
    df = df.copy()
    df["cost"] = pd.to_numeric(df["cost"], errors="coerce").fillna(0)

    total_shipments = len(df)
    delayed = df["is_delayed"].sum()

    return {
        "total_shipments": total_shipments,
        "delayed_shipments": int(delayed),
        "delay_rate_%": round(delayed / total_shipments * 100, 2),
        "avg_delivery_days": round(df["delivery_time_days"].mean(), 2),
        "total_cost": round(df["cost"].sum(), 2),
    }
