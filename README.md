# 📦 Logistics Reporting Automation

## Overview

Automated logistics reporting system that processes shipment data 
from Excel/CSV files and generates KPI analytics, delay insights, 
supplier performance metrics, and cost reports.

Designed as an end-to-end data pipeline + interactive dashboard 
for logistics and supply chain operations teams.

---

## 🚀 Features

- Automated shipment data ingestion
- Data cleaning & preprocessing
- Delivery delay detection
- KPI calculation
- Supplier performance analytics
- Cost analysis
- Excel report generation
- Interactive Streamlit dashboard
- Demo dataset fallback

---

## 📊 Calculated KPIs

- Total shipments
- Delayed shipments
- Delay rate %
- Average delivery time
- Total logistics cost
- Supplier delay performance

## 📁 Project Structure

```
project/
│
├── app.py
├── main.py
├── requirements.txt
│
├── src/
│   ├── loader.py
│   ├── cleaner.py
│   ├── kpi.py
│   └── report.py
│
├── reports/
│   └── temp_report.xlsx
│
└── README.md
```

## 🏗️ Project Architecture

Modules:

- `loader.py` — data ingestion
- `cleaner.py` — preprocessing & formatting
- `kpi.py` — KPI calculations
- `report.py` — Excel report builder
- `app.py` — Streamlit dashboard UI

---

## 🖥️ Dashboard Preview

Upload shipment file → View KPIs → Analyze delays → Download report

![Dashboard Screenshot](docs/dashboard_preview.png)

---

## 🧰 Tech Stack

**Data Processing**
- Python
- Pandas

**Visualization**
- Streamlit
- Matplotlib

**Reporting**
- OpenPyXL
- XlsxWriter

---

## ▶️ How to Run Locally

### 1️⃣ Clone repository
```bash
git clone https://github.com/your-username/logistics-reporting-automation.git
cd logistics-reporting-automation
```

### 2️⃣ Create virtual environment
```bash
python -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run Streamlit dashboard
```bash
streamlit run app.py
```

---

## 🧪 Demo Data

If no file is uploaded, the dashboard automatically loads a demo dataset
to showcase functionality.

## 🌐 Live Demo

🔗 https://logistics-reporting-automation.streamlit.app