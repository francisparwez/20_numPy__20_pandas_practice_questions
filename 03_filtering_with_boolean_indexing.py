# 3. Filtering with Boolean indexing
# Given:
#     sales = np.array([120, 450, 230, 890, 340, 150, 720])
# Return:
#     Sales greater than 400
#     Sales less than 300
#     Sales between 200 and 700
# Concepts: Boolean masks, &, comparisons.

import numpy as np

sales = np.array([120, 450, 230, 890, 340, 150, 720])

sales_greater_than_400 = sales[sales > 400]
sales_less_than_300 = sales[sales < 300]
sales_between_200__700 = sales[(sales >= 200) & (sales <= 700)]

print(sales_greater_than_400)
print(sales_less_than_300)
print(sales_between_200__700)