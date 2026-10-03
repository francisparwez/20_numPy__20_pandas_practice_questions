# 11. Missing values
# Given:
#     temperatures = np.array([25, 27, np.nan, 30, 28, np.nan, 32])
# Calculate:
#     Mean ignoring missing values
#     Number of missing values
#     Replace missing values with the mean
# Concepts: np.isnan() , np.nanmean() 

import numpy as np

temperatures = np.array([25, 27, np.nan, 30, 28, np.nan, 32])

temperature_mean = np.nanmean(temperatures)
print(f"Temperature Mean: {temperature_mean}")

missing_values_count = np.sum(np.isnan(temperatures))
print(f"Number of Missing Values: {missing_values_count}")

clean_temperatures = temperatures.copy()
clean_temperatures[np.isnan(clean_temperatures)] = temperature_mean
print(f"Cleaned Temperatures: {clean_temperatures}")

