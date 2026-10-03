import numpy as np

scores = np.array([45, 67, 82, 34, 91, 55, 73])

scores = np.where(scores < 50 , 0, scores)
print(scores)

scores = np.where(scores > 80 , 100, scores)
print(scores)