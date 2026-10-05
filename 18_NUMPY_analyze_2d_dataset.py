# 18. Analyze a 2D dataset
# Given:
#     data = np.array([
#         [25, 50000, 3],
#         [32, 70000, 5],
#         [28, 60000, 4],
#         [45, 90000, 8],
#         [35, 75000, 6]
#     ])
# Columns represent:
#     Age | Salary | Experience
# Calculate:
#     Average age
#     Average salary
#     Average experience
#     Highest salary
#     Employee with the highest salary
#     Employees with salary > 65,000

import numpy as np

data = np.array([
    [25, 50000, 3],
    [32, 70000, 5],
    [28, 60000, 4],
    [45, 90000, 8],
    [35, 75000, 6]
])

avg_age = np.mean(data[:, 0])
avg_salary = np.mean(data[:, 1])
avg_experience = np.mean(data[:, 2])
max_salary = np.max(data[:, 1])
highest_paid_employee = data[np.argmax(data[:, 1])]
employees_with_salary_gt_65000 = data[data[:, 1] > 65000]


print(f"Average Ages: {avg_age}")
print(f"Average Salary: {avg_salary}")
print(f"Average Experience: {avg_experience}")
print(f"Max Salary: {max_salary}")
print(f"Employee With The Highest Salary:\n{highest_paid_employee}")
print(f"Employee With Salary > 65,000:\n{employees_with_salary_gt_65000}")


