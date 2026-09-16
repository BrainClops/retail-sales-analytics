<img src="assets/banner.png" width="100%"/>

<h1 align="center">Retail Sales Analytics</h1>

<p align="center">
An end-to-end analytics pipeline that combines SQL, Python, and Machine Learning to
forecast sales and segment customers — served through an interactive dashboard.
</p>

<p align="center">
<a href="https://github.com/Rohit0101010101"><img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white"/></a>
<a href="https://www.linkedin.com/in/rohit-mohammad-342785368/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white"/></a>
<a href="mailto:mohammadrohit456@gmail.com"><img src="https://img.shields.io/badge/Gmail-EA4335?style=flat-square&logo=gmail&logoColor=white"/></a>
</p>

<p align="center">
<img src="https://skillicons.dev/icons?i=python,sqlite,pandas,sklearn,streamlit,git" />
</p>

---

## About

Retail businesses generate huge amounts of transaction data but often struggle to
turn it into decisions. This project builds a pipeline that:

- Stores and queries transactional data using **SQL**
- Forecasts future sales using **Machine Learning**
- Segments customers into actionable groups using **RFM + K-Means clustering**
- Presents everything in a live, interactive **Streamlit dashboard**

## Architecture

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

## Tech Stack

<table>
<tr>
<td align="center" width="96">
<img src="https://skillicons.dev/icons?i=python" width="48"/><br/>Python
</td>
<td align="center" width="96">
<img src="https://skillicons.dev/icons?i=sqlite" width="48"/><br/>SQLite
</td>
<td align="center" width="96">
<img src="https://skillicons.dev/icons?i=pandas" width="48"/><br/>Pandas
</td>
<td align="center" width="96">
<img src="https://skillicons.dev/icons?i=sklearn" width="48"/><br/>scikit-learn
</td>
<td align="center" width="96">
<img src="https://skillicons.dev/icons?i=streamlit" width="48"/><br/>Streamlit
</td>
<td align="center" width="96">
<img src="https://skillicons.dev/icons?i=git" width="48"/><br/>Git
</td>
</tr>
</table>

## Project Structure

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
├── assets/
│   └── banner.png
├── requirements.txt
└── README.md
```

## Features

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

## Run Locally

```bash
git clone https://github.com/Rohit0101010101/retail-sales-analytics.git
cd retail-sales-analytics

pip install -r requirements.txt

python data/generate_data.py
python database/load_data.py

streamlit run app/dashboard.py
```

## Sample Insights

- Identified top 5 revenue-driving products and category-wise revenue split
- Forecasted next 3 months of revenue using historical trend
- Segmented 500 customers into 4 actionable groups for targeted marketing

## Future Improvements

- [ ] Swap synthetic data for a real-world dataset
- [ ] Add XGBoost/Prophet for advanced time-series forecasting
- [ ] Deploy on Streamlit Community Cloud for a live public demo
- [ ] Add cohort retention analysis

---

<p align="center">
Built by <b>Rohit Mohammad</b>
</p>
