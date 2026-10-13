# 27. Remove duplicates
# Given customer data containing duplicate rows.
# Find:
#     Number of duplicate rows
#     Display duplicates
#     Remove duplicates
#     Verify the final number of rows
# Concepts:
#     duplicated(), drop_duplicates() 

import pandas as pd

# Sample customer data with duplicate rows
data = {
    "name": ["Alice", "Bob", "Alice", "Charlie", "Bob", "David"],
    "email": ["alice@email.com", "bob@email.com", "alice@email.com", "charlie@email.com", "bob@email.com", "david@email.com"]
}

df = pd.DataFrame(data)

print(f"Original number of rows: {len(df)}")
print(f"Number of Duplicate Rows found: {df.duplicated().sum()}")
print(f"Duplicate Rows:\n{df[df.duplicated()]}")

df = df.drop_duplicates()
print(f"Number of rows after removing duplicates: {len(df)}")