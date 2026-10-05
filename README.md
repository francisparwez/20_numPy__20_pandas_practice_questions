# NumPy & Pandas — 40 Practice Questions

A structured practice repository for building **NumPy and Pandas skills for Data Analysis and Data Science**.

The practice set contains **20 NumPy questions followed by 20 Pandas questions**, progressing from fundamentals to practical data-analysis challenges. The exercises are designed to reinforce analytical patterns across Python, SQL, NumPy, and Pandas rather than simply memorizing syntax.

---

## 🎯 Project Goal

The goal of this repository is to work through the practice questions **one problem at a time**, with each completed question stored as its own Python script.

The progression is:

```text
NumPy Fundamentals
        ↓
NumPy Data Analysis
        ↓
Pandas Fundamentals
        ↓
Pandas Data Cleaning
        ↓
Pandas Data Analysis
        ↓
Intermediate Analytics
```

The original practice set deliberately moves from basic numerical computation toward real-world data-analysis tasks such as filtering, aggregation, missing-value handling, date analysis, joins, rolling calculations, customer analytics, and an e-commerce analysis challenge.

---

# 📚 Practice Set

## 🔢 NumPy — 20 Questions

### Level N1 — NumPy Fundamentals

| #   | Practice Problem                | Main Concepts                                       | Status       |
| --- | ------------------------------- | --------------------------------------------------- | ------------ |
| 1   | Create and inspect an array     | `np.array()`, `.ndim`, `.size`, `.dtype`, `.shape`  | ✅ Completed |
| 2   | Array arithmetic                | Vectorized operations, percentage increase/decrease | ✅ Completed |
| 3   | Filtering with Boolean indexing | Boolean masks, comparisons, `&`                     | ✅ Completed |
| 4   | Replace values using conditions | `np.where()`                                        | ✅ Completed |
| 5   | Basic statistics                | `sum`, `mean`, `min`, `max`, `std`, `median`        | ✅ Completed |

### Level N2 — NumPy

| #   | Practice Problem                 | Main Concepts                     | Status       |
| --- | -------------------------------- | --------------------------------- | ------------ |
| 6   | Reshape data                     | `.reshape()`                      | ✅ Completed |
| 7   | Row and column operations        | `axis`                            | ✅ Completed |
| 8   | Find indexes of important values | `argmax()`, `argmin()`, `where()` | ✅ Completed |
| 9   | Sort an array                    | `sort()`, `argsort()`             | ✅ Completed |
| 10  | Remove duplicates                | `np.unique()`                     | ✅ Completed |

### Level N3 — NumPy Data Analysis

| #   | Practice Problem     | Main Concepts                                      | Status       |
| --- | -------------------- | -------------------------------------------------- | ------------ |
| 11  | Missing values       | `np.isnan()`, `np.nanmean()`                       | ✅ Completed |
| 12  | Normalize values     | Min-Max normalization, feature scaling             | ✅ Completed |
| 13  | Standardization      | Mean, standard deviation, z-score, feature scaling | ✅ Completed |
| 14  | Compare two datasets | Prediction error, absolute error, MAE              | ✅ Completed |
| 15  | Matrix operations    | Matrix arithmetic, `.T`, `@`                       | ✅ Completed |

### Level N4 — Practical Data Science

| #   | Practice Problem                   | Main Concepts                                          | Status       |
| --- | ---------------------------------- | ------------------------------------------------------ | ------------ |
| 16  | Detect outliers with NumPy         | IQR, Q1, Q3, bounds, outliers                          | ✅ Completed |
| 17  | Generate synthetic data            | Random data generation, reproducibility                | ✅ Completed |
| 18  | Analyze a 2D dataset               | 2D arrays, column analysis, filtering                  | ✅ Completed |
| 19  | Correlation                        | Correlation coefficient, relationship analysis         | ✅ Completed |
| 20  | NumPy mini data-analysis challenge | Customer analytics, statistics, filtering, correlation | ⬜ Pending   |

---

# 🐼 Pandas — 20 Questions

The Pandas section begins after the NumPy exercises and moves from DataFrame fundamentals into data cleaning, aggregation, joins, time-series calculations, and customer/e-commerce analysis.

## Level P1 — Pandas Fundamentals

| #   | Practice Problem          | Main Concepts                                                 | Status     |
| --- | ------------------------- | ------------------------------------------------------------- | ---------- |
| 21  | Create a DataFrame        | `DataFrame`, `head()`, `shape`, columns, `dtypes`, statistics | ⬜ Pending |
| 22  | Select columns            | `df["column"]`, `df[[...]]`                                   | ⬜ Pending |
| 23  | Filter rows               | Boolean filtering, multiple conditions                        | ⬜ Pending |
| 24  | Sort data                 | `sort_values()`                                               | ⬜ Pending |
| 25  | Create calculated columns | Vectorized column operations                                  | ⬜ Pending |

## Level P2 — Pandas Data Cleaning

| #   | Practice Problem           | Main Concepts                              | Status     |
| --- | -------------------------- | ------------------------------------------ | ---------- |
| 26  | Handle missing values      | Missing-value detection, median imputation | ⬜ Pending |
| 27  | Remove duplicates          | `duplicated()`, `drop_duplicates()`        | ⬜ Pending |
| 28  | Convert data types         | Numeric conversion, type handling          | ⬜ Pending |
| 29  | Clean categorical data     | String standardization, grouping           | ⬜ Pending |
| 30  | Detect and handle outliers | IQR, filtering, cleaned DataFrame          | ⬜ Pending |

