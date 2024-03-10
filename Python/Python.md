## Understanding Python

### Basics of Python

1.**For Printing a statement** - `` print() ``

2.**Comments in Python**

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

3. **DataTypes in Python**

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

4.**Typecasting in Python**

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







