# 22. Select columns
# Using the DataFrame in the earlier exercise, select:
#     Only name
#     Only salary
#     name and salary
#     age, salary
# Practice both:
#     df["salary"]
# and:
#     df[["name", "salary"]]

import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie", "David"],
    "age": [25, 30, 35, 28],
    "salary": [50000, 60000, 75000, 55000]
}

df = pd.DataFrame(data)

print(df['name'])
print(df['salary'])
print(df[['name', 'salary']])
print(df[['age', 'salary']])