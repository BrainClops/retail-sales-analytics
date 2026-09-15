<div align="center">

<img src="assets/banner.png" width="100%"/>

<br/><br/>

<a href="https://github.com/Rohit0101010101"><img src="https://img.shields.io/badge/GITHUB-000000?style=for-the-badge&logo=github&logoColor=white"/></a>
<a href="https://www.linkedin.com/in/rohit-mohammad-342785368/"><img src="https://img.shields.io/badge/LINKEDIN-000000?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
<a href="mailto:mohammadrohit456@gmail.com"><img src="https://img.shields.io/badge/GMAIL-000000?style=for-the-badge&logo=gmail&logoColor=white"/></a>

</div>

<br/>

## 📖 About

Hello! This is a **retail sales analytics pipeline** that turns raw transaction
data into decisions — built end-to-end with SQL, Python, and Machine Learning.

- 🗄️ Structured data stored and queried with **SQL** (JOINs, CTEs, window functions)
- 📈 Future revenue predicted with a **Machine Learning** forecasting model
- 👥 Customers grouped into actionable segments using **RFM + K-Means clustering**
- 📊 Everything visualized in a live, interactive **Streamlit dashboard**

<br/>

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

<br/>

## 🧰 Technologies

<div align="center">

<img src="https://img.shields.io/badge/-Python-000000?style=flat-square&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/-SQLite-000000?style=flat-square&logo=sqlite&logoColor=white"/>
<img src="https://img.shields.io/badge/-Pandas-000000?style=flat-square&logo=pandas&logoColor=white"/>
<img src="https://img.shields.io/badge/-NumPy-000000?style=flat-square&logo=numpy&logoColor=white"/>
<img src="https://img.shields.io/badge/-scikit--learn-000000?style=flat-square&logo=scikit-learn&logoColor=white"/>
<img src="https://img.shields.io/badge/-Streamlit-000000?style=flat-square&logo=streamlit&logoColor=white"/>

</div>

<br/>

## 📂 Structure

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

<br/>

## ✨ Features

**SQL Analytics** — monthly revenue trend, top products, category breakdown,
customer lifetime value ranking (`RANK()`), month-over-month growth (`LAG()`),
and an RFM base query built with CTEs. Full query set in
[`database/analysis_queries.sql`](database/analysis_queries.sql).

**Sales Forecasting** — pulls historical monthly revenue via SQL, fits a
Polynomial Regression model with scikit-learn, forecasts the next N months,
and reports MAE / R².

**Customer Segmentation** — computes RFM metrics per customer via SQL,
scales the features, and applies K-Means clustering. Clusters are
auto-labelled *Champions*, *Loyal Customers*, *At Risk*, and *Low Value/New*
based on their relative RFM profile.

**Dashboard** — three tabs (Overview, Forecast, Segments), live SQL-backed
metrics, an adjustable forecast horizon, and a filterable segment explorer.

<br/>

## ⚙️ Run Locally

```bash
git clone https://github.com/Rohit0101010101/retail-sales-analytics.git
cd retail-sales-analytics

pip install -r requirements.txt

python data/generate_data.py
python database/load_data.py

streamlit run app/dashboard.py
```

<br/>

## 📊 Statistics

<div align="center">

<img src="https://github-readme-stats.vercel.app/api/pin/?username=Rohit0101010101&repo=retail-sales-analytics&theme=dark&hide_border=true&title_color=ffffff&text_color=c9c9c9&icon_color=ffffff&bg_color=000000" width="70%"/>

</div>

<br/>

## 🔮 Future Improvements

- [ ] Swap synthetic data for a real-world dataset
- [ ] Add XGBoost/Prophet for advanced time-series forecasting
- [ ] Deploy on Streamlit Community Cloud for a live public demo
- [ ] Add cohort retention analysis

<br/>

<div align="center">

**Rohit Mohammad**

</div>
