# 13. Standardization
# Given:
# values = np.array([10, 20, 30, 40, 50])
# Calculate the standardized values using:
# z = (x - u) / o
# Where:        
# u = mean
# o = standard deviation
# Concept: feature scaling.

import numpy as np

x = np.array([10, 20, 30, 40, 50])

u = np.mean(x)
o = np.std(x)

z = (x - u) / o

print(f"Original Values: {x}")
print(f"Standardized Values: {z}")
