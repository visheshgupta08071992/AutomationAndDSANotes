## Understanding Pandas

Pandas is a powerful library in Python that allows you to work with data structures and perform data analysis. It's a must-know tool for data scientists, data analysts, and anyone working with data.


### 1. Installation:
First, you need to install Pandas if you haven't already. You can install it using pip:

```bash
pip install pandas
```

### 2. Importing Pandas:
Once installed, you can import Pandas into your Python script or notebook:

```python
import pandas as pd
```

### 3. Creating DataFrames:
The primary data structure in Pandas is the DataFrame. You can create a DataFrame using various methods:

#### From a dictionary:
```python
data = {'Name': ['John', 'Anna', 'Peter'],
        'Age': [28, 35, 42],
        'City': ['New York', 'Paris', 'London']}
df = pd.DataFrame(data)
print(df)
```

![image](https://github.com/visheshgupta08071992/AutomationAndDSANotes/assets/52998083/5c2ada4c-db30-47e9-8ea8-7252c50af2d5)


#### From a list of lists:
```python
data1 = [['John', 28, 'New York'],
        ['Anna', 35, 'Paris'],
        ['Peter', 42, 'London']]
df1 = pd.DataFrame(data1, columns=['Name', 'Age', 'City'])
```

### 4. Viewing Data:
You can use various methods to view data within a DataFrame:

#### Head:
```python
df.head()  # Displays the first few rows (default: 5)
```

#### Tail:
```python
df.tail()  # Displays the last few rows (default: 5)
```

#### Sample:
```python
df.sample(3)  # Displays a random sample of rows
```

### 5. Accessing Data:
You can access data within a DataFrame using indexing and slicing:

#### Column Selection:
```python
df['Name']  # Selects a single column
df[['Name', 'Age']]  # Selects multiple columns
```

![image](https://github.com/visheshgupta08071992/AutomationAndDSANotes/assets/52998083/31f90001-0fec-4700-aad9-6db1cd61bb66)


#### Row Selection:
```python
df.loc[0]  # Selects a single row by label
df.loc[[0, 2]]  # Selects multiple rows by label
```

![image](https://github.com/visheshgupta08071992/AutomationAndDSANotes/assets/52998083/3f0b2d15-31fb-4920-a15a-a2882274d880)


#### Conditional Selection:
```python
df[df['Age'] > 28]  # Selects rows where Age is greater than 30
```

![image](https://github.com/visheshgupta08071992/AutomationAndDSANotes/assets/52998083/f564bdec-aeb5-46ad-a19a-96c8aad35dcb)


### 6. Data Manipulation:
Pandas provides various methods for manipulating data:

#### Adding Columns:
```python
df['Salary'] = [50000, 60000, 70000]  # Adds a new column
```

#### Adding Rows:

Adding a new row to a DataFrame in Pandas can be achieved in several ways, depending on the specific requirements and the format of the data you want to append. Below are some common methods to add a new row to a DataFrame:

### Method 1: Using `loc`
If you know the index of the new row and it doesn't exist in the DataFrame, you can use the `loc` indexer to add a new row by specifying the index and assigning the values directly. This method is straightforward when you have a single row to add.

```python
import pandas as pd

# Existing DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob'],
    'Age': [25, 30]
})

# Adding a new row
df.loc[len(df) + 1] = ['Charlie', 35]

print(df)
```

### Method 2: Using `append`
The `append` method can add a row or multiple rows to a DataFrame. You need to pass either a Series, a DataFrame, or a dictionary representing the new rows. Note that `append` does not modify the original DataFrame; it returns a new DataFrame unless you reassign it.

```python
# Adding a new row using a dictionary
new_row = {'Name': 'David', 'Age': 40}
df = df.append(new_row, ignore_index=True)

print(df)
```

### Method 3: Using `concat`
The `concat` function is generally used for concatenating two or more DataFrames along a particular axis (either rows or columns). This is useful when you have multiple rows to add as a DataFrame.

```python
# Creating a DataFrame to append
new_rows = pd.DataFrame({
    'Name': ['Eve', 'Frank'],
    'Age': [28, 35]
})

df = pd.concat([df, new_rows], ignore_index=True)

print(df)
```

### Method 4: Using `pd.DataFrame.loc` with explicit index
If you have an explicit index name or number, you can directly add a new row using it:

```python
# Assuming df has a specific index
df.loc['new_index'] = ['Grace', 22]

print(df)
```

### Notes:
- `append` and `concat` have a parameter `ignore_index=True` which is useful when you don't want to retain the original row indices of the appended data.
- Starting from pandas 1.4.0, `append` is deprecated, and it's recommended to use `concat` instead for appending new rows to a DataFrame.
- Always ensure that the columns in the row being added match those in the DataFrame to avoid introducing NaNs or other issues.

These are the most common methods to add rows to a DataFrame. Each has its uses depending on whether you're adding a single row, multiple rows, or appending entire datasets.

#### Removing Rows/Columns:

```python
df.drop('Salary', axis=1, inplace=True)  # Removes the 'Salary' column
df.drop(0,axis=0,inplace=True) # Removes row with index 0
```

**Function: `drop`**
The `drop` method in Pandas is used to remove rows or columns from a DataFrame. The removal is specified by label names and corresponding axis, or by directly specifying index or column names.

### Parameters:
1. **First parameter (`'Salary'` in your case)**:
    - This is typically the labels/index or a list of labels/indexes you want to remove.
    - In your example, `'Salary'` is the label of the column you want to remove from the DataFrame.

2. **`axis`**:
    - The `axis` parameter specifies the axis along which the specified label will be dropped.
    - `axis=0` or `axis='index'`: This would drop rows based on the labels provided.
    - `axis=1` or `axis='columns'`: This drops columns based on the labels provided.
    - In your example, `axis=1` indicates that the operation should be performed on columns, i.e., it will look for `'Salary'` among the column labels and drop that column.

3. **`inplace`**:
    - This parameter decides whether the change should be made in the original DataFrame itself or return a new DataFrame with the changes.
    - `inplace=True`: The DataFrame is updated in place (no new DataFrame is returned, and the original DataFrame is modified).
    - `inplace=False` (which is the default): A new DataFrame is returned with the specified modifications, and the original DataFrame remains unchanged.
    - Your example uses `inplace=True`, which means that the column `'Salary'` is removed from the DataFrame `df` itself, and `df` is updated accordingly.

### Usage:
After executing the code `df.drop('Salary', axis=1, inplace=True)`, the DataFrame `df` will no longer contain the column labeled `'Salary'`. This operation directly modifies `df` due to the `inplace=True` parameter. If `inplace` were set to `False` or omitted, you would need to assign the result back to `df` or another DataFrame variable to retain the changes, like so: `df = df.drop('Salary', axis=1)`.

The `drop` function is a powerful tool in Pandas for data manipulation, allowing for selective removal of data based on label criteria, thereby facilitating dataset cleaning or reformatting processes.



#### Renaming Columns:
```python
df.rename(columns={'Name': 'Full Name', 'City': 'Location'}, inplace=True)  # Renames columns
```

### 7. Data Cleaning:
You can clean your data using Pandas:

#### Handling Missing Values:
```python
df.dropna()  # Drops rows with missing values
df.fillna(0)  # Fills missing values with a specified value (here, 0)
```

### 8. Grouping and Aggregating Data:
You can group your data and perform aggregate operations:

```python
grouped = df.groupby('City')  # Groups data by 'City'
grouped.mean()  # Computes the mean for each group
```

### 9. Data Visualization:
Pandas also allows for basic data visualization:

```python
df['Age'].plot(kind='hist')  # Creates a histogram of Age
```

### 10. Exporting Data:
You can export your DataFrame to various file formats:

```python
df.to_csv('data.csv', index=False)  # Exports DataFrame to a CSV file
df.to_excel('data.xlsx', index=False)  # Exports DataFrame to an Excel file
```

This tutorial covers the basics of Pandas. As you become more comfortable, you can explore more advanced topics like time series analysis, merging and joining datasets, and more!
