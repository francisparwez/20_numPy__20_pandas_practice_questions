# 23. Filter rows
# Given employee data, find employees:
#     Age > 30
#     Salary > 60,000
#     Salary between 50,000 and 70,000
#     Age > 25 AND salary > 55,000
# Concept: Boolean filtering.

import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie", "David"],
    "age": [25, 30, 35, 28],
    "salary": [50000, 60000, 75000, 55000]
}

df = pd.DataFrame(data)

print(df[df['age'] > 30])
print(df[df['salary'] > 60000])
print(df[df['salary'].between(50000, 70000)])
print(df[(df['age'] > 25) & (df['salary'] > 55000)])