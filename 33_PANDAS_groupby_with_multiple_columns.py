# 33. GroupBy with multiple columns
# Given:
#     City
#     Product
#     Sales
# Calculate:
#     Total sales by city and product
# For example:
#     Karachi → Laptop → 500000
#     Karachi → Phone → 300000
#     Lahore → Laptop → 400000
# Concept: multi-level grouping.

import pandas as pd

df = pd.DataFrame({
    'City': ['Karachi', 'Karachi', 'Lahore', 'Lahore', 'Karachi', 'Lahore'],
    'Product': ['Laptop', 'Phone', 'Laptop', 'Phone', 'Laptop', 'Laptop'],
    'Sales': [500000, 300000, 400000, 200000, 500000, 400000]
})

result = (
    df.groupby(['City', 'Product'])['Sales']
      .sum()
      .reset_index(name='Total_Sales')
)

print(f"Original DataFrame:\n{df}\n")
print(f"Grouped DataFrame:\n{result}\n")