# 25. Create calculated columns
# Given:
#     salary
# Create:
#     annual_salary
#     monthly_salary
#     tax
#     net_salary
# For example:
#     tax = salary × 0.10
# Concept: vectorized column operations.

import pandas as pd

df = pd.DataFrame({
    'employee': ['Alice', 'Bob', 'Charlie', 'David'],
    'monthly_salary': [4500, 6000, 3200, 8500]
})

# 1. Calculate annual salary
df['annual_salary'] = df['monthly_salary'] * 12

# 2. Calculate tax amount
df['tax'] = df['monthly_salary'] * 0.10

# 3. Calculate net salary
df['net_salary'] = df['monthly_salary'] - df['tax']

print(df)