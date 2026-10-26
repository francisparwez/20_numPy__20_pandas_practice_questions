# 36. Merge two DataFrames
# Create:
#     customers
#     customer_id
#     customer_name
#     city
# and:
# orders
#     order_id
#     customer_id
#     amount
# Merge them together.
# Then calculate:
#     Total spending by customer.
# This directly connects with your SQL JOIN practice.

import pandas as pd

# Customers DataFrame
df1 = pd.DataFrame({
    'customer_id': [101, 102, 103, 104, 105],
    'customer_name': ['Ali', 'Sara', 'Ahmed', 'Ayesha', 'Usman'],
    'city': ['Karachi', 'Lahore', 'Islamabad', 'Karachi', 'Multan']
})

# Orders DataFrame
df2 = pd.DataFrame({
    'order_id': [1, 2, 3, 4, 5, 6, 7, 8],
    'customer_id': [101, 102, 101, 103, 102, 104, 105, 101],
    'amount': [5000, 3000, 2500, 4000, 1500, 6000, 2000, 1000]
})

df = df1.merge(df2, on='customer_id')

print(f"Original Dataframes:\n{df1}\n\n{df2}\n")
print(f"Merged Dataframes:\n{df}\n")

spending_by_customer = df.groupby(['customer_id', 'customer_name'])['amount'].sum().reset_index(name='total_spending')
print(f'Total Spending By Each Customer:\n{spending_by_customer}')