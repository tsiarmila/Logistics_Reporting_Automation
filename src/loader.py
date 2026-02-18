import pandas as pd
from pathlib import Path


def load_shipments(file_path: str) -> pd.DataFrame:
    path = Path(file_path)

    if path.suffix == ".csv":
        df = pd.read_csv(path)
    elif path.suffix in [".xlsx", ".xls"]:
        df = pd.read_excel(path)
    else:
        raise ValueError("Unsupported file format")

    return df
