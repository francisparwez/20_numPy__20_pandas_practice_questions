# 32. Multiple aggregations
# Using the same sales data, calculate by city:
#     Total Sales
#     Average Sales
#     Minimum Sale
#     Maximum Sale
#     Number of Transactions
# Try:
#     .agg()
# 🔥 This is the Pandas equivalent of the SQL aggregation work you've already been doing.

import pandas as pd

df = pd.DataFrame({
    'TransactionID': [1, 2, 3, 4, 5, 6, 7, 8, 9],
    'City': ['New York', 'Los Angeles', 'Chicago', 'New York',  'Los Angeles', 'Chicago', 'New York', 'Los Angeles', 'Chicago'],
    'Sales': [100, 200, 150, 300, 400, 250, 500, 600, 350]
})

summary_df = (
    df.groupby('City')
    .agg(
        Total_Sales=('Sales', 'sum'),
        Average_Sales=('Sales', 'mean'),
        Minimum_Sale=('Sales', 'min'),
        Maximum_Sale=('Sales', 'max'),
        Number_of_Transactions=('TransactionID', 'count')
    )
    .reset_index()
)

print(summary_df)