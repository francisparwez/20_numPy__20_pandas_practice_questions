
# 40. 🔥 Pandas Boss-Level — Mini E-commerce Analysis
# Create or use an e-commerce dataset containing:
#     order_id
#     customer_id
#     order_date
#     city
#     product
#     category
#     quantity
#     unit_price
#     status
# Build a complete analysis.
#
# Calculate:
# Sales KPIs
#     Total revenue
#     Total orders
#     Average order value
#     Total quantity sold
#
# Customer analysis
#     Top 5 customers by spending
#     Average customer spending
#     Number of unique customers
#
# Product analysis
#     Best-selling product
#     Highest-revenue product
#     Revenue by category
#
# Geographic analysis
#     Revenue by city
#     Number of customers per city
#
# Time analysis
#     Monthly revenue
#     Monthly order count
#     Best-performing month
#
# Data quality
#     Missing values
#     Duplicate orders
#     Invalid prices
#     Invalid quantities
#
# Advanced
#     Customer
#     Total Spending
#     Number of Orders
#     Average Order Value
#     Customer Rank
#
# Finally, create an executive summary of the findings.


import pandas as pd
import numpy as np


# --------------------------------------------------
# 1. CREATE SYNTHETIC E-COMMERCE DATASET
# --------------------------------------------------

np.random.seed(42)
n_rows = 200

cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Miami']

categories = {
    'Electronics': ['Laptop', 'Smartphone', 'Headphones', 'Smartwatch'],
    'Clothing': ['T-Shirt', 'Jeans', 'Jackets', 'Sneakers'],
    'Home Decor': ['Lamp', 'Rug', 'Curtains', 'Vase']
}

prices = {
    'Laptop': 1000,
    'Smartphone': 700,
    'Headphones': 150,
    'Smartwatch': 250,
    'T-Shirt': 25,
    'Jeans': 60,
    'Jackets': 120,
    'Sneakers': 90,
    'Lamp': 45,
    'Rug': 150,
    'Curtains': 80,
    'Vase': 35
}

cust_ids = [f'CUST_{i:03d}' for i in range(1, 41)]

dates = pd.date_range(
    start='2026-01-01',
    end='2026-06-30',
    freq='D'
)

data = {
    'order_id': [f'ORD_{1000+i}' for i in range(n_rows)],
    'customer_id': np.random.choice(cust_ids, n_rows),
    'order_date': np.random.choice(dates, n_rows),
    'city': np.random.choice(cities, n_rows),
    'product': np.random.choice(list(prices.keys()), n_rows),
    'quantity': np.random.randint(1, 5, n_rows),
    'status': np.random.choice(
        ['Delivered', 'Cancelled', 'Returned'],
        n_rows
    )
}

df = pd.DataFrame(data)

# Map each product to its category
df['category'] = df['product'].map({
    product: category
    for category, products in categories.items()
    for product in products
})

# Map each product to its unit price
df['unit_price'] = df['product'].map(prices)

# Ensure order_date is a datetime column
df['order_date'] = pd.to_datetime(df['order_date'])

# Introduce data-quality issues for practice
df.loc[15, 'unit_price'] = -50.0  # Invalid price
df.loc[32, 'quantity'] = -5       # Invalid quantity
df.loc[50, 'city'] = np.nan       # Missing city


print("\n" + "=" * 60)
print("RAW E-COMMERCE DATASET")
print("=" * 60)

print(df.head(10))
print("\nDataset shape:", df.shape)


# --------------------------------------------------
# 2. DATA QUALITY ANALYSIS
# --------------------------------------------------

# Missing values in each column
missing_by_column = df.isnull().sum()

# Total missing cells
total_missing_values = df.isnull().sum().sum()

# Exact duplicate rows
duplicate_rows = df.duplicated().sum()

# Repeated order IDs after the first occurrence
duplicate_order_ids = df['order_id'].duplicated().sum()

# Invalid prices and quantities
invalid_prices = (df['unit_price'] <= 0).sum()
invalid_quantities = (df['quantity'] <= 0).sum()

