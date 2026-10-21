# 30. Detect and handle outliers
# Given an employee salary column:
# 	salary = [40000, 45000, 50000, 52000, 55000, 60000, 65000, 500000]
# Using the IQR method:
# 	Calculate Q1
# 	Calculate Q3
# 	Calculate IQR
# 	Identify outliers
# 	Create a cleaned DataFrame without the outliers
# This connects your Python IQR → NumPy → Pandas skills.

import pandas as pd

salary = [40000, 45000, 50000, 52000, 55000, 60000, 65000, 500000]

df = pd.DataFrame({
    "salary": salary
})

# Calculate Q1 and Q3
q1 = df['salary'].quantile(0.25)
q3 = df['salary'].quantile(0.75)
iqr = q3 - q1

# Identify outliers
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
outliers = df[(df['salary'] < lower_bound) | (df['salary'] > upper_bound)]

# Create a cleaned DataFrame without the outliers
cleaned_df = df[~df.index.isin(outliers.index)]

# Print results
print("Original DataFrame:")
print(df)
print("\nQ1:", q1)
print("Q3:", q3)
print("IQR:", iqr)
print("\nLower Bound:", lower_bound)
print("Upper Bound:", upper_bound)
print("\nOutliers:")
print(outliers)
print("\nCleaned DataFrame:")
print(cleaned_df)
