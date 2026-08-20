# 📊 Sales Data Analysis | Python, SQL & Power BI

## 📌 Project Overview

This project presents an end-to-end **Sales Data Analysis** performed using **Python, SQL, and Power BI**.

The objective of this project is to analyze sales transactions, identify top-performing product categories and payment methods, understand sales trends, and create an interactive dashboard to support data-driven business decisions.

The project demonstrates the complete data analytics workflow:

**Raw Data → Data Cleaning → Exploratory Data Analysis → SQL Analysis → Power BI Dashboard → Business Insights**

---

## 🎯 Business Objectives

The key objectives of this analysis are:

- Analyze overall sales performance
- Identify the top-performing product category
- Analyze sales by payment method
- Understand monthly sales trends
- Calculate average transaction value
- Identify important sales patterns
- Create meaningful business KPIs
- Build an interactive Power BI dashboard
- Present actionable insights for business decision-making

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|---|---|
| 🐍 Python | Data Cleaning & Exploratory Data Analysis |
| 🐼 Pandas | Data Manipulation & Analysis |
| 📊 Matplotlib | Data Visualization |
| 🗄️ SQL | Business Analysis & Data Queries |
| 📈 Power BI | Interactive Dashboard & Visualization |
| 📁 Excel / CSV | Dataset & Data Preparation |
| 💻 GitHub | Project Documentation & Version Control |

---

## 🔄 Project Workflow

```text
Raw Sales Dataset
       ↓
Data Cleaning using Python
       ↓
Exploratory Data Analysis
       ↓
SQL Business Analysis
       ↓
Power BI Data Modeling
       ↓
Dashboard Development
       ↓
Business Insights
```

---

# 🐍 Python Analysis

Python was used for data cleaning, transformation, exploratory analysis, and generating initial insights.

### Key Python Tasks

- Loaded the sales dataset using Pandas
- Checked dataset structure and data types
- Identified missing values
- Checked duplicate records
- Cleaned and transformed data
- Converted numerical columns into appropriate data types
- Created calculated metrics
- Performed category-wise and payment-wise analysis
- Analyzed sales trends
- Generated visualizations using Matplotlib

### Example Analysis

```python
import pandas as pd

df = pd.read_csv("sales_data.csv")

# Total Sales
total_sales = df["Sales"].sum()

# Average Transaction Value
average_transaction = df["Sales"].mean()

# Category-wise Sales
category_sales = df.groupby("Category")["Sales"].sum()

print(category_sales)
```

---

# 🗄️ SQL Analysis

SQL was used to perform business-oriented analysis and extract meaningful insights from the sales data.

### Key SQL Analysis

- Total sales
- Average transaction value
- Category-wise sales
- Payment method analysis
- Monthly sales trends
- Top-performing categories
- Sales contribution by category
- Transaction-level analysis
- Aggregated business KPIs

### Example SQL Query

```sql
SELECT
    category,
    SUM(sales) AS total_sales
FROM sales_data
GROUP BY category
ORDER BY total_sales DESC;
```

---

# 📊 Power BI Dashboard

The cleaned dataset was imported into **Power BI** to create an interactive sales dashboard.

### Dashboard KPIs

- 💰 Total Sales
- 🧾 Total Records
- 👥 Total Customers
- 📦 Total Product Categories
- 💳 Total Payment Methods
- 📈 Average Transaction Value

### Dashboard Visualizations

- Monthly Sales Trend
- Sales by Product Category
- Sales by Payment Method
- Category Performance
- Sales Distribution
- Interactive Filters / Slicers

---

# 📸 Dashboard Preview

![Sales Dashboard](images/sales_dashboard.png)

> **Note:** Replace `images/sales_dashboard.png` with the actual path/name of your Power BI dashboard screenshot.

---

# 📈 Key Business Insights

Based on the analysis:

### 💰 Overall Performance

- **Total Sales:** ₹381,350
- **Average Transaction Value:** ₹7,627
- **Total Records:** 50
- **Total Customers:** 50
- **Total Product Categories:** 4
- **Total Payment Methods:** 4

### 🏆 Top Product Category

**Electronics** was the highest-performing product category.

- **Electronics Sales:** ₹296,000

Electronics contributed the largest share of overall sales and was the strongest category in the dataset.

### 💳 Top Payment Method

**Credit Card** generated the highest sales among the available payment methods.

- **Credit Card Sales:** ₹296,000

This indicates that credit-card transactions represented a significant portion of the analyzed sales value.

---

# 💡 Business Recommendations

Based on the analysis, businesses can:

1. Focus on high-performing product categories such as **Electronics**.
2. Maintain sufficient inventory for products generating higher sales.
3. Encourage customers to use preferred digital payment methods.
4. Monitor monthly sales trends to identify growth opportunities.
5. Use dashboard KPIs for regular performance monitoring.
6. Analyze low-performing categories to identify improvement opportunities.
7. Combine sales, customer, and payment analysis for better business decisions.

---

# 📂 Project Structure

```text
Sales-Data-Analysis/
│
├── README.md
│
├── data/
│   └── sales_data.csv
│
├── python/
│   └── sales_analysis.py
│
├── sql/
│   └── sales_analysis.sql
│
├── powerbi/
│   └── Sales_Dashboard.pbix
│
├── images/
│   └── sales_dashboard.png
│
└── reports/
    └── analysis_summary.pdf
```

---

# 📁 Project Files

### 🐍 Python
Contains Python scripts used for:

- Data cleaning
- Data transformation
- Exploratory Data Analysis
- KPI calculations
- Visualization

### 🗄️ SQL
Contains SQL queries used for:

- Aggregation
- Grouping
- Business analysis
- Category analysis
- Payment analysis
- Sales trend analysis

### 📊 Power BI
Contains the interactive dashboard and visualization layer.

### 📄 Dataset
Contains the raw sales transaction data used for analysis.

---

# 🚀 Skills Demonstrated

Through this project, I demonstrated practical knowledge of:

- Data Cleaning
- Exploratory Data Analysis
- SQL
- Python
- Pandas
- Matplotlib
- Power BI
- Data Visualization
- KPI Development
- Business Analysis
- Data Storytelling
- GitHub Documentation

---

# 👨‍💻 About Me

I am a **Mathematics graduate** with professional experience in **MIS Reporting, Inventory Management, Operations Reporting, and Data Analysis**.

I am currently developing my skills in:

**SQL | Power BI | Excel | Python | Data Analytics**

This project is part of my Data Analytics portfolio, demonstrating my ability to transform raw data into meaningful business insights.

---

## ⭐ If you found this project useful

Feel free to explore the project files and analysis.

**Thank you for visiting my Data Analytics Portfolio! 🚀**
