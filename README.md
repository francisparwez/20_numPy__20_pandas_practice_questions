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
| 20  | NumPy mini data-analysis challenge | Customer analytics, statistics, filtering, correlation | ✅ Completed |

---

# 🐼 Pandas — 20 Questions

The Pandas section begins after the NumPy exercises and moves from DataFrame fundamentals into data cleaning, aggregation, joins, time-series calculations, and customer/e-commerce analysis.

## Level P1 — Pandas Fundamentals

| #   | Practice Problem          | Main Concepts                                                 | Status       |
| --- | ------------------------- | ------------------------------------------------------------- | ------------ |
| 21  | Create a DataFrame        | `DataFrame`, `head()`, `shape`, columns, `dtypes`, statistics | ✅ Completed |
| 22  | Select columns            | `df["column"]`, `df[[...]]`                                   | ✅ Completed |
| 23  | Filter rows               | Boolean filtering, multiple conditions                        | ✅ Completed |
| 24  | Sort data                 | `sort_values()`                                               | ⬜ Pending   |
| 25  | Create calculated columns | Vectorized column operations                                  | ✅ Completed |

## Level P2 — Pandas Data Cleaning

| #   | Practice Problem           | Main Concepts                              | Status       |
| --- | -------------------------- | ------------------------------------------ | ------------ |
| 26  | Handle missing values      | Missing-value detection, median imputation | ✅ Completed |
| 27  | Remove duplicates          | `duplicated()`, `drop_duplicates()`        | ✅ Completed |
| 28  | Convert data types         | Numeric conversion, type handling          | ✅ Completed |
| 29  | Clean categorical data     | String standardization, frequency counts   | ✅ Completed |
| 30  | Detect and handle outliers | IQR, filtering, cleaned DataFrame          | ⬜ Pending   |

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

## 20 — NumPy Mini Data-Analysis Challenge

**File:**

```text
20_NUMPY_mini_data_analysis_challenge.py
```

### Problem

Generate a dataset for **100 customers**, with five attributes:

- Customer ID
- Age
- Annual income
- Number of purchases
- Total spending

Use NumPy to calculate average age, average income, average spending, the highest and lowest spenders, customers spending above average, customers with more than 10 purchases, income–spending correlation, median spending, and the number of unique age values.

### Concepts Practiced

```text
np.random.seed()
np.column_stack()
Array transposition and unpacking (.T)
np.mean(), np.max(), np.min(), np.argmax(), np.argmin()
Boolean indexing
np.corrcoef()
np.median()
np.unique()
```

### Solution

```python
import numpy as np

# Generate reproducible data
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
print("6. Customer IDs spending above average:", customer_id[above_average])
print("   Their spending:", total_spending[above_average])

# 7. Customers with more than 10 purchases
frequent_customers = no_of_purchases > 10
print("7. Customer IDs with more than 10 purchases:", customer_id[frequent_customers])
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
```

### What This Solution Demonstrates

- `np.random.seed(42)` makes the generated data reproducible.
- `np.column_stack()` combines the five 100-element arrays into a 100 × 5 dataset.
- `dataset.T` transposes the dataset so each column can be unpacked into its own array.
- `np.argmax()` and `np.argmin()` identify the indexes of the highest and lowest spending values. Those indexes are then used to retrieve the corresponding customer IDs.
- Boolean masks filter customer IDs and their associated spending or purchase counts while preserving the row correspondence.
- `np.corrcoef(income, total_spending)[0, 1]` extracts the single correlation coefficient from the 2 × 2 correlation matrix.
- `np.unique(age)` returns the distinct ages, and `len()` counts them.

### Key Results

With the fixed random seed, the main numerical results are:

```text
Dataset shape: (100, 5)
Number of customers: 100
Average age: 57.38
Average income: 93302.94
Average spending: 2296.82
Highest spender ID: 89 (spending: 4500)
Lowest spender ID: 38 (spending: 21)
Income-spending correlation: -0.037
Median spending: 2509.5
Number of unique age values: 56
```

The generated income and spending values are independent random draws, so the correlation is close to zero in this run. This is expected for synthetic practice data and should not be interpreted as evidence about real customers.

This final NumPy exercise brings together **dataset construction, descriptive statistics, index-based selection, Boolean filtering, correlation, and unique-value counting**.

---

## 21 — Create a DataFrame

**File:**

```text
21_PANDAS_create_dataframe.py
```

### Problem

Create a DataFrame from employee data and display the first five rows, shape, column names, data types, and basic statistics.

### Concepts Practiced

```text
pd.DataFrame()
df.head()
df.shape
df.columns
df.dtypes
df.describe()
```

### Solution

