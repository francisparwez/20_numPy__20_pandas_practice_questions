# 28. Convert data types
# Given:
#     age = ["25", "30", "35", "40"]
#     salary = ["50000", "60000", "70000", "80000"]
# Convert them to numeric types.
# Then calculate:
#     Average age
#     Average salary

import pandas as pd

df = pd.DataFrame({
    "age": ["25", "30", "35", "40"],
    "salary": ["50000", "60000", "70000", "80000"]
})

# Convert age and salary to numeric types
df["age"] = pd.to_numeric(df["age"])
df["salary"] = pd.to_numeric(df["salary"])

# Calculate average age and salary
avg_age = df["age"].mean()
avg_salary = df["salary"].mean()

print(f"Average age: {avg_age}")
print(f"Average salary: {avg_salary}")