print("\n" + "=" * 60)
print("DATA QUALITY REPORT")
print("=" * 60)

print("\nMissing values by column:")
print(missing_by_column)

print("\nTotal missing cells:", total_missing_values)
print("Exact duplicate rows:", duplicate_rows)
print("Repeated order IDs:", duplicate_order_ids)
print("Invalid prices:", invalid_prices)
print("Invalid quantities:", invalid_quantities)


# --------------------------------------------------
# 3. CLEAN THE DATA
# --------------------------------------------------

# Remove exact duplicate rows and invalid prices/quantities
df_clean = df[
    (df['unit_price'] > 0) &
    (df['quantity'] > 0)
].drop_duplicates().copy()

# Keep delivered orders for sales analysis
# Cancelled and returned orders are excluded from sales KPIs
sales_df = df_clean[
    df_clean['status'] == 'Delivered'
].copy()

# Calculate revenue for each order row
sales_df['revenue'] = (
    sales_df['quantity'] * sales_df['unit_price']
)

print("\n" + "=" * 60)
print("CLEANING SUMMARY")
print("=" * 60)

print("Original rows:", len(df))
print("Valid rows after cleaning:", len(df_clean))
print("Delivered sales rows:", len(sales_df))
print("Rows removed during cleaning:", len(df) - len(df_clean))


# --------------------------------------------------
# 4. SALES KPIs
# --------------------------------------------------

# Total revenue from delivered orders
total_revenue = sales_df['revenue'].sum()

# Number of unique delivered orders
total_orders = sales_df['order_id'].nunique()

# Average order value
order_totals = sales_df.groupby('order_id')['revenue'].sum()

average_order_value = order_totals.mean()

# Total quantity sold
total_quantity_sold = sales_df['quantity'].sum()

print("\n" + "=" * 60)
print("SALES KPIs")
print("=" * 60)

print(f"Total revenue: ${total_revenue:,.2f}")
print(f"Total orders: {total_orders:,}")
print(f"Average order value: ${average_order_value:,.2f}")
print(f"Total quantity sold: {total_quantity_sold:,}")


# --------------------------------------------------
# 5. CUSTOMER ANALYSIS
# --------------------------------------------------

# First calculate revenue for each customer-order combination
customer_orders = sales_df.groupby(
    ['customer_id', 'order_id']
)['revenue'].sum().reset_index()

# Calculate customer-level metrics
customer_metrics = customer_orders.groupby('customer_id').agg(
    Total_Spending=('revenue', 'sum'),
    Number_Of_Orders=('order_id', 'nunique'),
    Average_Order_Value=('revenue', 'mean')
).reset_index()

# Rank customers by total spending
customer_metrics['Customer_Rank'] = (
    customer_metrics['Total_Spending']
    .rank(ascending=False, method='min')
    .astype(int)
)

# Top 5 customers by spending
top_5_customers = customer_metrics.sort_values(
    'Total_Spending',
    ascending=False
).head(5)

# Average spending per customer
avg_customer_spending = customer_metrics[
    'Total_Spending'
].mean()

# Number of unique customers with delivered orders
unique_customers = sales_df['customer_id'].nunique()

print("\n" + "=" * 60)
print("CUSTOMER ANALYSIS")
print("=" * 60)

print("\nTop 5 customers by spending:")
print(top_5_customers.to_string(index=False))

print(
    f"\nAverage customer spending: "
    f"${avg_customer_spending:,.2f}"
)

print("Number of unique customers:", unique_customers)

print("\nComplete customer ranking:")
print(
    customer_metrics.sort_values(
        'Customer_Rank'
    ).to_string(index=False)
)


# --------------------------------------------------
# 6. PRODUCT ANALYSIS
# --------------------------------------------------

# Total quantity sold by product
quantity_by_product = sales_df.groupby(
    'product'
)['quantity'].sum().sort_values(ascending=False)

# Total revenue by product
revenue_by_product = sales_df.groupby(
    'product'
)['revenue'].sum().sort_values(ascending=False)

# Best-selling product by quantity
best_selling_product = quantity_by_product.idxmax()

