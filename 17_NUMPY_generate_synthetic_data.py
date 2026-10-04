# 17. Generate synthetic data
# Use NumPy to generate:
#     100 random ages between 18 and 60
#     100 random salaries between 30,000 and 150,000
#     100 random exam scores between 0 and 100
# Then calculate basic statistics for each.
#     Concepts: random data generation, reproducibility.

import numpy as np

np.random.seed(42)

ages = np.random.randint(18, 61, size=100)
salaries = np.random.randint(30000, 150001, size=100)
exam_scores = np.random.randint(0, 101, size=100)

def calculate_statistics(name, data_array):
    print(f"=== {name} Statistics ===")
    print(f"Mean:               {np.mean(data_array):.2f}")
    print(f"Median:             {np.median(data_array):.2f}")
    print(f"Minimum Value:      {np.min(data_array)}")
    print(f"Maximum Value:      {np.max(data_array)}")
    print(f"Standard Deviation: {np.std(data_array):.2f}")
    

print(f"Ages: {ages}")
calculate_statistics("Ages", ages)
print(f"Salaries: {salaries}")
calculate_statistics("Salaries", salaries)
print(f"Exam Scores: {exam_scores}")
calculate_statistics("Exam Scores", exam_scores)