## Level P3 — Pandas Data Analysis

| #   | Practice Problem              | Main Concepts                         | Status     |
| --- | ----------------------------- | ------------------------------------- | ---------- |
| 31  | GroupBy analysis              | `groupby()`                           | ⬜ Pending |
| 32  | Multiple aggregations         | `.agg()`                              | ⬜ Pending |
| 33  | GroupBy with multiple columns | Multi-level grouping                  | ⬜ Pending |
| 34  | Value counts                  | `value_counts()`, percentages         | ⬜ Pending |
| 35  | Date/time analysis            | `datetime`, year, month, day, weekday | ⬜ Pending |

## Level P4 — Intermediate Analytics

| #   | Practice Problem                 | Main Concepts                                            | Status     |
| --- | -------------------------------- | -------------------------------------------------------- | ---------- |
| 36  | Merge two DataFrames             | `merge()`, SQL JOIN equivalent                           | ⬜ Pending |
| 37  | Find customers with no orders    | LEFT JOIN equivalent, `indicator=True`                   | ⬜ Pending |
| 38  | Running total and moving average | `.cumsum()`, `.rolling()`                                | ⬜ Pending |
| 39  | Customer analytics               | Aggregation, ranking, customer metrics                   | ⬜ Pending |
| 40  | Pandas mini e-commerce analysis  | KPIs, customers, products, geography, time, data quality | ⬜ Pending |

---

# ✅ Completed Solutions

## 01 — Create and Inspect an Array

**File:**

```text
01_create__inspect_an_array.py
```

### Problem

Given:

```python
values = [10, 20, 30, 40, 50]
```

Create a NumPy array and display:

- The array
- Number of dimensions
- Number of elements
- Data type
- Shape

### Concepts Practiced

```text
np.array()
.ndim
.size
.dtype
.shape
```

### Solution

```python
import numpy as np

values = [10, 20, 30, 40, 50]

arr_ = np.array(values)

print(arr_)
print(arr_.ndim)
print(arr_.size)
print(arr_.dtype)
print(arr_.shape)
```

### What This Solution Demonstrates

The Python list is converted into a NumPy array using `np.array()`.

The resulting array is then inspected using NumPy's basic array attributes:

| Attribute    | Purpose                               |
| ------------ | ------------------------------------- |
| `arr_.ndim`  | Returns the number of dimensions      |
| `arr_.size`  | Returns the total number of elements  |
| `arr_.dtype` | Returns the data type of the elements |
| `arr_.shape` | Returns the dimensions of the array   |

This first exercise establishes the basic pattern of **creating and inspecting NumPy arrays**, which is used throughout the remaining NumPy exercises.

---

## 02 — Array Arithmetic

**File:**

```text
02_array_arithmetic.py
```

### Problem

Given:

```python
sales = np.array([100, 200, 300, 400, 500])
```

Calculate:

- Sales after a **10% increase**
- Sales after a **20% decrease**
- Sales **multiplied by 2**
- Use **vectorized operations rather than loops**

### Concepts Practiced

```text
NumPy arrays
Vectorized arithmetic
Element-wise multiplication
Percentage calculations
```

### Solution

```python
import numpy as np

sales = np.array([100, 200, 300, 400, 500])

increase_10_percent = sales + (sales * 0.1)
decrease_20_percent = sales - (sales * 0.2)
double_sales = sales * 2

print(f"{increase_10_percent}\n{decrease_20_percent}\n{double_sales}")
```

### What This Solution Demonstrates

The calculations are performed directly on the NumPy array without using a loop.

For the **10% increase**:

```python
sales + (sales * 0.1)
```

This adds 10% of each original value back to the original sales.

For the **20% decrease**:

```python
sales - (sales * 0.2)
```

This subtracts 20% of each original value from the original sales.

For **doubling the sales**:

```python
sales * 2
```

NumPy applies these operations element-by-element across the entire array.

### Expected Results

```text
10% increase:
[110. 220. 330. 440. 550.]

20% decrease:
[ 80. 160. 240. 320. 400.]

Sales multiplied by 2:
[ 200  400  600  800 1000]
```

This exercise reinforces the idea of **vectorization**: performing an operation on an entire NumPy array instead of manually processing each element with a loop.

---

## 03 — Filtering with Boolean Indexing

**File:**

```text
03_filtering_with_boolean_indexing.py
```

### Problem

Given:

```python
sales = np.array([120, 450, 230, 890, 340, 150, 720])
```

Return:

- Sales greater than 400
- Sales less than 300
- Sales between 200 and 700

### Concepts Practiced

```text
Boolean masks
Comparisons
&
Boolean indexing
```

### Solution

```python
import numpy as np

sales = np.array([120, 450, 230, 890, 340, 150, 720])

sales_greater_than_400 = sales[sales > 400]
sales_less_than_300 = sales[sales < 300]
sales_between_200__700 = sales[(sales >= 200) & (sales <= 700)]

print(sales_greater_than_400)
print(sales_less_than_300)
print(sales_between_200__700)
```

