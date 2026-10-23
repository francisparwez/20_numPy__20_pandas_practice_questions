# 31. GroupBy analysis
# Given sales data:
#     City | Product | Sales
# Calculate:
#     Total sales by city
#     Average sales by city
#     Total sales by product
#     Number of transactions by city
# Concept: groupby() 

import pandas as pd

df = pd.DataFrame({
    "City": [
        "Karachi", "Lahore", "Karachi", "Islamabad",
        "Lahore", "Karachi", "Islamabad", "Lahore"
    ],
    "Product": [
        "Laptop", "Mobile", "Mobile", "Laptop",
        "Laptop", "Laptop", "Mobile", "Mobile"
    ],
    "Sales": [
        100000, 50000, 30000, 90000,
        80000, 120000, 40000, 60000
    ]
})

print(df)
print("\nDataFrame shape:", df.shape)

sum_of_sales_by_city = df.groupby("City")["Sales"].sum()
avg_of_sales_by_city = round(df.groupby("City")["Sales"].mean(), 2)
sum_of_sales_by_product = df.groupby("Product")["Sales"].sum()
transactions_by_city = df.groupby("City").size()


print(f"Total Sales By City:\n{sum_of_sales_by_city}")
print(f"Average Sales By City:\n{avg_of_sales_by_city}")
print(f"Total Sales By Product:\n{sum_of_sales_by_product}")
print(f"Number of Transactions By City:\n{transactions_by_city}")