```python
import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie", "David"],
    "age": [25, 30, 35, 28],
    "salary": [50000, 60000, 75000, 55000]
}

df = pd.DataFrame(data)

print(f"First 5 Rows:\n{df.head(5)}\n")
print(f"Shape: {df.shape}\n")
print(f"Columns: {df.columns}\n")
print(f"Data Types For Each Column:\n{df.dtypes}\n")
print(f"Basic Statistics:\n{df.describe()}")
```

### What This Solution Demonstrates

- `pd.DataFrame(data)` creates a DataFrame from a dictionary.
- `df.head(5)` displays up to five rows. This dataset contains four rows, so all four are displayed.
- `df.shape` returns the number of rows and columns: `(4, 3)`.
- `df.columns` displays the column labels.
- `df.dtypes` displays each column's data type.
- `df.describe()` summarizes the numeric columns with descriptive statistics.

---

## 22 — Select Columns

**File:**

```text
22_PANDAS_selected_columns.py
```

### Problem

Using the employee DataFrame, select the `name` column, the `salary` column, both `name` and `salary`, and both `age` and `salary`.

### Concepts Practiced

```text
Single-column selection
Multiple-column selection
Pandas Series
Pandas DataFrame
df["column"]
df[["column1", "column2"]]
```

### Solution

```python
import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie", "David"],
    "age": [25, 30, 35, 28],
    "salary": [50000, 60000, 75000, 55000]
}

df = pd.DataFrame(data)

print(df['name'])
print(df['salary'])
print(df[['name', 'salary']])
print(df[['age', 'salary']])
```

### What This Solution Demonstrates

- `df['name']` and `df['salary']` each return a one-dimensional Pandas Series.
- `df[['name', 'salary']]` returns a DataFrame containing two columns.
- `df[['age', 'salary']]` selects a different pair of columns.
- The order of columns in the selection follows the order specified in the list.

---

## 23 — Filter Rows

**File:**

```text
23_PANDAS_filter_rows.py
```

### Problem

Using the employee data, find employees whose age is greater than 30, whose salary is greater than 60,000, whose salary is between 50,000 and 70,000, and whose age is greater than 25 **and** salary is greater than 55,000.

### Concepts Practiced

```text
Boolean filtering
Comparison operators
Series.between()
Combining conditions with &
Boolean masks
```

### Solution

```python
import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie", "David"],
    "age": [25, 30, 35, 28],
    "salary": [50000, 60000, 75000, 55000]
}

df = pd.DataFrame(data)

print(df[df['age'] > 30])
print(df[df['salary'] > 60000])
print(df[df['salary'].between(50000, 70000)])
print(df[(df['age'] > 25) & (df['salary'] > 55000)])
```

### What This Solution Demonstrates

- `df[condition]` selects rows for which the condition evaluates to `True`.
- `df['age'] > 30` filters employees older than 30.
- `df['salary'] > 60000` filters employees earning more than 60,000.
- `.between(50000, 70000)` includes both boundary values by default.
- `&` combines conditions using **AND**. Each condition is wrapped in parentheses.

### Expected Results

- Age greater than 30: Charlie.
- Salary greater than 60,000: Charlie.
- Salary between 50,000 and 70,000: Alice, Bob, and David.
- Age greater than 25 **and** salary greater than 55,000: Bob and Charlie.

These first three Pandas exercises establish a workflow of creating a DataFrame, selecting relevant columns, and filtering rows using conditions.

---

## 24 — Sort Data _(Pending)_

**File:**

```text
24_PANDAS_sort_data.py
```

### Problem

Using an employee DataFrame with `name`, `department`, `age`, and `salary` columns, practise sorting employees by:

1. Salary in ascending order (lowest to highest).
2. Salary in descending order (highest to lowest).
3. Age in descending order (oldest to youngest).
4. Department in ascending order, then salary in descending order within each department.

### Concepts to Practise

```text
DataFrame.sort_values()
ascending=True
ascending=False
Sorting by multiple columns
Per-column sort directions
```

### Key Syntax

```python
df.sort_values(by="salary", ascending=True)
df.sort_values(by="salary", ascending=False)
df.sort_values(by="age", ascending=False)
df.sort_values(
    by=["department", "salary"],
    ascending=[True, False]
)
```

### What This Exercise Teaches

- `sort_values()` orders rows based on one or more columns.
- `ascending=True` sorts from lower to higher values or alphabetically.
- `ascending=False` sorts from higher to lower values or reverse-alphabetically.
- When sorting by multiple columns, the order of the columns in `by` determines the sorting priority.
- Each item in `ascending` corresponds to the column in the same position in `by`. In the final task, departments are sorted alphabetically first, and salaries are sorted from highest to lowest within each department.

**Status:** Pending — complete and verify the exercise before marking it as completed.

---

## 25 — Create Calculated Columns

**File:**

