import pandas as pd

# =========================================================
# 1. LOAD DATA
# =========================================================

df = pd.read_csv("Indian_Retail_Store.csv")

print("\n========== DATA LOADED ==========")
print(df.head())


# =========================================================
# 2. DATA ANALYSIS / INSPECTION
# =========================================================

print("\n========== DATA SHAPE ==========")
print(df.shape)

print("\n========== DATA INFORMATION ==========")
print(df.info())

print("\n========== DESCRIPTIVE STATISTICS ==========")
print(df.describe())


# =========================================================
# 3. DATA CLEANING
# =========================================================

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

print("\n========== DUPLICATE ROWS ==========")
print(df.duplicated().sum())

# Remove duplicate records
df = df.drop_duplicates()

# Convert visit_date into proper datetime format
df["visit_date"] = pd.to_datetime(
    df["visit_date"],
    dayfirst=True,
    format="mixed"
)

print("\n========== DATE FORMAT ==========")
print(df["visit_date"].head())


# =========================================================
# 4. EXPLORATORY DATA ANALYSIS (EDA)
# =========================================================

print("\n========== TOTAL SALES ==========")
print(df["total_amount"].sum())

print("\n========== TOTAL TRANSACTIONS ==========")
print(df["total_amount"].count())

print("\n========== AVERAGE SALES ==========")
print(df["total_amount"].mean())

print("\n========== TOTAL QUANTITY SOLD ==========")
print(df["quantity"].sum())


# =========================================================
# 5. SALES BY PRODUCT CATEGORY
# =========================================================

print("\n========== SALES BY PRODUCT CATEGORY ==========")

category_sales = (
    df.groupby("product_category")["total_amount"]
    .sum()
    .sort_values(ascending=False)
)

print(category_sales)


# =========================================================
# 6. QUANTITY BY PRODUCT CATEGORY
# =========================================================

print("\n========== QUANTITY BY PRODUCT CATEGORY ==========")

category_quantity = (
    df.groupby("product_category")["quantity"]
    .sum()
    .sort_values(ascending=False)
)

print(category_quantity)


# =========================================================
# 7. SALES BY PAYMENT METHOD
# =========================================================

print("\n========== SALES BY PAYMENT METHOD ==========")

payment_sales = (
    df.groupby("payment_method")["total_amount"]
    .sum()
    .sort_values(ascending=False)
)

print(payment_sales)


# =========================================================
# 8. QUANTITY BY PAYMENT METHOD
# =========================================================

print("\n========== QUANTITY BY PAYMENT METHOD ==========")

payment_quantity = (
    df.groupby("payment_method")["quantity"]
    .sum()
    .sort_values(ascending=False)
)

print(payment_quantity)


# =========================================================
# 9. MONTHLY SALES
# =========================================================

print("\n========== MONTHLY SALES ==========")

monthly_sales = (
    df.groupby(df["visit_date"].dt.month)["total_amount"]
    .sum()
)

print(monthly_sales)


# =========================================================
# 10. TOP 10 CITIES BY SALES
# =========================================================

print("\n========== TOP 10 CITIES BY SALES ==========")

city_sales = (
    df.groupby("city")["total_amount"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(city_sales)


# =========================================================
# 11. QUANTITY BY STORE TYPE
# =========================================================

print("\n========== QUANTITY BY STORE TYPE ==========")

store_quantity = (
    df.groupby("store_type")["quantity"]
    .sum()
    .sort_values(ascending=False)
)

print(store_quantity)


# =========================================================
# 12. STORE TYPE PERFORMANCE
# =========================================================

print("\n========== STORE TYPE PERFORMANCE ==========")

store_performance = (
    df.groupby("store_type")["total_amount"]
    .agg(["sum", "count", "mean"])
    .sort_values("sum", ascending=False)
)

print(store_performance)


# =========================================================
# 13. SAVE CLEANED DATA
# =========================================================

df.to_csv("Indian_Retail_Store_Cleaned.csv", index=False)

print("\n========== PROCESS COMPLETED ==========")
print("Cleaned dataset saved successfully.")

# =========================================================
# 14. BAR CHART - SALES BY PRODUCT CATEGORY
# =========================================================

import matplotlib.pyplot as plt

category_sales = (
    df.groupby("product_category")["total_amount"]
      .sum()
      .sort_values(ascending=False)
)

plt.figure(figsize=(8, 5))

plt.bar(category_sales.index, category_sales.values)

plt.title("Sales by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.grid(axis="y", alpha=0.3)

plt.tight_layout()
plt.show()


# =========================================================
# 15. PIE CHART - SALES BY PAYMENT METHOD
# =========================================================

payment_sales = (
    df.groupby("payment_method")["total_amount"]
      .sum()
      .sort_values(ascending=False)
)

plt.figure(figsize=(7, 7))

plt.pie(
    payment_sales.values,
    labels=payment_sales.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Sales by Payment Method")

plt.tight_layout()
plt.show()


# =========================================================
# 16. LINE CHART - MONTHLY SALES TREND
# =========================================================

monthly_sales = (
    df.groupby(df["visit_date"].dt.to_period("M"))["total_amount"]
      .sum()
)

plt.figure(figsize=(9, 5))

monthly_sales.plot(kind="line", marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# =========================================================
# 17. BUSINESS INSIGHTS
# =========================================================

# Top Product Category
top_category = category_sales.idxmax()
top_category_sales = category_sales.max()

print("Top Product Category:", top_category)
print("Top Category Sales:", top_category_sales)


# Top Payment Method
top_payment = payment_sales.idxmax()
top_payment_sales = payment_sales.max()

print("Top Payment Method:", top_payment)
print("Top Payment Method Sales:", top_payment_sales)


# Total Sales
total_sales = df["total_amount"].sum()

print("Total Sales:", total_sales)


# Average Transaction Value
average_transaction = df["total_amount"].mean()

print("Average Transaction Value:", round(average_transaction, 2))

# =========================================================
# 18. DATASET SUMMARY
# =========================================================

print("Total Records:", len(df))
print("Total Customers:", df["bill_id"].nunique())
print("Total Product Categories:", df["product_category"].nunique())
print("Total Payment Methods:", df["payment_method"].nunique())