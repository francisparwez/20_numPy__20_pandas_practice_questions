# 37. Find customers with no orders
# Using the same DataFrames:
# 	Perform a LEFT JOIN equivalent in Pandas.
# Find customers who have:
# 	no orders
# Hint:
# 	merge(..., how="left", indicator=True)
# This is an excellent SQL → Pandas connection.

import pandas as pd

# Customers DataFrame
df1 = pd.DataFrame({
    'customer_id': [101, 102, 103, 104, 105, 106],
    'customer_name': ['Ali', 'Sara', 'Ahmed', 'Ayesha', 'Usman', 'Zain'],
    'city': ['Karachi', 'Lahore', 'Islamabad', 'Karachi', 'Multan', 'Peshawar']
})

# Orders DataFrame
df2 = pd.DataFrame({
    'order_id': [1, 2, 3, 4, 5, 6, 7, 8],
    'customer_id': [101, 102, 101, 103, 102, 104, 105, 101],
    'amount': [5000, 3000, 2500, 4000, 1500, 6000, 2000, 1000]
})

df = df1.merge(df2, how='left', indicator=True)

no_orders = df[df['_merge'] == 'left_only'].loc[:, ['customer_id', 'customer_name', 'city']]

print(f'Original:\n{df}\n')
print(f'No Orders:\n{no_orders}\n')