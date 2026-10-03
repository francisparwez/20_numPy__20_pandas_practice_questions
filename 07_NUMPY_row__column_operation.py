# 7. Row and column operations
# Given:
#     sales = np.array([
#     [100, 200, 300],
#     [150, 250, 350],
#     [200, 300, 400]
#     ])
# Calculate:
#     Total sales for each row
#     Total sales for each column
#     Average sales for each row
#     Average sales for each column
# Important concept: axis

import numpy as np

sales = np.array([
    [100, 200, 300],
    [150, 250, 350],
    [200, 300, 400]
])

print(f"Total sales for each row: {np.sum(sales, axis=1)}")
print(f"Total sales for each column: {np.sum(sales, axis=0)}")
print(f"Average sales for each row: {np.mean(sales, axis=1)}")
print(f"Average sales for each column: {np.mean(sales, axis=0)}")
