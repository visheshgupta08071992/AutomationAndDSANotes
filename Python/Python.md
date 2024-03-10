## Understanding Python

### Basics of Python

Pycharm is IDE which is mostly used for coding in Python While PIP(Python Package Index) is used to download and use external packages in Python. It is similar to maven or gradle in Java.

### For Printing a statement

`` print() ``

### Comments in Python

```python
# This is a single-line comment  - SHortcut(ctrl + /)

'''
This is a multi-line comment
spanning multiple lines.
'''

"""
This is also a multi-line comment
spanning multiple lines.
"""

```

### DataTypes in Python

```python
# Print Statement
print("Hello, How are you")

# DataTypes in Python

#int
a=5
print(5) #5

#float
a=5.5
print(a) #5.5

#boolean
c= True # or False
print(c) #True

#String
d="Vihes"

print(d) #Vishes

#None
#None is a dataype in Python which represents the absence of value that is there is no value

e=None
print(e) #None

```

### Typecasting in Python

Certainly! Typecasting, also known as type conversion or type coercion, is the process of converting the data from one data type to another. In Python, you can perform typecasting using built-in functions or constructors provided by Python.

### Implicit Type Conversion (Automatic Typecasting):

Python automatically converts data types in certain situations, such as when performing operations involving different data types. This is known as implicit type conversion. For example:

```python
# Implicit type conversion
x = 10       # integer
y = 5.5      # float

result = x + y   # x is implicitly converted to float
print(result)    # Output: 15.5
```

### Explicit Type Conversion (Manual Typecasting):

You can also explicitly convert data types using built-in functions or constructors. This is called explicit type conversion. Here are some commonly used functions for typecasting in Python:

1. **int()**: Converts a value to an integer.

```python
# Explicitly converting a float to an integer
x = 10.5
int_x = int(x)
print(int_x)  # Output: 10
```

2. **float()**: Converts a value to a floating-point number.

```python
# Explicitly converting an integer to a float
y = 5
float_y = float(y)
print(float_y)  # Output: 5.0
```

3. **str()**: Converts a value to a string.

```python
# Explicitly converting an integer to a string
z = 100
str_z = str(z)
print(str_z)  # Output: "100"
```

4. **list()**: Converts a sequence (e.g., tuple, string) to a list.

```python
# Explicitly converting a tuple to a list
tuple_values = (1, 2, 3)
list_values = list(tuple_values)
print(list_values)  # Output: [1, 2, 3]
```

5. **tuple()**: Converts a sequence (e.g., list, string) to a tuple.

```python
# Explicitly converting a list to a tuple
list_values = [4, 5, 6]
tuple_values = tuple(list_values)
print(tuple_values)  # Output: (4, 5, 6)
```

6. **set()**: Converts a sequence (e.g., list, tuple) to a set.

```python
# Explicitly converting a list to a set
list_values = [1, 2, 2, 3, 3, 3]
set_values = set(list_values)
print(set_values)  # Output: {1, 2, 3}
```

7. **bool()**: Converts a value to a boolean.

```python
# Explicitly converting an integer to a boolean
x = 10
bool_x = bool(x)
print(bool_x)  # Output: True
```

### Functions in Python

**Syntax**

```python
def function_name(parameters):
    """docstring"""
    # function body
    # (statements to be executed)
    return expression
```

**Example**

```python
def add_numbers(a, b):
    """This function adds two numbers."""
    sum = a + b
    return sum

result = add_numbers(10, 20)
print("Sum:", result)  # Output: Sum: 30
```


### Modules in Python


A module is a file containing Python definitions and statements. The file name is the module name with the suffix `.py`. Modules can contain functions, variables, and classes that can be imported and used in other Python scripts.

#### Creating a Module:

Here's an example of a simple module named `my_module.py`:

```python
# my_module.py

def greeting(name):
    print("Hello, " + name)
```

#### Using a Module:

To use the functions defined in a module, you need to import the module into your Python script using the `import` statement.

```python
# main.py

import my_module

my_module.greeting("Alice")  # Output: Hello, Alice
```

You can also import specific functions or variables from a module using the `from` keyword.

```python
# main.py

from my_module import greeting

greeting("Bob")  # Output: Hello, Bob
```

### PIP (Python Package Index):

PIP is a package manager for Python that allows you to install, uninstall, and manage Python packages (also known as libraries or modules) from the Python Package Index (PyPI). PyPI is a repository of software packages developed and maintained by the Python community.

#### Installing Packages with PIP:

To install a package using PIP, you can use the `pip install` command followed by the package name.

```bash
pip install package_name
```

For example, to install the `requests` package, you would run:

```bash
pip install requests
```

#### Listing Installed Packages:

You can list all installed packages and their versions using the `pip list` command.

```bash
pip list
```

#### Uninstalling Packages:

To uninstall a package, you can use the `pip uninstall` command followed by the package name.

```bash
pip uninstall package_name
```

#### Requirements File:

You can also create a requirements file (`requirements.txt`) that lists all the packages required for your project along with their versions. This file can then be used to install all the dependencies at once.

```text
# requirements.txt

requests==2.26.0
numpy==1.21.2
```

To install the packages listed in the requirements file, you can use the `-r` flag with the `pip install` command.

```bash
pip install -r requirements.txt
```










