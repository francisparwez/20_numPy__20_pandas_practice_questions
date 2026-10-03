# 10. Remove duplicates
# Given:
#     customer_ids = np.array([101, 102, 101, 103, 104, 102, 105, 103])
# Return only unique customer IDs.
# Then determine how many unique customers exist.
# Concepts: np.unique() 

import numpy as np

customer_ids = np.array([101, 102, 101, 103, 104, 102, 105, 103])

print(f"Original Customer ID: {customer_ids}")

unique_customer_ids = np.unique(customer_ids)

print(f"Unique Customer ID: {unique_customer_ids}")
print(f"Number of Unique Customers: {len(unique_customer_ids)}")