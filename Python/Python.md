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


### Strings in Python

Strings are immutable i.e unmodifible. Whenever we a modify a String a new String is created.


1. **`capitalize()`**

   - This method returns a copy of the string with the first character capitalized and the rest of the characters in lowercase.

   ```python
   str = "hello world"
   capitalized_str = str.capitalize()
   print(capitalized_str)  # Output: Hello world
   ```

2. **`upper()`**

   - This method returns a copy of the string with all characters converted to uppercase.

   ```python
   str = "hello world"
   upper_str = str.upper()
   print(upper_str)  # Output: HELLO WORLD
   ```

3. **`lower()`**

   - This method returns a copy of the string with all characters converted to lowercase.

   ```python
   str = "HELLO WORLD"
   lower_str = str.lower()
   print(lower_str)  # Output: hello world
   ```

4. **`title()`**

   - This method returns a copy of the string with the first character of each word capitalized and the rest of the characters in lowercase.

   ```python
   str = "hello world"
   title_str = str.title()
   print(title_str)  # Output: Hello World
   ```

5. **`strip()`**

   - This method returns a copy of the string with leading and trailing whitespace removed.

   ```python
   str = "   hello world   "
   stripped_str = str.strip()
   print(stripped_str)  # Output: hello world
   ```

6. **`replace()`**

   - This method returns a copy of the string with all occurrences of a substring replaced by another substring.

   ```python
   str = "hello world"
   replaced_str = str.replace("world", "Python")
   print(replaced_str)  # Output: hello Python
   ```

7. **`split()`**

   - This method returns a list of substrings obtained by splitting the string at occurrences of a delimiter.

   ```python
   str = "hello,world,python"
   split_str = str.split(",")
   print(split_str)  # Output: ['hello', 'world', 'python']
   ```

8. **`join()`**

   - This method concatenates the elements of an iterable with the string as a separator.

   ```python
   list = ['hello', 'world', 'python']
   joined_str = ",".join(list)
   print(joined_str)  # Output: hello,world,python
   ```

9. **`startswith()`**

   - This method returns `True` if the string starts with the specified prefix; otherwise, it returns `False`.

   ```python
   str = "hello world"
   starts_with_hello = str.startswith("hello")
   print(starts_with_hello)  # Output: True
   ```

10. **`endswith()`**

    - This method returns `True` if the string ends with the specified suffix; otherwise, it returns `False`.

    ```python
    str = "hello world"
    ends_with_world = str.endswith("world")
    print(ends_with_world)  # Output: True
    ```

11. **`find()`**

    - This method returns the lowest index of the first occurrence of a substring within the string, or `-1` if the substring is not found.

    ```python
    str = "hello world"
    index_of_world = str.find("world")
    print(index_of_world)  # Output: 6
    ```

12. **`length of String`**

     - In Python, you can calculate the length of a string using the `len()` function. The `len()` function returns the number of characters in a string.

Here's an example:

```python
string = "Hello World"
length = len(string)
print(length)  # Output: 11
```

In this example, the length of the string "Hello World" is 11 characters, including spaces.

13. **`Slicing a String`**

    In Python, you can slice strings using the following syntax:

```python
string[start:end:step]
```

Where:
- `start` is the starting index of the slice (inclusive).
- `end` is the ending index of the slice (exclusive).
- `step` is the step or increment value for the slice (optional).

Here are some examples:

1. **Basic slicing:**

```python
string = "Hello World"
substring = string[3:8]  # Retrieves characters from index 3 to 7 (inclusive start, exclusive end)
print(substring)  # Output: "lo Wo"
```

2. **Negative indices:**

```python
string = "Hello World"
substring = string[-5:-2]  # Retrieves characters from the 5th character from the end to the 2nd character from the end
print(substring)  # Output: "Wor"
```

3. **Omitting start or end indices:**

```python
string = "Hello World"
substring = string[:5]  # Retrieves characters from the beginning to index 4 (exclusive end)
print(substring)  # Output: "Hello"

substring = string[6:]  # Retrieves characters from index 6 to the end
print(substring)  # Output: "World"
```

4. **Reversing the String**

