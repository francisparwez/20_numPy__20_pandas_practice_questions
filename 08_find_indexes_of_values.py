# 8. Find indexes of important values
# Given:
#     sales = np.array([120, 450, 230, 890, 340, 720])
# Find:
#     Index of the maximum value
#     Index of the minimum value
#     Indexes where sales are greater than 400
# Concepts: argmax() , argmin() , where() 

import numpy as np

sales = np.array([120, 450, 230, 890, 340, 720])

print(f"Index of the maximum value: {np.argmax(sales)}")
print(f"Index of the minimum value: {np.argmin(sales)}")
print(f"Indexes where sales are greater than 400: {np.where(sales > 400)}")