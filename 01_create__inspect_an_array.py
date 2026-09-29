# Level N1 — NumPy Fundamentals
# 1. Create and inspect an array
# Given:
#     values = [10, 20, 30, 40, 50]
# Create a NumPy array and display:
#     The array
#     Number of dimensions
#     Number of elements
#     Data type
#     Shape
# Concepts: np.array() , .ndim , .size , .dtype , .shape

import numpy as np

values = [10, 20, 30, 40, 50]

arr_ = np.array(values)
print(arr_)
print(arr_.ndim)
print(arr_.size)
print(arr_.dtype)
print(arr_.shape)