### What This Solution Demonstrates

The solution uses **Boolean indexing** to filter elements from a NumPy array based on conditions.

For sales greater than 400:

```python
sales[sales > 400]
```

NumPy creates a Boolean mask where each element is checked against the condition `sales > 400`, then returns only the values where the condition is `True`.

For sales less than 300:

```python
sales[sales < 300]
```

This returns only the values that satisfy the condition.

For values between 200 and 700:

```python
sales[(sales >= 200) & (sales <= 700)]
```

Two conditions are combined using `&` (**AND**). A value is included only when it is both greater than or equal to 200 and less than or equal to 700.

### Expected Results

```text
Sales greater than 400:
[450 890 720]

Sales less than 300:
[120 230 150]

Sales between 200 and 700:
[450 230 340]
```

This exercise reinforces **Boolean masks and conditional filtering**, which are fundamental techniques for working with NumPy arrays and later with Pandas DataFrames.

---

## 04 — Replace Values Using Conditions

**File:**

```text
04_replace_values_using_conditions.py
```

### Problem

Given:

```python
scores = np.array([45, 67, 82, 34, 91, 55, 73])
```

Replace:

- Scores below **50** with `0`
- Scores above **80** with `100`

### Concepts Practiced

```text
np.where()
Conditional value replacement
Applying conditions to NumPy arrays
```

### Solution

```python
import numpy as np

scores = np.array([45, 67, 82, 34, 91, 55, 73])

scores = np.where(scores < 50, 0, scores)
print(scores)

scores = np.where(scores > 80, 100, scores)
print(scores)
```

### What This Solution Demonstrates

The solution uses `np.where()` to replace values in a NumPy array when a condition is satisfied.

For scores below 50:

```python
scores = np.where(scores < 50, 0, scores)
```

Any score below 50 is replaced with `0`. Values that do not satisfy the condition remain unchanged.

For scores above 80:

```python
scores = np.where(scores > 80, 100, scores)
```

Any score above 80 is replaced with `100`. Other values remain unchanged.

The two conditions are applied sequentially to the same array.

### Expected Results

After replacing scores below 50:

```text
[ 0 67 82  0 91 55 73]
```

After also replacing scores above 80:

```text
[  0  67 100   0 100  55  73]
```

This exercise reinforces **conditional value replacement with `np.where()`**, an important NumPy technique for transforming data based on rules.

## 05 — Basic Statistics

**File:**

```text
05_basic_statistics.py
```

### Problem

Given:

```python
sales = np.array([120, 150, 200, 180, 300, 250, 170])
```

Calculate:

- Total
- Mean
- Minimum
- Maximum
- Standard deviation
- Median

### Concepts Practiced

```text
sum()
mean()
min()
max()
std()
median()
```

### Solution

```python
import numpy as np

sales = np.array([120, 150, 200, 180, 300, 250, 170])

sales_total = np.sum(sales)
sales_mean = np.mean(sales)
sales_min = np.min(sales)
sales_max = np.max(sales)
sales_std = np.std(sales)
sales_median = np.median(sales)

print(sales_total)
print(sales_min)
print(sales_max)
print(sales_std)
print(sales_median)
```

### What This Solution Demonstrates

The solution uses NumPy's built-in statistical functions to calculate common descriptive statistics from the sales array.

- `np.sum()` calculates the total of all sales values.
- `np.mean()` calculates the arithmetic mean.
- `np.min()` finds the smallest value.
- `np.max()` finds the largest value.
- `np.std()` calculates the standard deviation.
- `np.median()` finds the middle value after ordering the data.

The solution focuses on applying NumPy's statistical functions directly to the array.

### Expected Results

```text
Total:
1370

Mean:
195.71428571428572

Minimum:
120

Maximum:
300

Standard deviation:
55.636...

Median:
180.0
```

This exercise reinforces **basic descriptive statistics with NumPy**, which are fundamental for exploratory data analysis.

## 06 — Reshape Data

**File:**

```text
06_reshape_data.py
```

### Problem

Given:

```python
values = np.arange(1, 13)
```

Convert it into **4 rows × 3 columns**, then into **3 rows × 4 columns**.

### Concepts Practiced

```text
np.arange()
np.reshape()
Array dimensions
```

### Solution

```python
# NumPy — Level N2
# 6. Reshape data
# Given:
#     values = np.arange(1, 13)
# Convert it into:
#     4 rows × 3 columns
# Then convert it into:
#     3 rows × 4 columns
# Concepts: reshape() .

import numpy as np

values = np.arange(1, 13)
print("Original 1D array:\n", values)

shape_4x3 = np.reshape(values, (4, 3))
print("\nReshaped to 4x3:\n", shape_4x3)

shape_3x4 = np.reshape(values, (3, 4))
print("\nReshaped to 3x4:\n", shape_3x4)
```

### What This Solution Demonstrates

The solution creates a 1D NumPy array containing 1 through 12, then reshapes the same 12 elements into two different two-dimensional structures. `np.reshape(values, (4, 3))` creates a 4 × 3 array, while `np.reshape(values, (3, 4))` creates a 3 × 4 array. The values remain the same; only their arrangement changes.

### Expected Results

