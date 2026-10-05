# 19. Correlation
# Given:
#     experience = np.array([1, 2, 3, 4, 5, 6])
#     salary = np.array([30000, 35000, 40000, 48000, 55000, 65000])
# Calculate the correlation coefficient.
# Then determine whether the relationship is:
#     Positive
#     Negative
#     Approximately zero
# Concept: correlation and relationship analysis.

import numpy as np

experience = np.array([1, 2, 3, 4, 5, 6])
salary = np.array([30000, 35000, 40000, 48000, 55000, 65000])

correlation = np.corrcoef(experience, salary)[0, 1]

print(f"Correlation coefficient: {correlation:.2f}")

if correlation > 0:
    print("Relationship: Positive")
elif correlation < 0:
    print("Relationship: Negative")
else:
    print("Relationship: Approximately zero")