# Product generating the highest revenue
highest_revenue_product = revenue_by_product.idxmax()

# Revenue by category
revenue_by_category = sales_df.groupby(
    'category'
)['revenue'].sum().sort_values(ascending=False)

print("\n" + "=" * 60)
print("PRODUCT ANALYSIS")
print("=" * 60)

print("\nQuantity sold by product:")
print(quantity_by_product)

print("\nRevenue by product:")
print(revenue_by_product)

print("\nBest-selling product:", best_selling_product)
print("Highest-revenue product:", highest_revenue_product)

print("\nRevenue by category:")
print(revenue_by_category)


# --------------------------------------------------
# 7. GEOGRAPHIC ANALYSIS
# --------------------------------------------------

# Revenue by city, including missing city values
revenue_by_city = sales_df.groupby(
    'city',
    dropna=False
)['revenue'].sum().sort_values(ascending=False)

# Unique customers per city
customers_per_city = sales_df.groupby(
    'city',
    dropna=False
)['customer_id'].nunique().sort_values(ascending=False)

print("\n" + "=" * 60)
print("GEOGRAPHIC ANALYSIS")
print("=" * 60)

print("\nRevenue by city:")
print(revenue_by_city)

print("\nNumber of unique customers per city:")
print(customers_per_city)


# --------------------------------------------------
# 8. TIME ANALYSIS
# --------------------------------------------------

# Extract year and month from order_date
sales_df['month'] = sales_df['order_date'].dt.to_period('M')

# Monthly revenue
monthly_revenue = sales_df.groupby(
    'month'
)['revenue'].sum().sort_index()

# Monthly order count
monthly_order_count = sales_df.groupby(
    'month'
)['order_id'].nunique().sort_index()

# Month with the highest revenue
best_performing_month = monthly_revenue.idxmax()

# Month with the most orders
busiest_month = monthly_order_count.idxmax()

print("\n" + "=" * 60)
print("TIME ANALYSIS")
print("=" * 60)

print("\nMonthly revenue:")
print(monthly_revenue)

print("\nMonthly order count:")
print(monthly_order_count)

print("\nBest-performing month by revenue:", best_performing_month)
print("Busiest month by order count:", busiest_month)


# --------------------------------------------------
# 9. ORDER STATUS ANALYSIS
# --------------------------------------------------

# Count orders by status
orders_by_status = df_clean.groupby(
    'status'
)['order_id'].nunique().sort_values(ascending=False)

print("\n" + "=" * 60)
print("ORDER STATUS ANALYSIS")
print("=" * 60)

print("\nUnique orders by status:")
print(orders_by_status)


# --------------------------------------------------
# 10. EXECUTIVE SUMMARY
# --------------------------------------------------

print("\n" + "=" * 60)
print("EXECUTIVE SUMMARY")
print("=" * 60)

print(
    f"""
Sales Performance
-----------------
Total revenue: ${total_revenue:,.2f}
Total delivered orders: {total_orders:,}
Average order value: ${average_order_value:,.2f}
Total quantity sold: {total_quantity_sold:,}

Customer Insights
-----------------
Unique customers with delivered orders: {unique_customers:,}
Average spending per customer: ${avg_customer_spending:,.2f}
Top-spending customer: {top_5_customers.iloc[0]['customer_id']}
Top customer's spending: ${top_5_customers.iloc[0]['Total_Spending']:,.2f}

Product Insights
----------------
Best-selling product by quantity: {best_selling_product}
Highest-revenue product: {highest_revenue_product}
Top-revenue category: {revenue_by_category.idxmax()}

Geographic Insights
-------------------
Highest-revenue city: {revenue_by_city.idxmax()}
Highest city revenue: ${revenue_by_city.max():,.2f}

Time Insights
-------------
Best-performing month by revenue: {best_performing_month}
Busiest month by order count: {busiest_month}

Data Quality
------------
Missing cells in raw dataset: {total_missing_values}
Exact duplicate rows: {duplicate_rows}
Repeated order IDs: {duplicate_order_ids}
Invalid prices: {invalid_prices}
Invalid quantities: {invalid_quantities}
"""
)
