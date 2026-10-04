# 15. Matrix operations
# Given:
#     A = np.array([
#     [1, 2],
#     [3, 4]
#     ])
#     B = np.array([
#     [5, 6],
#     [7, 8]
#     ])
# Calculate:
#     A + B
#     A - B
# Element-wise multiplication
# Matrix multiplication
# Transpose of A
# Concepts: matrix operations, .T , @

import numpy as np

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

print(f"A: \n{A}")
print(f"B: \n{B}")
print(f"A + B: \n{A + B}")
print(f"A - B: \n{A - B}")
print(f"A X B: \n{A * B}") # Element-Wise Multiplication
print(f"A @ B: \n{A @ B}") # Matrix Multiplication
print(f"Transpose Of A: \n{A.T}")