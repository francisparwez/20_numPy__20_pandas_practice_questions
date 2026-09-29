# 2. Array arithmetic
# Given:
#     sales = np.array([100, 200, 300, 400, 500])
# Calculate:
#     Sales after a 10% increase
#     Sales after a 20% decrease
#     Sales multiplied by 2
# Do this using vectorized operations, not loops.

import numpy as np

sales = np.array([100, 200, 300, 400, 500])

increase_10_percent = sales + (sales * 0.1)
decrease_20_percent = sales - (sales * 0.2)
double_sales = sales * 2

print(f"{increase_10_percent}\n{decrease_20_percent}\n{double_sales}")