```text
Original 1D array:
[ 1  2  3  4  5  6  7  8  9 10 11 12]

Reshaped to 4x3:
[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]]

Reshaped to 3x4:
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
```

This exercise reinforces array reshaping and dimensional thinking.

---

## 07 — Row and Column Operations

**File:**

```text
07_row__column_operation.py
```

### Problem

Given:

```python
sales = np.array([
    [100, 200, 300],
    [150, 250, 350],
    [200, 300, 400]
])
```

Calculate:

- Total sales for each row
- Total sales for each column
- Average sales for each row
- Average sales for each column

**Important concept:** `axis`

### Concepts Practiced

```text
np.sum()
np.mean()
axis=0
axis=1
Row operations
Column operations
```

### Solution

```python
# 7. Row and column operations
# Given:
#     sales = np.array([
#     [100, 200, 300],
#     [150, 250, 350],
#     [200, 300, 400]
#     ])
# Calculate:
#     Total sales for each row
#     Total sales for each column
#     Average sales for each row
#     Average sales for each column
# Important concept: axis

import numpy as np

sales = np.array([
    [100, 200, 300],
    [150, 250, 350],
    [200, 300, 400]
])

print(f"Total sales for each row: {np.sum(sales, axis=1)}")
print(f"Total sales for each column: {np.sum(sales, axis=0)}")
print(f"Average sales for each row: {np.mean(sales, axis=1)}")
print(f"Average sales for each column: {np.mean(sales, axis=0)}")
```

### What This Solution Demonstrates

The solution uses NumPy's `axis` parameter to perform calculations across rows and columns.

For row-wise calculations, `axis=1` calculates across each row and produces one result for every row. For column-wise calculations, `axis=0` calculates down each column and produces one result for every column.

The same `axis` concept is used with both `np.sum()` and `np.mean()`.

### Expected Results

```text
Total sales for each row: [600 750 900]
Total sales for each column: [450 750 1050]
Average sales for each row: [200. 250. 300.]
Average sales for each column: [150. 250. 350.]
```

This exercise reinforces the important NumPy concept of **`axis`**, which is essential when performing calculations on multidimensional arrays.

---

## 08 — Find Indexes of Important Values

**File:**

```text
08_find_indexes_of_important_values.py
```

### Problem

Given:

```python
sales = np.array([120, 450, 230, 890, 340, 720])
```

Find:

- Index of the maximum value
- Index of the minimum value
- Indexes where sales are greater than 400

### Concepts Practiced

```text
np.argmax()
np.argmin()
np.where()
Finding indexes
```

### Solution

```python
import numpy as np

sales = np.array([120, 450, 230, 890, 340, 720])

print(f"Index of the maximum value: {np.argmax(sales)}")
print(f"Index of the minimum value: {np.argmin(sales)}")
print(f"Indexes where sales are greater than 400: {np.where(sales > 400)}")
```

### What This Solution Demonstrates

The solution uses NumPy index-finding functions to locate important values in the sales array.

- `np.argmax()` returns the index of the maximum value.
- `np.argmin()` returns the index of the minimum value.
- `np.where()` returns the indexes where a condition is `True`.

For this array:

```text
Maximum value: 890 → index 3
Minimum value: 120 → index 0
Sales greater than 400 → indexes [1, 3, 5]
```

### Expected Results

```text
Index of the maximum value: 3
Index of the minimum value: 0
Indexes where sales are greater than 400: (array([1, 3, 5]),)
```

This exercise reinforces the difference between **finding values** and **finding their positions (indexes)**, which is useful when analyzing NumPy arrays.

---

---

## 09 — Sort an Array

**File:**

```text
09_sort_an_array.py
```

### Problem

Given:

```python
values = np.array([45, 12, 89, 23, 67, 34])
```

Create:

- An ascending version
- A descending version
- The indexes that would sort the original array

### Concepts Practiced

```text
np.sort()
np.argsort()
Array slicing with [::-1]
Sorting values
Finding sorting indexes
```

### Solution

```python
import numpy as np

values = np.array([45, 12, 89, 23, 67, 34])

print(f"Original: {values}")
print(f"Ascending: {np.sort(values)}")
print(f"Descending: {np.sort(values)[::-1]}")
print(f"Sort Indexes (Ascending): {np.argsort(values)}")
print(f"Sort Indexes (Descending): {np.argsort(values)[::-1]}")
```

### What This Solution Demonstrates

The solution uses NumPy sorting functions to sort values and identify the indexes that would produce the sorted order.

- `np.sort()` returns a sorted copy of the array.
- `[::-1]` reverses the sorted array to produce descending order.
- `np.argsort()` returns the indexes that would sort the array.
- Reversing `np.argsort()` produces the descending sort indexes.

### Expected Results

```text
Original: [45 12 89 23 67 34]
Ascending: [12 23 34 45 67 89]
Descending: [89 67 45 34 23 12]
Sort Indexes (Ascending): [1 3 5 0 4 2]
Sort Indexes (Descending): [2 4 0 5 3 1]
```

This exercise reinforces the difference between **sorting values** and **finding the positions that define the sorted order**.

---

## 10 — Remove Duplicates

**File:**

```text
10_remove_duplicates.py
```

### Problem

Given:

