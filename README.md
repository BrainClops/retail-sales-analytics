<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:1a1a2e,100:16213e&height=200&section=header&text=Retail%20Sales%20Analytics&fontSize=36&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=SQL%20%2B%20Python%20%2B%20Machine%20Learning%20%7C%20End-to-End%20Analytics%20Pipeline&descSize=16&descAlignY=58" width="100%"/>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)

<br/>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=20&pause=1000&color=6C63FF&center=true&vCenter=true&width=650&lines=SQL-driven+analytics+%2B+ML+forecasting+%2B+customer+segmentation;JOINs+%C2%B7+CTEs+%C2%B7+Window+Functions+%C2%B7+K-Means+%C2%B7+Regression;Live+interactive+Streamlit+dashboard" alt="Typing SVG" />

</div>

<br/>

## 📌 Problem Statement

Retail businesses generate huge amounts of transaction data but often struggle to
turn it into decisions. This project builds a pipeline that:

- 🗄️ Stores and queries transactional data using **SQL**
- 📈 Forecasts future sales using **Machine Learning**
- 👥 Segments customers into actionable groups using **RFM + K-Means clustering**
- 📊 Presents everything in a live, interactive **dashboard**

<br/>

## 🏗️ Architecture

```
CSV Data (customers, products, transactions)
        │
        ▼
   SQLite Database  ◄──── schema.sql
        │
        ▼
  SQL Analytics Queries (JOINs, CTEs, window functions)
        │
        ├──► ML: Sales Forecasting (Polynomial Regression)
        │
        └──► ML: Customer Segmentation (RFM + K-Means)
                    │
                    ▼
           Streamlit Dashboard
```

<br/>

## 🛠️ Tech Stack

<div align="center">

| Layer | Tools |
|---|---|
| 🗄️ Database | SQLite — JOINs, CTEs, window functions |
| 🐍 Data Processing | Python, Pandas, NumPy |
| 🤖 Machine Learning | scikit-learn (Regression, K-Means, StandardScaler) |
| 📊 Dashboard | Streamlit |

</div>

<br/>

## 📂 Project Structure

```
retail-analytics-project/
├── data/
│   ├── generate_data.py      # generates synthetic retail dataset
│   ├── customers.csv
│   ├── products.csv
│   └── transactions.csv
├── database/
│   ├── schema.sql             # table definitions
│   ├── load_data.py           # loads CSVs into SQLite
│   └── analysis_queries.sql   # business SQL queries (JOINs, CTEs, window functions)
├── ml/
│   ├── forecasting.py         # revenue forecasting model
│   └── segmentation.py        # RFM + K-Means customer segmentation
├── app/
│   └── dashboard.py           # Streamlit dashboard
├── requirements.txt
└── README.md
```

<br/>

## ✨ Key Features

### 🗄️ SQL Analytics
- Monthly revenue trend, top products, category-wise breakdown
- Customer Lifetime Value ranking using **window functions** (`RANK()`, `LAG()`)
- RFM (Recency, Frequency, Monetary) base query using **CTEs**
- Month-over-month growth analysis

📄 See [`database/analysis_queries.sql`](database/analysis_queries.sql) for all queries.

### 📈 Sales Forecasting (ML)
- Pulls historical monthly revenue via SQL
- Polynomial Regression model (scikit-learn) to forecast next N months
- Evaluated using MAE and R²

### 👥 Customer Segmentation (ML)
- Computes RFM metrics per customer via SQL
- Standardizes features and applies **K-Means clustering**
- Auto-labels clusters as *Champions*, *Loyal Customers*, *At Risk*, *Low Value/New*

### 🖥️ Interactive Dashboard
- Live SQL-backed metrics and charts
- Adjustable forecast horizon
- Filterable customer segment explorer

<br/>

## 🚀 How to Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/Rohit0101010101/retail-sales-analytics.git
cd retail-sales-analytics

# 2. Install dependencies
pip install -r requirements.txt

# 3. Generate the dataset
python data/generate_data.py

# 4. Load data into SQLite
python database/load_data.py

# 5. Launch the dashboard
streamlit run app/dashboard.py
```

<br/>

## 💡 Sample Insights Generated

- 🏆 Identified top 5 revenue-driving products and category-wise revenue split
- 📈 Forecasted next 3 months of revenue using historical trend
- 🎯 Segmented 500 customers into 4 actionable groups for targeted marketing
  (e.g. re-engagement campaigns for "At Risk" customers)

<br/>

## 🔮 Future Improvements

- [ ] Swap synthetic data for a real-world dataset
- [ ] Add XGBoost/Prophet for advanced time-series forecasting
- [ ] Deploy on Streamlit Community Cloud for a live public demo
- [ ] Add cohort retention analysis

<br/>

<div align="center">

### 🙋 Author

**Rohit Mohammad**

<a href="https://github.com/Rohit0101010101">
  <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white"/>
</a>
<a href="https://www.linkedin.com/in/rohit-mohammad-342785368/">
  <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"/>
</a>
<a href="mailto:mohammadrohit456@gmail.com">
  <img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white"/>
</a>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:1a1a2e,100:16213e&height=100&section=footer" width="100%"/>

</div>
