# 🐼 Pandas — Level P2 — Data Cleaning
# 26. Handle missing values
# Given:
# data = {
#     "name": ["Alice", "Bob", "Charlie", "David"],
#     "age": [25, None, 35, 28],
#     "salary": [50000, 60000, None, 55000]
# }
# Find:
#     Number of missing values per column
#     Rows containing missing values
# Then:
#     Fill missing age with the median age
#     Fill missing salary with the median salary

import pandas as pd

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie", "David"],
    "age": [25, None, 35, 28],
    "salary": [50000, 60000, None, 55000]
})

# Number of missing values per column
print(df.isnull().sum())

# Rows containing missing values
print(df[df.isnull().any(axis=1)])

# Fill missing age with the median age
df['age'] = df['age'].fillna(df['age'].median())

# Fill missing salary with the median salary
df['salary'] = df['salary'].fillna(df['salary'].median())

print(df)
