# NumPy — Level N2
# 6. Reshape data
# Given:
#     values = np.arange(1, 13)
# Convert it into:
#     4 rows × 3 columns
# Then convert it into:
#     3 rows × 4 columns
# Concepts: reshape() .

import numpy as np

values = np.arange(1, 13)
print("Original 1D array:\n", values)

shape_4x3 = np.reshape(values, (4, 3))
print("\nReshaped to 4x3:\n", shape_4x3)

shape_3x4 = np.reshape(values, (3, 4))
print("\nReshaped to 3x4:\n", shape_3x4)