```text
25_PANDAS_create_calculated_columns.py
```

### Problem

Using employee monthly salaries, create calculated columns for annual salary, tax, and net monthly salary.

### Concepts Practiced

```text
Vectorized column operations
Derived columns
Percentage calculations
Pandas Series arithmetic
```

### Solution

```python
import pandas as pd

df = pd.DataFrame({
    'employee': ['Alice', 'Bob', 'Charlie', 'David'],
    'monthly_salary': [4500, 6000, 3200, 8500]
})

# Calculate annual salary
df['annual_salary'] = df['monthly_salary'] * 12

# Calculate tax amount (10% of monthly salary)
df['tax'] = df['monthly_salary'] * 0.10

# Calculate net monthly salary
df['net_salary'] = df['monthly_salary'] - df['tax']

print(df)
```

### What This Solution Demonstrates

- `df['monthly_salary'] * 12` calculates annual salary for every employee.
- `df['monthly_salary'] * 0.10` calculates a 10% monthly tax amount.
- Subtracting `tax` from `monthly_salary` calculates net monthly salary.
- Pandas applies these calculations to the entire column without requiring a loop.

### Expected Results

| Employee | Monthly Salary | Annual Salary | Tax (10%) | Net Monthly Salary |
| -------- | -------------: | ------------: | --------: | -----------------: |
| Alice    |          4,500 |        54,000 |       450 |              4,050 |
| Bob      |          6,000 |        72,000 |       600 |              5,400 |
| Charlie  |          3,200 |        38,400 |       320 |              2,880 |
| David    |          8,500 |       102,000 |       850 |              7,650 |

In this exercise, both `tax` and `net_salary` represent monthly amounts because the tax is calculated from `monthly_salary`.

---

## 26 — Handle Missing Values

**File:**

```text
26_PANDAS_handle_missing_values.py
```

### Problem

Given employee data with missing age and salary values:

- Count missing values in each column.
- Display rows containing at least one missing value.
- Fill missing ages with the median age.
- Fill missing salaries with the median salary.

### Concepts Practiced

```text
df.isnull()
df.isnull().sum()
df.isnull().any(axis=1)
Series.median()
Series.fillna()
Median imputation
```

### Solution

```python
import pandas as pd

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie", "David"],
    "age": [25, None, 35, 28],
    "salary": [50000, 60000, None, 55000]
})

# Number of missing values per column
print(df.isnull().sum())

# Rows containing missing values
print(df[df.isnull().any(axis=1)])

# Fill missing age and salary with their respective medians
df['age'] = df['age'].fillna(df['age'].median())
df['salary'] = df['salary'].fillna(df['salary'].median())

print(df)
```

### What This Solution Demonstrates

- `df.isnull().sum()` counts missing values column by column.
- `df.isnull().any(axis=1)` identifies rows where at least one value is missing.
- `df[df.isnull().any(axis=1)]` displays those rows rather than only returning a Boolean mask.
- `fillna()` replaces missing values, and `median()` calculates the replacement value from the non-missing values in each column.
- Assigning the result back to the column makes the update explicit.

### Expected Results

Before filling missing values, the missing-value counts are:

```text
name      0
age       1
salary    1
```

The rows containing missing values are Bob (missing age) and Charlie (missing salary).

The replacement values are:

- Median age: approximately `29.33`.
- Median salary: `55000`.

After imputation, all four rows have values for both `age` and `salary`.

---

## 27 — Remove Duplicates

**File:**

```text
27_PANDAS_remove_duplicates.py
```

### Problem

Given customer data with repeated rows:

- Count the duplicate rows.
- Display duplicate occurrences.
- Remove duplicates.
- Verify the final row count.

### Concepts Practiced

```text
df.duplicated()
df.duplicated().sum()
df.drop_duplicates()
len(df)
```

### Solution

```python
import pandas as pd

# Sample customer data with duplicate rows
data = {
    "name": ["Alice", "Bob", "Alice", "Charlie", "Bob", "David"],
    "email": [
        "alice@email.com",
        "bob@email.com",
        "alice@email.com",
        "charlie@email.com",
        "bob@email.com",
        "david@email.com"
    ]
}

df = pd.DataFrame(data)

print(f"Original number of rows: {len(df)}")
print(f"Number of Duplicate Rows found: {df.duplicated().sum()}")
print(f"Duplicate Rows:\n{df[df.duplicated()]}")

df = df.drop_duplicates()
print(f"Number of rows after removing duplicates: {len(df)}")
```

### What This Solution Demonstrates

- `len(df)` returns the number of rows in the DataFrame.
- `df.duplicated()` marks subsequent occurrences of fully duplicated rows as `True`; the first occurrence is retained by default.
- `.sum()` counts the `True` values to calculate the number of duplicate rows.
- `df[df.duplicated()]` displays only the duplicate occurrences.
- `df.drop_duplicates()` removes repeated rows while keeping the first occurrence by default.

