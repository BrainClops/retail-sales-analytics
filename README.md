<h1 align="center">🛒 Retail Sales Analytics</h1>

<p align="center">
An end-to-end analytics pipeline that combines SQL, Python, and Machine Learning to
forecast sales and segment customers — served through an interactive dashboard.
</p>

<p align="center">
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white"/>
<img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white"/>
<img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white"/>
<img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
<img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white"/>
</p>

<p align="center">
<a href="https://github.com/Rohit0101010101"><img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white"/></a>
<a href="https://www.linkedin.com/in/rohit-mohammad-342785368/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white"/></a>
<a href="mailto:mohammadrohit456@gmail.com"><img src="https://img.shields.io/badge/Gmail-EA4335?style=flat-square&logo=gmail&logoColor=white"/></a>
</p>

---

## 📖 About

> Turning raw transactions into decisions — SQL + Python + Machine Learning.

Retail businesses generate huge amounts of transaction data but often struggle to
turn it into decisions. This project builds a pipeline that:

- 🗄️ Stores and queries transactional data using **SQL**
- 📈 Forecasts future sales using **Machine Learning**
- 👥 Segments customers into actionable groups using **RFM + K-Means clustering**
- 📊 Presents everything in a live, interactive **Streamlit dashboard**

## 🏗️ Architecture

```
CSV Data ──▶ SQLite Database ──▶ SQL Analytics Queries
                                        │
                        ┌───────────────┴───────────────┐
                        ▼                                ▼
              ML Sales Forecasting               ML Customer Segmentation
                        │                                │
                        └───────────────┬────────────────┘
                                         ▼
                               Streamlit Dashboard
```

## 📂 Project Structure

| Path | Description |
|---|---|
| `data/generate_data.py` | Generates the synthetic retail dataset |
| `data/*.csv` | Customers, products, transactions data |
| `database/schema.sql` | SQLite table definitions |
| `database/load_data.py` | Loads CSVs into SQLite |
| `database/analysis_queries.sql` | Business SQL queries (JOINs, CTEs, window functions) |
| `ml/forecasting.py` | Sales forecasting model (Polynomial Regression) |
| `ml/segmentation.py` | Customer segmentation (RFM + K-Means) |
| `app/dashboard.py` | Streamlit dashboard |
| `requirements.txt` | Python dependencies |

<details>
<summary><b>📁 Click to expand full folder tree</b></summary>

```
retail-analytics-project/
├── data/
│   ├── generate_data.py
│   ├── customers.csv
│   ├── products.csv
│   └── transactions.csv
├── database/
│   ├── schema.sql
│   ├── load_data.py
│   └── analysis_queries.sql
├── ml/
│   ├── forecasting.py
│   └── segmentation.py
├── app/
│   └── dashboard.py
├── requirements.txt
└── README.md
```

</details>

## ✨ Features

**SQL Analytics** — monthly revenue trend, top products, category breakdown,
customer lifetime value ranking (`RANK()`), month-over-month growth (`LAG()`),
and an RFM base query built with CTEs. Full query set in
[`database/analysis_queries.sql`](database/analysis_queries.sql).

**Sales Forecasting** — pulls historical monthly revenue via SQL, fits a
Polynomial Regression model with scikit-learn, forecasts the next N months,
and reports MAE / R².

**Customer Segmentation** — computes RFM metrics per customer via SQL, scales
the features, and applies K-Means clustering. Clusters are auto-labelled
*Champions*, *Loyal Customers*, *At Risk*, and *Low Value/New* based on their
relative RFM profile.

**Dashboard** — three tabs (Overview, Forecast, Segments), live SQL-backed
metrics, an adjustable forecast horizon, and a filterable segment explorer.

## 🚀 Run Locally

```bash
git clone https://github.com/Rohit0101010101/retail-sales-analytics.git
cd retail-sales-analytics

pip install -r requirements.txt

python data/generate_data.py
python database/load_data.py

streamlit run app/dashboard.py
```

## 💡 Sample Insights

- 🏆 Identified top 5 revenue-driving products and category-wise revenue split
- 📈 Forecasted next 3 months of revenue using historical trend
- 🎯 Segmented 500 customers into 4 actionable groups for targeted marketing

## 🔮 Future Improvements

- [ ] Swap synthetic data for a real-world dataset
- [ ] Add XGBoost/Prophet for advanced time-series forecasting
- [ ] Deploy on Streamlit Community Cloud for a live public demo
- [ ] Add cohort retention analysis

---

<p align="center">Built by <b>Rohit Mohammad</b></p>
