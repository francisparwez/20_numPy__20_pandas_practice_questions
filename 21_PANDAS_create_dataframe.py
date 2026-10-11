# 21. Create a DataFrame
# Create:
    # data = {
    # "name": ["Alice", "Bob", "Charlie", "David"],
    # "age": [25, 30, 35, 28],
    # "salary": [50000, 60000, 75000, 55000]
    # }
# Create a DataFrame and display:
    # First 5 rows
    # Shape
    # Column names
    # Data types
    # Basic statistics


import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie", "David"],
    "age": [25, 30, 35, 28],
    "salary": [50000, 60000, 75000, 55000]
}

df = pd.DataFrame(data)

print(f"First 5 Rows:\n{df.head(5)}\n")
print(f"Shape: {df.shape}\n")
print(f"Columns: {df.columns}\n")
print(f"Data Types For Each Column:\n{df.dtypes}\n")
print(f"Basic Statistics:\n{df.describe()}")