```python
customer_ids = np.array([101, 102, 101, 103, 104, 102, 105, 103])
```

Return only the unique customer IDs and determine how many unique customers exist.

### Concepts Practiced

```text
np.unique()
Finding unique values
Counting unique values
```

### Solution

```python
import numpy as np

customer_ids = np.array([101, 102, 101, 103, 104, 102, 105, 103])

print(f"Original Customer ID: {customer_ids}")

unique_customer_ids = np.unique(customer_ids)

print(f"Unique Customer ID: {unique_customer_ids}")
print(f"Number of Unique Customers: {len(unique_customer_ids)}")
```

### What This Solution Demonstrates

The solution uses `np.unique()` to remove duplicate customer IDs and return each customer ID only once.

The resulting unique array is then reused to calculate the number of unique customers with `len()`.

### Expected Results

```text
Original Customer ID: [101 102 101 103 104 102 105 103]
Unique Customer ID: [101 102 103 104 105]
Number of Unique Customers: 5
```

This exercise reinforces a common data-analysis task: identifying distinct entities in a dataset and determining how many unique entities are present.

## 12 — Normalize Values

**File:**

```text
12_normalize_values.py
```

### Problem

Given:

```python
values = np.array([10, 20, 30, 40, 50])
```

Perform Min-Max normalization using:

```text
x' = (x - min(x)) / (max(x) - min(x))
```

The expected normalized range is **0 → 1**.

### Concepts Practiced

```text
np.min()
np.max()
Min-Max normalization
Feature scaling
Vectorized NumPy operations
```

### Solution

```python
import numpy as np

values = np.array([10, 20, 30, 40, 50])

min_ = np.min(values)
max_ = np.max(values)
min_max = (values - min_) / (max_ - min_)

print(min_max)
```

### What This Solution Demonstrates

The solution calculates the minimum and maximum values of the array, then applies the Min-Max normalization formula directly to the entire NumPy array.

For this dataset:

```text
Minimum = 10
Maximum = 50
```

The normalized values are calculated as:

```text
(10 - 10) / (50 - 10) = 0
(20 - 10) / (50 - 10) = 0.25
(30 - 10) / (50 - 10) = 0.50
(40 - 10) / (50 - 10) = 0.75
(50 - 10) / (50 - 10) = 1
```

This demonstrates how NumPy can apply a feature-scaling formula element-by-element without using a loop.

### Expected Results

```text
[0.   0.25 0.5  0.75 1.  ]
```

This exercise introduces **Min-Max normalization**, a common feature-scaling technique used to transform numerical values into a defined range.

## 13 — Standardization

**File:**

```text
13_standardization.py
```

### Problem

Given:

```python
values = np.array([10, 20, 30, 40, 50])
```

Calculate the standardized values using:

```text
z = (x - μ) / σ
```

Where:

```text
μ = mean
σ = standard deviation
```

### Concepts Practiced

```text
np.mean()
np.std()
Z-score standardization
Feature scaling
Vectorized NumPy operations
```

### Solution

```python
import numpy as np

x = np.array([10, 20, 30, 40, 50])

u = np.mean(x)
o = np.std(x)

z = (x - u) / o

print(f"Original Values: {x}")
print(f"Standardized Values: {z}")
```

### What This Solution Demonstrates

The solution calculates the mean and standard deviation of the array, then applies z-score standardization to each value.

For this dataset:

```text
Mean = 30
Standard deviation ≈ 14.1421
```

The standardized values represent how many standard deviations each value is away from the mean.

### Expected Results

```text
Original Values: [10 20 30 40 50]
Standardized Values: [-1.41421356 -0.70710678  0.  0.70710678  1.41421356]
```

This exercise introduces **standardization (z-score scaling)**, which transforms values so that the resulting data has a mean of approximately 0 and a standard deviation of 1.

## 14 — Compare Two Datasets

**File:**

```text
14_comparing_two_datasets.py
```

### Problem

Given:

```python
actual = np.array([100, 120, 150, 200, 250])
predicted = np.array([110, 115, 145, 210, 240])
```

Calculate:

- Error for each prediction
- Absolute error
- Mean Absolute Error (MAE)

This exercise introduces basic model evaluation.

### Concepts Practiced

```text
Prediction error
Signed error
Absolute error
Mean Absolute Error (MAE)
np.abs()
np.mean()
```

### Solution

```python
import numpy as np

actual = np.array([100, 120, 150, 200, 250])
predicted = np.array([110, 115, 145, 210, 240])

error = predicted - actual
absolute_error = np.abs(error)
mae = np.mean(absolute_error)

print(f"Error: {error}")
print(f"Absolute Error: {absolute_error}")
print(f"Mean Absolute Error: {mae}")
```

### What This Solution Demonstrates

The solution compares predicted values against actual values to measure prediction error.

For the **error for each prediction**:

```python
error = predicted - actual
```

This produces signed errors, showing whether each prediction is above or below the actual value.

For the **absolute error**:

```python
absolute_error = np.abs(error)
```

This removes the sign from each error so that only the magnitude of the error remains.

For **Mean Absolute Error (MAE)**:

```python
mae = np.mean(absolute_error)
```

This calculates the average of all absolute errors.

### Expected Results

