from src.loader import load_shipments
from src.cleaner import clean_shipments
from src.kpi import calculate_kpis, summary_metrics
from src.report import generate_report
import matplotlib.pyplot as plt


def main():
    df = load_shipments("data/shipments_jan.csv")

    df = clean_shipments(df)
    df = calculate_kpis(df)

    metrics = summary_metrics(df)

    generate_report(
        df,
        metrics,
        "reports/logistics_report.xlsx"
    )


def plot_delays(df):
    df["delay_days"].hist()
    plt.title("Delay Distribution")
    plt.xlabel("Days")
    plt.ylabel("Shipments")
    plt.show()


if __name__ == "__main__":
    main()
