# 38. Running total and moving average
# Given:
# 	date
# 	sales
# Calculate:
# 	1. Cumulative sales
# 	2. 3-day moving average
# Concepts:
# 	.cumsum()
# 	.rolling()
# This connects directly to the SQL window-function concepts you're currently learning.


import pandas as pd

df = pd.DataFrame({
    'date': [
        '2026-10-01',
        '2026-10-02',
        '2026-10-03',
        '2026-10-04',
        '2026-10-05',
        '2026-10-06',
        '2026-10-07'
    ],
    'sales': [1000, 1500, 800, 2000, 1200, 1800, 900]
})

df['cumulative_sales'] = df['sales'].cumsum()
df['moving_average_3day'] = df['sales'].rolling(window=3).mean()

print(df)