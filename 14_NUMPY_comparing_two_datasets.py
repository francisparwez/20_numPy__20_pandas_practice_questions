# 14. Compare two datasets
# Given:
#     actual = np.array([100, 120, 150, 200, 250])
#     predicted = np.array([110, 115, 145, 210, 240])
# Calculate:
#     Error for each prediction
#     Absolute error
#     Mean Absolute Error
# This introduces you to basic model evaluation.

import numpy as np

actual = np.array([100, 120, 150, 200, 250])
predicted = np.array([110, 115, 145, 210, 240])

error = predicted - actual
absolute_error = np.abs(error)
mae = int(np.mean(absolute_error))

print(f"Error: {error}")
print(f"Absolute Error: {absolute_error}")
print(f"Mean Absolute Error: {mae}")
