# 24. Sort data
# Sort employees by:
#     Salary ascending
#     Salary descending
#     Age descending
# Then sort by:
#     department ascending
#     salary descending
# Concept:
#     sort_values() 


import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie", "David"],
    "department": ["HR", "IT", "Finance", "IT"],
    "age": [25, 30, 35, 28],
    "salary": [50000, 60000, 75000, 55000]
}

df = pd.DataFrame(data)

print(f"Salary Ascending:\n{df.sort_values(by='salary', ascending=True)}")
print(f"Salary Descending:\n{df.sort_values(by='salary', ascending=False)}")
print(f"Age Descending:\n{df.sort_values(by='age', ascending=False)}")
print(
    f"Department Ascending & Salary Descending:\n"
    f"{df.sort_values(by=['department', 'salary'], ascending=[True, False])}"
)