# 35. Date/time analysis
# Given:
#     order_date
#     2026-01-05
#     2026-01-17
#     2026-02-03
#     2026-02-20
#     2026-03-10
# Convert the column to datetime.
# Create:
#     year
#     month
#     month_name
#     day
#     day_of_week
# Then calculate monthly order counts.
# 🔥 Very important Data Analyst skill

import pandas as pd

df = pd.DataFrame({
    'order_date': ['2026-01-05', '2026-01-17', '2026-02-03', '2026-02-20', '2026-03-10']
})

# Convert the column to datetime
df['order_date'] = pd.to_datetime(df['order_date'])

# Create new columns for year, month, month_name, day, and day_of_week
df['day'] = df['order_date'].dt.day
df['month'] = df['order_date'].dt.month
df['year'] = df['order_date'].dt.year
df['day_of_week'] = df['order_date'].dt.day_name()
df['month_name'] = df['order_date'].dt.month_name()

# Calculate monthly order counts
monthly_order_counts = (
    df.groupby(['month', 'month_name'])['order_date']
      .count()
      .reset_index(name='order_count')
      .sort_values('month')
      .set_index('month_name')['order_count']
)

print(df)
print("\nMonthly Order Counts:")
print(monthly_order_counts)
