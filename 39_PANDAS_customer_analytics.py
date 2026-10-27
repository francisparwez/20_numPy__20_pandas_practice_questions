# 39. Customer analytics
# Given:
#     customer_id
#     order_date
#     amount
# Calculate:
#     1. Total spending per customer
#     2. Average order value
#     3. Number of orders
#     4. Largest order
#     5. First order date
#     6. Last order date
#     7. Rank customers by spending
#     8. Customers whose spending is above the overall average
# 🔥 This is essentially a mini Data Analyst interview problem.


import pandas as pd

data = {
    'customer_id': [101, 102, 101, 103, 102, 101, 104, 103, 104],
    'order_date': pd.to_datetime(['2026-01-01', '2026-01-02', '2026-01-05', '2026-01-06', '2026-01-10', '2026-01-15', '2026-01-20', '2026-01-22', '2026-01-25']),
    'amount': [150.00, 80.50, 45.00, 300.00, 120.00, 200.00, 50.00, 150.00, 75.00]
}

df = pd.DataFrame(data)

customer_analytics = df.groupby('customer_id').agg(
    total_spending=('amount', 'sum'),
    average_order_value=('amount', 'mean'),
    number_of_orders=('amount', 'count'),
    largest_order=('amount', 'max'),
    first_order_date=('order_date', 'min'),
    last_order_date=('order_date', 'max')
).reset_index()

customer_analytics['spending_rank'] = customer_analytics['total_spending'].rank(ascending=False, method='min')

overall_avg_spending = customer_analytics['total_spending'].mean()
above_avg_customer = customer_analytics[customer_analytics['total_spending'] > overall_avg_spending]

print(customer_analytics)
print("\nCustomers spending above the average:")
print(above_avg_customer)