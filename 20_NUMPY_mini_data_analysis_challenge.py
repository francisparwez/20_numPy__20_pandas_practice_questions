
import numpy as np

# 1. Generate reproducible data
np.random.seed(42)

dataset = np.column_stack((
    np.arange(1, 101),                     # Customer ID
    np.random.randint(18, 99, size=100),    # Age
    np.random.randint(30000, 150001, 100),  # Annual income
    np.random.randint(1, 51, size=100),     # Number of purchases
    np.random.randint(5, 4501, size=100)    # Total spending
))

# Extract each column
customer_id, age, income, no_of_purchases, total_spending = dataset.T

# Verify dataset dimensions
print("Dataset shape:", dataset.shape)
print("Number of customers:", len(customer_id))

# 1. Average age
print("\n1. Average age:", np.mean(age))

# 2. Average income
print("2. Average income:", np.mean(income))

# 3. Average spending
average_spending = np.mean(total_spending)
print("3. Average spending:", average_spending)

# 4. Highest spender
highest_index = np.argmax(total_spending)
print("4. Highest spender ID:", customer_id[highest_index])
print("   Highest spending:", total_spending[highest_index])

# 5. Lowest spender
lowest_index = np.argmin(total_spending)
print("5. Lowest spender ID:", customer_id[lowest_index])
print("   Lowest spending:", total_spending[lowest_index])

# 6. Customers spending above average
above_average = total_spending > average_spending
print("6. Customer IDs spending above average:",
      customer_id[above_average])
print("   Their spending:", total_spending[above_average])

# 7. Customers with more than 10 purchases
frequent_customers = no_of_purchases > 10
print("7. Customer IDs with more than 10 purchases:",
      customer_id[frequent_customers])
print("   Their purchase counts:", no_of_purchases[frequent_customers])

# 8. Correlation between income and spending
correlation = np.corrcoef(income, total_spending)[0, 1]
print("8. Income-spending correlation:", round(correlation, 3))

# 9. Median spending
print("9. Median spending:", np.median(total_spending))

# 10. Number of unique age values
unique_ages = np.unique(age)
print("10. Number of unique age values:", len(unique_ages))
print("    Unique ages:", unique_ages)
