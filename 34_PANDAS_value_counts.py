# 34. Value counts
# Given:
#     status
#     -------
#     Completed
#     Pending
#     Completed
#     Cancelled
#     Completed
#     Pending
# Calculate:
#     Number of orders per status
#     Percentage of orders per status
#     Then identify the most common status.

import pandas as pd

df = pd.DataFrame({    
    'status': ['Completed', 'Pending', 'Completed', 'Cancelled', 'Completed', 'Pending']
})

# Calculate the number of orders per status
count = df['status'].value_counts()

# Calculate the percentage of orders per status
# Setting normalize=True returns relative frequencies; multiplying by 100 turns them into percentages
percentage = df['status'].value_counts(normalize=True) * 100

# Combine the calculations into a single clean summary table
summary_df = pd.DataFrame({
    'Order Count': count,
    'Percentage (%)': round(percentage, 2)
})

# Identify the most common status
most_common_status = count.idxmax()

# Output the results
print("--- Frequency Table Summary ---")
print(summary_df)
print("\n--- Analytics Conclusion ---")
print(f"The most common status is: '{most_common_status}' with {count[most_common_status]} occurrences.")
