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
| 8   | Find indexes of important values | `argmax()`, `argmin()`, `where()` | ⬜ Pending   |
| 9   | Sort an array                    | `sort()`, `argsort()`             | ⬜ Pending   |
| 10  | Remove duplicates                | `np.unique()`                     | ⬜ Pending   |

### Level N3 — NumPy Data Analysis

| #   | Practice Problem     | Main Concepts                                      | Status     |
| --- | -------------------- | -------------------------------------------------- | ---------- |
| 11  | Missing values       | `np.isnan()`, `np.nanmean()`                       | ⬜ Pending |
| 12  | Normalize values     | Min-Max normalization, feature scaling             | ⬜ Pending |
| 13  | Standardization      | Mean, standard deviation, z-score, feature scaling | ⬜ Pending |
| 14  | Compare two datasets | Prediction error, absolute error, MAE              | ⬜ Pending |
| 15  | Matrix operations    | Matrix arithmetic, `.T`, `@`                       | ⬜ Pending |

### Level N4 — Practical Data Science

| #   | Practice Problem                   | Main Concepts                                          | Status     |
| --- | ---------------------------------- | ------------------------------------------------------ | ---------- |
| 16  | Detect outliers with NumPy         | IQR, Q1, Q3, bounds, outliers                          | ⬜ Pending |
| 17  | Generate synthetic data            | Random data generation, reproducibility                | ⬜ Pending |
| 18  | Analyze a 2D dataset               | 2D arrays, column analysis, filtering                  | ⬜ Pending |
| 19  | Correlation                        | Correlation coefficient, relationship analysis         | ⬜ Pending |
| 20  | NumPy mini data-analysis challenge | Customer analytics, statistics, filtering, correlation | ⬜ Pending |

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
| NumPy     |      1–20 |         7 |        13 |
| Pandas    |     21–40 |         0 |        20 |
| **Total** |  **1–40** |     **7** |    **33** |

**Overall progress: 7 / 40 completed (17.5%)**

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
```

### Next Exercise

**08 — Find indexes of important values**

The next task will practice:

- `argmax()`
- `argmin()`
- `where()`
- Finding indexes of important values