```text
Error:
[ 10  -5  -5  10 -10]

Absolute Error:
[10  5  5 10 10]

Mean Absolute Error:
8.0
```

This exercise introduces a basic **model evaluation metric**, Mean Absolute Error, which measures the average magnitude of prediction errors.

---

## 15 — Matrix Operations

**File:**

```text
15_matrix_operations.py
```

### Problem

Given:

```python
A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])
```

Calculate:

- `A + B`
- `A - B`
- Element-wise multiplication
- Matrix multiplication
- Transpose of `A`

### Concepts Practiced

```text
Matrix arithmetic
Element-wise operations
Matrix multiplication
Transpose
.T
@
```

### Solution

```python
import numpy as np

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

print(f"A: \n{A}")
print(f"B: \n{B}")
print(f"A + B: \n{A + B}")
print(f"A - B: \n{A - B}")
print(f"A @ B: \n{A @ B}")
print(f"A X B: \n{A * B}")
print(f"Transpose Of A: \n{A.T}")
```

### What This Solution Demonstrates

The solution performs several common matrix operations using NumPy.

For **matrix addition**:

```python
A + B
```

NumPy adds corresponding elements from the two matrices.

For **matrix subtraction**:

```python
A - B
```

NumPy subtracts corresponding elements from `B` from `A`.

For **element-wise multiplication**:

```python
A * B
```

Each element in `A` is multiplied by the corresponding element in `B`.

For **matrix multiplication**:

```python
A @ B
```

The `@` operator performs matrix multiplication, where each result is calculated from a row of `A` and a column of `B`.

For the **transpose**:

```python
A.T
```

The rows of `A` become columns and the columns become rows.

### Expected Results

```text
A:
[[1 2]
 [3 4]]

B:
[[5 6]
 [7 8]]

A + B:
[[ 6  8]
 [10 12]]

A - B:
[[-4 -4]
 [-4 -4]]

A @ B:
[[19 22]
 [43 50]]

A X B:
[[ 5 12]
 [21 32]]

Transpose Of A:
[[1 3]
 [2 4]]
```

This exercise reinforces the important distinction between **element-wise multiplication (`*`)** and **matrix multiplication (`@`)**, as well as the use of `.T` for transposing a matrix.

## 16 — Detect Outliers with NumPy

**File:**

```text
16_detect_outliers_with_numpy.py
```

### Problem

Given:

```python
values = np.array([10, 12, 11, 13, 12, 15, 14, 100, 11, 13])
```

Using the IQR method, calculate:

- Q1
- Q3
- IQR
- Lower bound
- Upper bound
- Normal values
- Outliers

### Concepts Practiced

```text
np.percentile()
Interquartile Range (IQR)
Q1 and Q3
Lower and upper bounds
NumPy Boolean indexing
Outlier detection
```

### Solution

```python
import numpy as np

values = np.array([10, 12, 11, 13, 12, 15, 14, 100, 11, 13])

print(f"Original Values: {values}")

q1 = np.percentile(values, 25)
print(f"Q1: {q1}")

q3 = np.percentile(values, 75)
print(f"Q3: {q3}")

iqr = q3 - q1
print(f"IQR: {iqr}")

lower_bound = q1 - (1.5 * iqr)
print(f"Lower Bound: {lower_bound}")

upper_bound = q3 + (1.5 * iqr)
print(f"Upper Bound: {upper_bound}")

normal_values = values[(values >= lower_bound) & (values <= upper_bound)]
print(f"Normal Values: {normal_values}")

outliers = values[(values < lower_bound) | (values > upper_bound)]
print(f"Outliers: {outliers}")
```

### What This Solution Demonstrates

The solution applies the **IQR method** to identify values that fall outside the expected range of the dataset.

First, `np.percentile()` calculates the first and third quartiles:

```python
q1 = np.percentile(values, 25)
q3 = np.percentile(values, 75)
```

The interquartile range is then calculated as:

```python
iqr = q3 - q1
```

The lower and upper bounds are calculated using the standard IQR rule:

```text
Lower Bound = Q1 - 1.5 × IQR
Upper Bound = Q3 + 1.5 × IQR
```

Boolean indexing is then used to separate values inside the bounds from values outside them.

### Expected Results

```text
Q1: 11.0
Q3: 14.0
IQR: 3.0
Lower Bound: 6.5
Upper Bound: 18.5

Normal Values: [10 12 11 13 12 15 14 11 13]
Outliers: [100]
```

The value **100** is identified as an outlier because it is greater than the upper bound of `18.5`.

This exercise reinforces **IQR-based outlier detection** and combines percentile calculations with NumPy Boolean indexing.

---

## 17 — Generate Synthetic Data

**File:**

```text
17_generate_synthetic_data.py
```

### Problem

Use NumPy to generate:

- 100 random ages between **18 and 60**
- 100 random salaries between **30,000 and 150,000**
- 100 random exam scores between **0 and 100**

Then calculate basic statistics for each dataset.

**Concepts:** random data generation, reproducibility.

### Concepts Practiced

```text
np.random.seed()
np.random.randint()
Random data generation
Reproducibility
np.mean()
np.median()
np.min()
np.max()
np.std()
Reusable functions
```

### Solution

