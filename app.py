import os
import streamlit as st
import pandas as pd

from src.cleaner import clean_shipments
from src.kpi import calculate_kpis, summary_metrics
from src.report import generate_report


st.set_page_config(
    page_title="Logistics Reporting Dashboard",
    layout="wide"
)

st.title("📦 Logistics Reporting Automation")

os.makedirs("reports", exist_ok=True)

# 📂 Upload
uploaded_file = st.file_uploader(
    "Upload Shipments File",
    type=["csv", "xlsx"]
)

if uploaded_file:

    st.success("File uploaded successfully ✅")

    # Load
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

else:
    st.info("No file uploaded — using demo data")

    demo_data = {
        "shipment_id": ["S001", "S002", "S003", "S004"],
        "supplier": ["DHL", "UPS", "DHL", "FedEx"],
        "origin": ["Berlin", "Paris", "Madrid", "Prague"],
        "destination": ["Warsaw", "Rome", "Lisbon", "Vienna"],
        "ship_date": [
            "2025-01-01",
            "2025-01-02",
            "2025-01-03",
            "2025-01-04"
        ],
        "delivery_date": [
            "2025-01-03",
            "2025-01-05",
            "2025-01-04",
            "2025-01-08"
        ],
        "planned_date": [
            "2025-01-02",
            "2025-01-04",
            "2025-01-05",
            "2025-01-06"
        ],
        "cost": [1200, 900, 700, 1500],
    }

    df = pd.DataFrame(demo_data)

# Raw Data
st.subheader("📄 Raw Data")
with st.expander("Processed Data"):
    st.dataframe(df)

# Clean + KPI
df = clean_shipments(df)
df = calculate_kpis(df)

metrics = summary_metrics(df)

# Processed data
st.subheader("⚙️ Processed Data")

with st.expander("Show processed dataset"):
    st.dataframe(df)

# KPI Cards
st.subheader("📊 KPI Summary")

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric(
    "Total Shipments",
    metrics["total_shipments"]
)

col2.metric(
    "Delayed Shipments",
    metrics["delayed_shipments"]
)

col3.metric(
    "Delay Rate %",
    metrics["delay_rate_%"]
)

col4.metric(
    "Avg Delivery Days",
    metrics["avg_delivery_days"]
)

col5.metric(
    "Total Cost",
    f"${metrics['total_cost']:,.2f}"
)

# 📈 Delay Distribution
st.subheader("Delay Distribution")

st.bar_chart(df["delay_days"])

# 🏢 Supplier Analysis
st.subheader("Supplier Performance")

supplier_perf = (
    df.groupby("supplier")["delay_days"]
    .mean()
    .sort_values(ascending=False)
)

st.bar_chart(supplier_perf)

# Cost by supplier
st.subheader("💰 Cost by Supplier")

cost_perf = (
    df.groupby("supplier")["cost"]
    .sum()
    .sort_values(ascending=False)
)

st.bar_chart(cost_perf)

# 💾 Download report
st.subheader("Download Report")

output_path = "reports/temp_report.xlsx"

generate_report(df, metrics, output_path)

with open(output_path, "rb") as f:
    st.download_button(
        label="Download Excel Report",
        data=f,
        file_name="logistics_report.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

# Footer
st.markdown("---")
st.caption(
    "Logistics Reporting Automation • Built with Python & Streamlit"
)
