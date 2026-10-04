# 16. Detect outliers with NumPy
# Given:
#     values = np.array([10, 12, 11, 13, 12, 15, 14, 100, 11, 13])
# Using the IQR method:
#     Calculate Q1
#     Calculate Q3
#     Calculate IQR
#     Calculate lower bound
#     Calculate upper bound
#     Return normal values
#     Return outliers
# This directly reinforces the IQR problem you've already done in native Python.

import numpy as np

values = np.array([10, 12, 11, 13, 12, 15, 14, 100, 11, 13])

print(f"Original Values: {values}")

q1 = np.percentile(values, 25)
print(f"Q1: {q1}")

q3 = np.percentile(values, 75)
print(f"Q3: {q3}")

iqr = q3 - q1
print(f"IQR: {iqr}")

lower_bound = q1 - (1.5 * iqr)
print(f"Lower Bound: {lower_bound}")

upper_bound = q3 + (1.5 * iqr)
print(f"Upper Bound: {upper_bound}")

# Use NumPy boolean indexing to filter for values that fall between or equal to the lower and upper bounds.
normal_values = values[(values >= lower_bound) & (values <= upper_bound)]
print(f"Normal Values: {normal_values}")

# Filter for values that fall outside the boundaries (either less than the 
# lower bound OR greater than the upper bound).
outliers = values[(values < lower_bound) | (values > upper_bound)]
print(f"Outliers: {outliers}")




