# =========================================================
# SALES ANALYSIS USING PYTHON
# Run this code in Jupyter Notebook
# Libraries: Pandas, NumPy, Matplotlib, Seaborn
# =========================================================

# -----------------------------
# STEP 1: IMPORT LIBRARIES
# -----------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Display charts inside notebook
%matplotlib inline

# Style for charts
sns.set(style="whitegrid")

# -----------------------------
# STEP 2: CREATE SAMPLE DATASET
# -----------------------------

np.random.seed(10)

products = ["Laptop", "Mobile", "Tablet", "Headphones", "Smartwatch"]
regions = ["North", "South", "East", "West"]

data = {
    "Order_ID": range(1001, 1501),
    "Product": np.random.choice(products, 500),
    "Region": np.random.choice(regions, 500),
    "Units_Sold": np.random.randint(1, 10, 500),
    "Price_Per_Unit": np.random.randint(500, 80000, 500),
    "Customer_Age": np.random.randint(18, 60, 500)
}

# Create DataFrame
df = pd.DataFrame(data)

# Add Total Sales column
df["Total_Sales"] = df["Units_Sold"] * df["Price_Per_Unit"]

# Add some missing values
df.loc[5:10, "Price_Per_Unit"] = np.nan

# Save dataset
df.to_csv("sales_data.csv", index=False)

print("Dataset Created Successfully!")
display(df.head())   # ✅ Use display instead of print for Jupyter

# -----------------------------
# STEP 3: LOAD DATASET
# -----------------------------

df = pd.read_csv("sales_data.csv")

print("\nDataset Information")
df.info()   # ✅ No need to wrap in print()

print("\nFirst 5 Records")
display(df.head())

# -----------------------------
# STEP 4: DATA CLEANING
# -----------------------------

print("\nMissing Values Before Cleaning")
print(df.isnull().sum())

# Fill missing values with mean
df["Price_Per_Unit"] = df["Price_Per_Unit"].fillna(df["Price_Per_Unit"].mean())


print("\nMissing Values After Cleaning")
print(df.isnull().sum())

# -----------------------------
# STEP 5: EXPLORATORY DATA ANALYSIS
# -----------------------------

print("\nStatistical Summary")
display(df.describe())

# Total Sales
total_sales = df["Total_Sales"].sum()
print(f"\nTotal Sales: ₹{total_sales:,.2f}")

# Average Sales
avg_sales = df["Total_Sales"].mean()
print(f"Average Sales: ₹{avg_sales:,.2f}")

# Best Selling Product
best_product = df.groupby("Product")["Total_Sales"].sum().idxmax()
print(f"Best Selling Product: {best_product}")

# Region Wise Sales
region_sales = df.groupby("Region")["Total_Sales"].sum()
print("\nRegion Wise Sales")
display(region_sales)

# -----------------------------
# STEP 6: DATA VISUALIZATION
# -----------------------------

# 1. BAR CHART - PRODUCT SALES
plt.figure(figsize=(8,5))
product_sales = df.groupby("Product")["Total_Sales"].sum()
sns.barplot(x=product_sales.index, y=product_sales.values)
plt.title("Product Wise Sales")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.xticks(rotation=20)
plt.show()

# 2. HISTOGRAM - CUSTOMER AGE
plt.figure(figsize=(8,5))
sns.histplot(df["Customer_Age"], bins=10, kde=True)
plt.title("Customer Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

# 3. SCATTER PLOT - PRICE VS SALES
plt.figure(figsize=(8,5))
sns.scatterplot(x=df["Price_Per_Unit"], y=df["Total_Sales"])
plt.title("Price vs Total Sales")
plt.xlabel("Price Per Unit")
plt.ylabel("Total Sales")
plt.show()

# 4. PIE CHART - REGION SALES
plt.figure(figsize=(7,7))
region_sales.plot(kind="pie", autopct="%1.1f%%")
plt.title("Region Wise Sales Distribution")
plt.ylabel("")
plt.show()

# 5. BOX PLOT - SALES DISTRIBUTION
plt.figure(figsize=(8,5))
sns.boxplot(x=df["Total_Sales"])
plt.title("Sales Distribution")
plt.show()

# 6. HEATMAP - CORRELATION
plt.figure(figsize=(8,5))
correlation = df.corr(numeric_only=True)
sns.heatmap(correlation, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# -----------------------------
# STEP 7: TOP 10 SALES RECORDS
# -----------------------------

top_sales = df.sort_values(by="Total_Sales", ascending=False).head(10)
print("\nTop 10 Sales Records")
display(top_sales)

# -----------------------------
# STEP 8: SAVE CLEANED DATA
# -----------------------------

df.to_csv("cleaned_sales_data.csv", index=False)
print("\nCleaned dataset saved successfully!")

# -----------------------------
# STEP 9: FINAL REPORT
# -----------------------------

print("\n========== SALES ANALYSIS REPORT ==========")
print(f"Total Records          : {len(df)}")
print(f"Total Sales            : ₹{total_sales:,.2f}")
print(f"Average Sales          : ₹{avg_sales:,.2f}")
print(f"Highest Sale           : ₹{df['Total_Sales'].max():,.2f}")
print(f"Lowest Sale            : ₹{df['Total_Sales'].min():,.2f}")
print(f"Best Selling Product   : {best_product}")
print("\nSales Analysis Completed Successfully!")