### Expected Results

```text
Original number of rows: 6
Number of Duplicate Rows found: 2
Number of rows after removing duplicates: 4
```

Alice and Bob each appear twice with the same email, so two repeated rows are removed. By default, Pandas compares all columns when identifying duplicate rows.

---

## 28 — Convert Data Types

**File:**

```text
28_PANDAS_convert_data_types.py
```

### Problem

The `age` and `salary` columns contain numbers stored as strings. Convert both columns to numeric types, then calculate the average age and average salary.

### Concepts Practiced

```python
pd.to_numeric()
Series.mean()
```

### Solution

```python
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
```

### What This Solution Demonstrates

- `pd.to_numeric()` converts values such as numeric strings into numeric values.
- Converting the columns before calculating their means ensures Pandas treats the values as numbers rather than text.
- `.mean()` calculates the arithmetic average of each numeric column.
- `pd.to_numeric()` raises an error by default if a value cannot be converted. For messy data, `errors="coerce"` can convert invalid values to `NaN` so they can be handled separately.

### Expected Results

```text
Average age: 32.5
Average salary: 65000.0
```

---

## 29 — Clean Categorical Data

**File:**

```text
29_PANDAS_clean_categorical_data.py
```

### Problem

The `city` column contains inconsistent capitalization, such as `Karachi`, `karachi`, and `KARACHI`. Standardize the city names so each city has a consistent label, then count the customers in each city.

### Concepts Practiced

```python
Series.str.capitalize()
Series.value_counts()
```

### Solution

```python
import pandas as pd

# Sample data
data = {
    "city": ["Karachi", "karachi", "KARACHI", "Lahore", "lahore", "Islamabad"]
}

df = pd.DataFrame(data)

# Standardize city names by capitalizing the first letter and lowercasing the rest
df["city"] = df["city"].str.capitalize()

# Count customers per city
city_counts = df["city"].value_counts()

print(city_counts)
```

### What This Solution Demonstrates

- `.str.capitalize()` standardizes capitalization, so variations such as `Karachi`, `karachi`, and `KARACHI` become `Karachi`.
- `.value_counts()` counts the occurrences of each standardized city and sorts the counts from highest to lowest by default.
- The solution handles the capitalization variations in the provided data. For real-world data, `.str.strip()` can also be used before capitalization to remove leading or trailing spaces.

### Expected Results

```text
city
Karachi      3
Lahore       2
Islamabad    1
Name: count, dtype: int64
```

---

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
├── 20_NUMPY_mini_data_analysis_challenge.py
├── 21_PANDAS_create_dataframe.py
├── 22_PANDAS_selected_columns.py
├── 23_PANDAS_filter_rows.py
├── 24_PANDAS_sort_data.py
├── 25_PANDAS_create_calculated_columns.py
├── 26_PANDAS_handle_missing_values.py
├── 27_PANDAS_remove_duplicates.py
├── 28_PANDAS_convert_data_types.py
├── 29_PANDAS_clean_categorical_data.py
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
├── 20_NUMPY_mini_data_analysis_challenge.py
├── 21_PANDAS_create_dataframe.py
├── 22_PANDAS_selected_columns.py
├── 23_PANDAS_filter_rows.py
├── 24_PANDAS_sort_data.py
├── 25_PANDAS_create_calculated_columns.py
├── 26_PANDAS_handle_missing_values.py
├── 27_PANDAS_remove_duplicates.py
├── 28_PANDAS_convert_data_types.py
├── 29_PANDAS_clean_categorical_data.py
├── ...
├── 40_pandas_mini_ecommerce_analysis.py
└── README.md
```

The filenames above represent the intended progression; files should be added as the corresponding problems are actually completed.

---

# 📊 Progress

| Section   | Questions | Completed | Remaining |
| --------- | --------: | --------: | --------: |
| NumPy     |      1–20 |        20 |         0 |
| Pandas    |     21–40 |         8 |        12 |
| **Total** |  **1–40** |    **28** |    **12** |

**Overall progress: 28 / 40 completed (70%)**

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
20 — NumPy mini data-analysis challenge ✅
21 — Create a DataFrame                ✅
22 — Select columns                    ✅
23 — Filter rows                       ✅
24 — Sort data                         ⬜ Pending
25 — Create calculated columns         ✅
26 — Handle missing values             ✅
27 — Remove duplicates                 ✅
28 — Convert data types                 ✅
29 — Clean categorical data              ✅
```

### Next Exercise

**30 — Detect and Handle Outliers**

The next task practises identifying outliers and filtering data using the IQR method. Question 24 remains pending and can be completed later.