```python
str = "hello world"
reversed_str = str[::-1]
print(reversed_str)  # Output: "dlrow olleh"
```

### Taking user input in python

In Python, you can use the `input()` function to take user input. When `input()` is called, the program pauses and waits for the user to enter something. Once the user presses the "Enter" key, the input is read as a string and can be assigned to a variable.

Here's the basic syntax:

```python
variable_name = input(prompt)
```

- `variable_name` is the variable where you want to store the input from the user.
- `prompt` is an optional argument that you can provide to display a message to the user. This could be a simple instruction like "Enter your name:".

### Example 1: Basic User Input

```python
name = input("Enter your name: ")
print(f"Hello, {name}!")
print("Hello my name is : " + name)
```

In this example, the program will prompt the user to enter their name. After the user enters their name and presses "Enter", the program will greet the user with their name.

### Example 2: Converting User Input

Since `input()` always returns a string, if you expect a numeric value, you need to convert the input to the appropriate data type using functions like `int()` for integers, `float()` for floating-point numbers, etc.

```python
age = input("Enter your age: ")
age = int(age)  # Convert the input string to an integer
print(f"You are {age} years old.")
print("My age is : " , age)
```

Or, you can do the conversion directly in a single line:

```python
age = int(input("Enter your age: "))
print(f"You are {age} years old.")
```

### List in python

List in python is mutable i.e when we modify a List, Changes get reflected in same list and new list is not created. 

1. **`append()`** - Adds an item to the end of the list.

   ```python
   fruits = ['apple', 'banana', 'cherry']
   fruits.append('orange')
   print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']
   ```

2. **`extend()`** - Adds all elements of a list (or any iterable) to the end of the current list.

   ```python
   fruits = ['apple', 'banana', 'cherry']
   more_fruits = ['orange', 'grape', 'pear']
   fruits.extend(more_fruits)
   print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange', 'grape', 'pear']
   ```

3. **`insert()`** - Inserts an item at a specified position.

   ```python
   fruits = ['apple', 'banana', 'cherry']
   fruits.insert(1, 'orange')
   print(fruits)  # Output: ['apple', 'orange', 'banana', 'cherry']
   ```

4. **`remove()`** - Removes the first item from the list whose value is equal to x. Throws a ValueError if the item is not found.

   ```python
   fruits = ['apple', 'banana', 'cherry', 'banana']
   fruits.remove('banana')
   print(fruits)  # Output: ['apple', 'cherry', 'banana']
   ```

5. **`pop()`** - Removes the item at the given position in the list and returns it. If no index is specified, `pop()` removes and returns the last item in the list.

   ```python
   fruits = ['apple', 'banana', 'cherry']
   fruit = fruits.pop()
   print(fruit)  # Output: 'cherry'
   print(fruits)  # Output: ['apple', 'banana']
   ```

6. **`clear()`** - Removes all items from the list.

   ```python
   fruits = ['apple', 'banana', 'cherry']
   fruits.clear()
   print(fruits)  # Output: []
   ```

7. **`index()`** - Returns the index of the first item whose value is equal to x. Throws a ValueError if the item is not found.

   ```python
   fruits = ['apple', 'banana', 'cherry']
   index = fruits.index('banana')
   print(index)  # Output: 1
   ```

8. **`count()`** - Returns the number of times x appears in the list.

   ```python
   fruits = ['apple', 'banana', 'cherry', 'banana']
   count = fruits.count('banana')
   print(count)  # Output: 2
   ```

9. **`sort()`** - Sorts the items of the list in place (the arguments can be used for sort customization).

   ```python
   fruits = ['banana', 'apple', 'cherry']
   fruits.sort()
   print(fruits)  # Output: ['apple', 'banana', 'cherry']
   ```

10. **`reverse()`** - Reverses the elements of the list in place.

    ```python
    fruits = ['banana', 'apple', 'cherry']
    fruits.reverse()
    print(fruits)  # Output: ['cherry', 'apple', 'banana']
    ```

11. **`copy()`** - Returns a shallow copy of the list.

    ```python
    fruits = ['apple', 'banana', 'cherry']
    fruits_copy = fruits.copy()
    print(fruits_copy)  # Output: ['apple', 'banana', 'cherry']
    ```