```python
import numpy as np

np.random.seed(42)

ages = np.random.randint(18, 61, size=100)
salaries = np.random.randint(30000, 150001, size=100)
exam_scores = np.random.randint(0, 101, size=100)

def calculate_statistics(name, data_array):
    print(f"=== {name} Statistics ===")
    print(f"Mean:               {np.mean(data_array):.2f}")
    print(f"Median:             {np.median(data_array):.2f}")
    print(f"Minimum Value:      {np.min(data_array)}")
    print(f"Maximum Value:      {np.max(data_array)}")
    print(f"Standard Deviation: {np.std(data_array):.2f}")


print(f"Ages: {ages}")
calculate_statistics("Ages", ages)
print(f"Salaries: {salaries}")
calculate_statistics("Salaries", salaries)
print(f"Exam Scores: {exam_scores}")
calculate_statistics("Exam Scores", exam_scores)
```

### What This Solution Demonstrates

The solution uses NumPy's random-number generation functions to create three synthetic datasets, each containing 100 values.

`np.random.seed(42)` makes the random generation **reproducible**. Running the program again with the same seed produces the same generated values, which is useful when testing, debugging, and comparing analysis results.

The `np.random.randint()` calls generate integer values within the required ranges. Because the upper bound is exclusive, the code correctly uses `61`, `150001`, and `101` to include 60, 150,000, and 100 respectively.

The `calculate_statistics()` function avoids repeating the same statistical calculation code for each dataset. For every dataset, it calculates the mean, median, minimum, maximum, and standard deviation.

This exercise reinforces the workflow of **generating reproducible synthetic data → calculating descriptive statistics → reusing a function across multiple datasets**.

---

## 18 — Analyze a 2D Dataset

**File:**

```text
18_analyze_2d_dataset.py
```

### Problem

Given:

```python
data = np.array([
    [25, 50000, 3],
    [32, 70000, 5],
    [28, 60000, 4],
    [45, 90000, 8],
    [35, 75000, 6]
])
```

Columns represent:

```text
Age | Salary | Experience
```

Calculate:

- Average age
- Average salary
- Average experience
- Highest salary
- Employee with the highest salary
- Employees with salary > 65,000

### Concepts Practiced

```text
2D NumPy arrays
Column selection
np.mean()
np.max()
np.argmax()
Boolean indexing
Conditional filtering
```

### Solution

```python
import numpy as np

data = np.array([
    [25, 50000, 3],
    [32, 70000, 5],
    [28, 60000, 4],
    [45, 90000, 8],
    [35, 75000, 6]
])

avg_ages = np.mean(data[:, 0])
avg_salary = np.mean(data[:, 1])
avg_experience = np.mean(data[:, 2])
max_salary = np.max(data[:, 1])
highest_paid_employee = data[np.argmax(data[:, 1])]
employees_with_salary_gt_65000 = data[data[:, 1] > 65000]


print(f"Average Ages: {avg_ages}")
print(f"Average Salary: {avg_salary}")
print(f"Average Experience: {avg_experience}")
print(f"Max Salary: {max_salary}")
print(f"Employee With The Highest Salary:\n{highest_paid_employee}")
print(f"Employee With Salary > 65,000:\n{employees_with_salary_gt_65000}")
```

### What This Solution Demonstrates

The solution treats the NumPy array as a small employee dataset and analyzes each column separately.

Column selection is performed using `data[:, 0]`, `data[:, 1]`, and `data[:, 2]` for Age, Salary, and Experience respectively. `np.mean()` calculates averages, while `np.max()` identifies the highest salary.

To retrieve the complete employee row associated with the highest salary, `np.argmax()` is combined with NumPy indexing. Boolean indexing filters employees whose salary is greater than 65,000.

### Expected Results

```text
Average Ages: 33.0
Average Salary: 69000.0
Average Experience: 5.2
Max Salary: 90000
Employee With The Highest Salary:
[   45 90000     8]
Employee With Salary > 65,000:
[[   32 70000     5]
 [   45 90000     8]
 [   35 75000     6]]
```

This exercise reinforces **2D array column analysis, aggregation, index finding, and Boolean filtering**.

## 19 — Correlation

**File:**

```text
19_NUMPY_correlation.py
```

### Problem

Given:

```python
experience = np.array([1, 2, 3, 4, 5, 6])
salary = np.array([30000, 35000, 40000, 48000, 55000, 65000])
```

Calculate the correlation coefficient and determine whether the relationship is:

- Positive
- Negative
- Approximately zero

### Concepts Practiced

```text
np.corrcoef()
Correlation coefficient
Relationship analysis
Array indexing
Conditional logic
```

### Solution

```python
import numpy as np

experience = np.array([1, 2, 3, 4, 5, 6])
salary = np.array([30000, 35000, 40000, 48000, 55000, 65000])

correlation = np.corrcoef(experience, salary)[0, 1]

print(f"Correlation coefficient: {correlation:.2f}")

if correlation > 0:
    print("Relationship: Positive")
elif correlation < 0:
    print("Relationship: Negative")
else:
    print("Relationship: Approximately zero")
```

### What This Solution Demonstrates

The solution uses `np.corrcoef()` to calculate the correlation matrix between experience and salary.

The `[0, 1]` indexing extracts the correlation coefficient between the two variables rather than returning the complete 2 × 2 correlation matrix.

