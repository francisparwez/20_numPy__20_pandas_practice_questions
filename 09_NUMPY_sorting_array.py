# Sort an array
# Given:
#     values = np.array([45, 12, 89, 23, 67, 34])
# Create:
#     Ascending version
#     Descending version
#     Then find the indexes that would sort the original array.
# Concepts: sort() , argsort() 

import numpy as np

values = np.array([45, 12, 89, 23, 67, 34])

print(f"Original: {values}")
print(f"Ascending: {np.sort(values)}")
print(f"Descending: {np.sort(values)[::-1]}")
print(f"Sort Indexes (Ascending): {np.argsort(values)}")
print(f"Sort Indexes (Descending): {np.argsort(values)[::-1]}")