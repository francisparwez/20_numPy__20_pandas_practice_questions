# 29. Clean categorical data
# Given:
#     city
#     -------
#     Karachi
#     karachi
#     KARACHI
#     Lahore
#     lahore
#     Islamabad
# Standardize the city names so that variations such as:
#     Karachi
#     karachi
#     KARACHI
# become:
#     Karachi
# Then calculate the number of customers per city.


import pandas as pd

# Sample data
data = {
    'city': ['Karachi', 'karachi', 'KARACHI', 'Lahore', 'lahore', 'Islamabad']
}

df = pd.DataFrame(data)

# Standardize city names by capitalizing the first letter and making the rest lowercase
df['city'] = df['city'].str.strip().str.capitalize()

# Calculate the number of customers per city
city_counts = df['city'].value_counts()

# Display the results
print(city_counts)

