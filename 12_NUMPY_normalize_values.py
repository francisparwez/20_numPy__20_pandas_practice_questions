# 12. Normalize values
# Given:
#   values = np.array([10, 20, 30, 40, 50])
# Perform Min-Max normalization:
#   x' = (x - min(x)) / (max(x) - min(x))
# Expected range:
#   0 → 1

import numpy as np

values = np.array([10, 20, 30, 40, 50])

min_ = np.min(values)
max_ = np.max(values)
min_max = (values - min_) / (max_ - min_)

print(min_max)