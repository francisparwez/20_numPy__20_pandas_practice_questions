# 5. Basic statistics
# Given:
#     sales = np.array([120, 150, 200, 180, 300, 250, 170])
# Calculate:
#     Total
#     Mean
#     Minimum
#     Maximum
#     Standard deviation
#     Median
# Concepts: sum , mean , min , max , std , median

import numpy as np

sales = np.array([120, 150, 200, 180, 300, 250, 170])

sales_total = np.sum(sales)
sales_mean = np.mean(sales)
sales_min = np.min(sales)
sales_max = np.max(sales)
sales_std = np.std(sales)
sales_median = np.median(sales)

print(sales_total)
print(sales_min)
print(sales_max)
print(sales_std)
print(sales_median)
