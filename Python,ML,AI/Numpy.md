## Understanding Numpy

### Basics of Numpy

Numpy in a Numerical Python package used majorly for scientific computation in Python. Numpy provides support for arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.

### Jupyter Notebook

Jupyter Notebook is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations, and narrative text. It supports multiple programming languages, but it is particularly popular in the Python community.

Here's a breakdown of its key features and uses:

1. **Interactive Computing**: Jupyter Notebooks allow you to write and execute code in individual cells. This makes it ideal for interactive computing, as you can run small code snippets and immediately see the results.

2. **Support for Multiple Languages**: Although originally designed for Python, Jupyter Notebooks support many programming languages including R, Julia, and Scala. This makes it a versatile tool for data science and scientific computing.

3. **Rich Output**: Jupyter Notebooks support rich media representations, allowing you to include images, videos, HTML, LaTeX, and more within your documents. This makes it easy to create reports and presentations that combine code, visualizations, and explanatory text.

4. **Data Exploration and Visualization**: With libraries like NumPy, Pandas, and Matplotlib integrated with Jupyter Notebooks, you can easily explore and visualize data. This makes it a powerful tool for data analysis and visualization tasks.

5. **Education and Sharing**: Jupyter Notebooks are widely used in education and research for teaching programming, data science, and other subjects. They allow instructors to create interactive tutorials and exercises, and students can run the code and experiment with it in real-time. Additionally, Jupyter Notebooks can be easily shared with others, allowing for collaboration and reproducibility of results.

6. **Integration with External Tools**: Jupyter Notebooks can be integrated with version control systems like Git, interactive widgets, and external services like GitHub, Dropbox, and Google Drive. This makes it easy to work with notebooks in a collaborative environment and share them with others.

Overall, Jupyter Notebook is a versatile and powerful tool for interactive computing, data analysis, and scientific research, and it's widely used in academia, industry, and education. If you're learning NumPy or any other Python library for data science, using Jupyter Notebooks can greatly enhance your learning experience and productivity.


### How to install Numpy and Jupiter notebook

**Command to install Numpy**
```
pip install numpy
```

**Command to install Jupyter notebook**
```
pip install jupyter
```

**Command to start Jupyter notebook**

```
jupyter notebook
```

**Command to import numpy**

```
import numpy as np
```
By convention, NumPy is usually imported as `np`, making it easier to reference its functions and classes.

### Advantage of Using Numpy Arrays

1. Numpy uses much less memory to store data. Numpy Arrays can only store data of same Type while Python list allows storing data of different types.
2. Numpy makes it extremely easy to perform mathematical operations on it while mathematical operations are difficult to perform with List.
3. Numpy Used for the creation of n-dimensional arrays.


### Creating NumPy Arrays

The most fundamental object in NumPy is the `ndarray`, which is an n-dimensional array. You can create NumPy arrays in several ways:

1. **From a Python list**:

```python
my_list = [1, 2, 3, 4, 5]
my_array = np.array(my_list)
print(my_array) # Output: [1 2 3 4 5]
```

2. **Using built-in functions**:

```python
# Create an array of zeros
zeros_array = np.zeros((3, 4))  # Creates a 3x4 array filled with zeros
print(zeros_array)

"""
Output:
[[0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]]
"""

# Create an array of ones
ones_array = np.ones((2, 3))  # Creates a 2x3 array filled with ones
print(ones_array)

"""
Output:
[[1. 1. 1.]
 [1. 1. 1.]]
"""

# Create an array with a range of values
range_array = np.arange(10)  # Creates a 1D array with values from 0 to 9
print(range_array)   # Output: [0 1 2 3 4 5 6 7 8 9]



# Create an array of random values
random_array = np.random.rand(2, 2)  # Creates a 2x2 array with random values
print(random_array)

"""
Output:
[[0.36651521 0.77502487]
 [0.52115335 0.92239789]]
"""

```

### Array Attributes and Methods

Once you've created an array, you can access its attributes and use its methods to perform various operations. Some commonly used attributes and methods include:

1. **Shape and Size**:

```python
my_list = [1, 2, 3, 4, 5]
my_array = np.array(my_list)
print(my_array.shape)  # Prints the shape of the array (Output: (5,))
print(my_array.size)   # Prints the number of elements in the array (Output: 5)
myarr2D=np.array([[2,3],[4,5]])
print(myarr2D.shape)  # Prints the shape of the array Output -(2, 2) 
print(myarr2D.size)   # Prints the number of elements in the array (Output: 4)
```

2. **Reshaping**:

```python
my_list = [1, 2, 3, 4, 5]
reshaped_array = my_array.reshape(5, 1)  # Reshapes the array to a 5x1 array
print(reshaped_array)
"""
Output:
[[1]
 [2]
 [3]
 [4]
 [5]]
"""
```

3. **Indexing and Slicing**:

```python
my_list = [1, 2, 3, 4, 5]
my_array = np.array(my_list)
print(my_array[0])     # Accesses the element at index 0 (Output: 1)
print(my_array[:2])    # Accesses the first two elements (Output: [1 2])
print(my_array[2:])    # Accesses elements from index 2 to the end (Output: [3 4 5])
```

4. **Mathematical Operations**:

```python
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

print(array1 + array2)  # Element-wise addition (Output: [5 7 9])
print(array1 * array2)  # Element-wise multiplication (Output: [ 4 10 18])
print(np.dot(array1, array2))  # Dot product (Output: 32)
```

5. **Statistical Functions**:

```python
print(np.mean(my_array))   # Computes the mean of the array (Output: 3.0)
print(np.median(my_array)) # Computes the median of the array (Output: 3.0)
print(np.std(my_array))    # Computes the standard deviation of the array (Output: 1.4142135623730951)
```