The coefficient is then classified using conditional logic:

- Greater than `0` → Positive relationship
- Less than `0` → Negative relationship
- Equal to `0` → Approximately zero relationship

### Expected Results

```text
Correlation coefficient: 0.99
Relationship: Positive
```

The result shows a **very strong positive relationship** between experience and salary in this dataset.

This exercise reinforces **correlation analysis**, extracting values from NumPy results, and using conditional logic to interpret a numerical relationship.

# 📁 Project Structure

Current repository structure:

```text
20_numPy__20_pandas_practice_questions/
├── 01_create__inspect_an_array.py
├── 02_array_arithmetic.py
├── 03_filtering_with_boolean_indexing.py
├── 04_replace_values_using_conditions.py
├── 05_basic_statistics.py
├── 06_reshape_data.py
├── 07_row__column_operation.py
├── 08_find_indexes_of_important_values.py
├── 09_sort_an_array.py
├── 10_remove_duplicates.py
├── 11_missing_values.py
├── 12_normalize_values.py
├── 13_standardization.py
├── 14_comparing_two_datasets.py
├── 15_matrix_operations.py
├── 16_detect_outliers_with_numpy.py
├── 17_generate_synthetic_data.py
├── 18_analyze_2d_dataset.py
├── 19_NUMPY_correlation.py
└── README.md
```

As additional questions are completed, each solution will be added as a separate Python file:

```text
20_numPy__20_pandas_practice_questions/
├── 01_create__inspect_an_array.py
├── 02_array_arithmetic.py
├── 03_filtering_with_boolean_indexing.py
├── 04_replace_values_using_conditions.py
├── ...
├── 20_numpy_mini_data_analysis_challenge.py
├── 21_create_a_dataframe.py
├── ...
├── 40_pandas_mini_ecommerce_analysis.py
└── README.md
```

The filenames above represent the intended progression; files should be added as the corresponding problems are actually completed.

---

# 📊 Progress

| Section   | Questions | Completed | Remaining |
| --------- | --------: | --------: | --------: |
| NumPy     |      1–20 |        19 |         1 |
| Pandas    |     21–40 |         0 |        20 |
| **Total** |  **1–40** |    **19** |    **21** |

**Overall progress: 19 / 40 completed (47.5%)**

---

# 🧠 Skill Progression

These exercises intentionally build on analytical ideas that appear in multiple tools.

For example:

```text
Python aggregation
      ↓
SQL GROUP BY
      ↓
NumPy axis operations
      ↓
Pandas groupby()
```

Another progression is:

```text
SQL ROW_NUMBER()
      ↓
Pandas ranking
```

And:

```text
SQL window functions
      ↓
Pandas rolling / cumulative calculations
```

The purpose is to develop **cross-tool pattern recognition** rather than memorizing isolated library commands.

---

# 🛠️ Technologies

- **Python**
- **NumPy**
- **Pandas** — used in the later exercises
- **Git / GitHub** — for version control and tracking progress

---

# 📌 Practice Strategy

Each exercise should follow the same workflow:

1. Read the problem carefully.
2. Identify the required concept(s).
3. Write the solution in a separate `.py` file.
4. Run and verify the output.
5. Keep the solution focused on the requested task.
6. Update this README when the question is completed.
7. Commit the completed exercise to Git.
8. Move to the next question.

The goal is **progressive skill development**, not completing all 40 questions as quickly as possible.

---

# 🚀 Long-Term Learning Path

This practice set fits into a broader Data Analyst / Data Science progression:

```text
Python
   ↓
SQL
   ↓
NumPy
   ↓
Pandas
   ↓
Power BI
   ↓
Statistics
   ↓
Machine Learning
   ↓
Data Engineering
```

The NumPy and Pandas questions are deliberately connected to concepts from Python and SQL so that the same analytical ideas can be practiced in different environments.

---

## 📚 Source Practice Set

The exercises in this repository are based on the **20 NumPy + 20 Pandas Practice Questions** practice set.

The original sequence covers:

- NumPy fundamentals
- NumPy data analysis
- Practical NumPy data science
- Pandas fundamentals
- Pandas data cleaning
- Pandas data analysis
- Intermediate Pandas analytics

This repository tracks the implementation of those exercises as individual Python solutions.

---

## 🔄 Current Status

**Current progress:**

```text
01 — Create and inspect an array       ✅
02 — Array arithmetic                  ✅
03 — Filtering with Boolean indexing   ✅
04 — Replace values using conditions   ✅
05 — Basic statistics                  ✅
06 — Reshape data                      ✅
07 — Row and column operations         ✅
08 — Find indexes of important values  ✅
09 — Sort an array                     ✅
10 — Remove duplicates                 ✅
11 — Missing values                    ✅
12 — Normalize values                  ✅
13 — Standardization                   ✅
14 — Compare two datasets              ✅
15 — Matrix operations                 ✅
16 — Detect outliers with NumPy        ✅
17 — Generate synthetic data            ✅
18 — Analyze a 2D dataset              ✅
19 — Correlation with NumPy            ✅
```

### Next Exercise

**20 — NumPy Mini Data-Analysis Challenge**

The next task will practice:

- Customer analytics
- Statistics
- Filtering
- Correlation
