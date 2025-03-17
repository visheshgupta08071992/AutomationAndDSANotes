## Understanding Python

### Basics of Python

Pycharm is IDE which is mostly used for coding in Python While PIP(Python Package Index) is used to download and use external packages in Python. It is similar to maven or gradle in Java.


### To check which version of python is installed on your machine

Type below command within command prompt

```python --version```

### To check where python exe file is stored after installation

```where python```

### **Steps to Ensure While Setting or Creating a Project in PyCharm**

#### **1. Create a New Project**
- Open PyCharm.
- Click on **File** → **New Project**.

![image](https://github.com/user-attachments/assets/61ed7dbc-9fa6-40cc-a02e-50e72be93021)

---

#### **2. Configure Project Name, Location, and Python Interpreter**
- **Project Name:** Provide a meaningful name for your project.
- **Location:** Specifies where PyCharm will store your project files.
- **Interpreter Type:** Choose the Python interpreter that PyCharm will use.

##### **Choosing the Right Interpreter:**
- You can either create a **new virtual environment** or use an **existing one**.
- **Recommended:** Use an **existing** Python which you have installed on your machine for better control over dependencies.
  - Select **custom environment**
  - Select **Existing Interpreter**.
  - Provide the path to your Python executable.  
  - You can find the Python executable path by running the following command in the terminal:
    ```
    where python
    ```
  - Providing a custom interpreter ensures that when you install Python packages via the command line (`pip install <package_name>`), they will be available in your PyCharm project.

![image](https://github.com/user-attachments/assets/4b16aecc-fada-4ce1-9378-64c244786ee3)

---

#### **3. Verify the Python Interpreter Configuration**
After creating the project, verify that the selected interpreter is correctly set:
- **Go to** `File` → `Settings` → `Project` → `Python Interpreter`
- Ensure that the Python path points to the desired environment (custom or system-wide).
- You can also see the installed packages here.

---


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

### Undestanding what dataType value our variable is storing
we can use type function to get the dataType of value which variable is storing

```python
a=1
b=2.2
c=False
d="Hello"

print(type(a)) # <class 'int'>
print(type(b)) # <class 'float'>
print(type(c)) # <class 'bool'>
print(type(d)) # <class 'str'>

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

In Python, you can manage package dependencies using `pip`, which is the package installer for Python. To update a particular package using `pip`, we can follow these steps:

### Updating a Package with `pip`

1. **Check the Current Version**: First, you might want to check the current version of the package you have installed. You can do this by running:
   ```bash
   pip show package_name
   ```

2. **Update the Package**: To update a specific package to the latest version, you can use the following command:
   ```bash
   pip install --upgrade package_name
   ```

   If you want to update to a specific version, you can specify the version number:
   ```bash
   pip install package_name==version_number
   ```

### Example

For example, if you want to update the `requests` package to the latest version, you would run:
```bash
pip install --upgrade requests
```

If you want to update it to a specific version, say `2.25.1`, you would run:
```bash
pip install requests==2.25.1
```

### Using a Requirements File

If you are managing multiple dependencies, you might have a `requirements.txt` file, similar to Maven's `pom.xml`. You can specify the package versions in this file. For example:

```
requests==2.25.1
numpy>=1.19.0
```

To update the packages listed in `requirements.txt`, you can run:
```bash
pip install -r requirements.txt --upgrade
```

### Summary

- Use `pip install --upgrade package_name` to update to the latest version.
- Use `pip install package_name==version_number` to update to a specific version.
- Use a `requirements.txt` file to manage multiple dependencies and their versions.

This approach is somewhat analogous to updating dependencies in a `pom.xml` file in Maven, where you specify the versions of the libraries you want to use.


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

13.**`Checking whether one string is present in another`**

```python
  str = "Hello Hi"
  str1 = "Hi"

 print(str1 in str) # True
```

14. **`Slicing a String`**

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

List in python is mutable i.e when we modify a List, Changes get reflected in same list and new list is not created. List allows values of different dataType.

```python

a = [1,"Hello",3,4.5]
print(a)  # [1, 'Hello', 3, 4.5]

# Providing -1 Returns value of last index
print(a[-1]) # 4.5

# Returns value of last index
print(a[3]) # 4.5

#Updating value
a[1] ="Hi"
print(a) # [1, 'Hi', 3, 4.5]

#Deleting a value

del a[2]
print(a) # [1, 'Hi', 4.5]

```

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

11. **`sort(reverse=true)`** - Sort the list in descending order
    ```python
    fruits = ['banana', 'apple', 'cherry']
    fruits.sort(reverse=True)
    print(fruits)  # Output: ['cherry', 'banana', 'apple']
    ```

12. **`reverse()`** - Reverses the elements of the list in place.

    ```python
    fruits = ['banana', 'apple', 'cherry']
    fruits.reverse()
    print(fruits)  # Output: ['cherry', 'apple', 'banana']
    ```

13. **`copy()`** - Returns a shallow copy of the list.

    ```python
    fruits = ['apple', 'banana', 'cherry']
    fruits_copy = fruits.copy()
    print(fruits_copy)  # Output: ['apple', 'banana', 'cherry']
    ```
14. **`slicing a list`** - Is used to slice a list and return a new list

    ```python
    fruits = ['apple', 'banana', 'cherry']
    newFruits = fruits[0:1]
    print(newFruits) # Output: ['apple']
    ```

### Tuples in python

Tuples are a fundamental data type in Python that are quite similar to lists with a crucial difference: tuples are immutable. This immutability means that once a tuple is created, the elements inside it cannot be changed, removed, or added. In contrast, lists are mutable, allowing for modification of their elements.

### Tuple Definition and Usage

A tuple is defined by enclosing its elements within parentheses `()`, whereas a list is defined with square brackets `[]`.

**Tuple Example:**

```python
my_tuple = (1, 2, 3, 4)
print(my_tuple)  # Output: (1, 2, 3, 4)
```

**List Example:**

```python
my_list = [1, 2, 3, 4]
print(my_list)  # Output: [1, 2, 3, 4]
```

### Immutability of Tuples

Due to their immutability, tuples do not support operations that alter them, such as `append()`, `remove()`, or `pop()`, which are available with lists. This immutability makes tuples a preferred choice for fixed data that should not change throughout the execution of a program, ensuring data integrity and potentially optimizing memory usage and performance.

### When to Use Tuples

- When the collection of items is not going to change.
- To use as keys in dictionaries (because keys must be immutable in Python).
- When passing a sequence of values to a function where you don't want those values to be altered.

### Commonly Used Tuple Methods

Tuples have fewer methods compared to lists, primarily because of their immutability. The two most commonly used tuple methods are:

1. **`count()`** - Returns the number of times a specified value occurs in a tuple.

   **Example:**

   ```python
   my_tuple = (1, 4, 3, 7, 4, 2, 4)
   print(my_tuple.count(4))  # Output: 3
   ```

   Here, `my_tuple.count(4)` returns `3` because the value `4` appears three times in the tuple.

2. **`index()`** - Searches the tuple for a specified value and returns the position of where it was found.

   **Example:**

   ```python
   my_tuple = (1, 2, 3, 4, 5)
   print(my_tuple.index(3))  # Output: 2
   ```

   `my_tuple.index(3)` returns `2`, indicating that the value `3` is located at index 2 in the tuple.

### Difference from Lists

- **Immutability**: The key difference is that tuples are immutable, while lists are mutable.
- **Syntax**: Tuples use parentheses `()`; lists use square brackets `[]`.
- **Performance**: Tuples can be slightly faster than lists for certain operations due to their immutability.
- **Usage**: Tuples are used for data that should remain constant throughout the program, while lists are used for data that can change.


 ### Sets in Python

 Sets in Python can be created using the set() constructor or by placing all the elements within curly braces {}.

```python
my_set = {1, 2, 3}
print(my_set)

# Using the set() constructor to create a set
my_set2 = set([1, 2, 2, 3, 4])  # Duplicate values will be removed
print(my_set2)
```

Here are some commonly used set methods in Python, along with examples:


**`add()`**: Adds a single element to the set.

```python
my_set = {1, 2, 3, 4, 5}
my_set.add(6)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}
```

**`update()`**: Adds multiple elements to the set. You can pass a list, tuple, string, or another set as the argument.

```python
my_set.update([7, 8, 9])
print(my_set)  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9}
```

**`remove()`**: Removes a specific element from the set. Raises a KeyError if the element is not found.

```python
my_set.remove(9)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}
```

**`discard()`**: Removes a specific element from the set. Does not raise an error if the element is not found.

```python
my_set.discard(8)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6, 7}
```

**`pop()`**: Removes and returns an arbitrary element from the set. Since sets are unordered, you do not know which item that gets removed.

```python
element = my_set.pop()
print(element)  # Output: Can be any element from the set
print(my_set)  # The set without the removed element
```

**`clear()`**: Removes all elements from the set.

```python
my_set.clear()
print(my_set)  # Output: set()
```

**`union()`**: Returns a set that is the union of two sets.

```python
A = {1, 2, 3}
B = {3, 4, 5}
C = A.union(B)
print(C)  # Output: {1, 2, 3, 4, 5}
```

**`intersection()`**: Returns a set that is the intersection of two sets.

```python
D = A.intersection(B)
print(D)  # Output: {3}
```


### Dictionary in Python

In Python, a dictionary is a collection of items that are stored in a key-value pair. It is simialr to Map in Java

Here are some of the commonly used dictionary methods in Python with examples:


**`Creates a new dictionary.`**

Example:
```python
new_dict = dict(name="rahul", hobby="playing")
print(new_dict)  # Output: {'name': 'rahul', 'hobby': 'playing'}

new_dict= {"name":"sachin","hobby":"sports"}
print(new_dict)  # Output: {'name': 'sachin', 'hobby': 'sports'}
```

**`.get(key, default=None)`**
Returns the value for a key if the key is in the dictionary, else `default`.

Example:
```python
my_dict = {'name': 'Alice', 'age': 25}
print(my_dict.get('name'))  # Output: Alice
print(my_dict.get('location', 'Unknown'))  # Output: Unknown
print(my_dict['age']) # Output: 25
```

**`.keys()`**
Returns a view object that displays a list of all the keys.

Example:
```python
my_dict = {'name': 'Alice', 'age': 25}
print(list(my_dict.keys()))  # Output: ['name', 'age']
```

**`.values()`**
Returns a view object that displays a list of all the values.

Example:
```python
my_dict = {'name': 'Alice', 'age': 25}
print(list(my_dict.values()))  # Output: ['Alice', 25]
```

**`.items()`**
Returns a view object that displays a list of a dictionary's key-value tuple pairs.

Example:
```python
my_dict = {'name': 'Alice', 'age': 25}
print(list(my_dict.items()))  # Output: [('name', 'Alice'), ('age', 25)]
```

**`.update([other])`**
Updates the dictionary with the key/value pairs from `other`, overwriting existing keys.

Example:
```python
my_dict = {'name': 'Alice', 'age': 25}
my_dict.update({'age': 26, 'location': 'New York'})
print(my_dict)  # Output: {'name': 'Alice', 'age': 26, 'location': 'New York'}
my_dict["Country"]="USA"
my_dict["age"]=25
print(my_dict) # Output: {'name': 'Alice', 'age': 25, 'location': 'New York', 'Country': 'USA'}
```

**`.pop(key[, default])`**
Removes the item with the specified key and returns its value. If the key does not exist and `default` is specified, it returns `default`, otherwise it raises a `KeyError`.

Example:
```python
my_dict = {'name': 'Alice', 'age': 25}
print(my_dict.pop('age'))  # Output: 25
print(my_dict)  # Output: {'name': 'Alice'}
```

**`.clear()`**
Removes all items from the dictionary.

Example:
```python
my_dict = {'name': 'Alice', 'age': 25}
my_dict.clear()
print(my_dict)  # Output: {}
```

**`.copy()`**
Returns a shallow copy of the dictionary.

Example:
```python
original = {'name': 'Alice', 'age': 25}
new_dict = original.copy()
print(new_dict)  # Output: {'name': 'Alice', 'age': 25}
```

### If Else in Python
Please find below basic if else program in python. In : represents indentation, It is similar to braces in Java.

```python
age = int(input("Please enter your age : "))

if (age >= 18):
    print("you can drive car")
elif(age >=10):
    print("you can drive cycle")
else:
    print("You need to walk")

```

### Iteration in python

The general syntax of a for loop in Python is:

```python

for item in iterable:
    # code block to execute for each item

```

**`Iterating List and set`**

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

my_set = {"apple", "banana", "cherry"}

for item in my_set:
    print(item)
```

**`Iterating dictionary`** 

```python

person = {"name": "John", "age": 30, "city": "New York"}

for key, value in person.items():
    print(key, ":", value)


person = {"name": "John", "age": 30, "city": "New York"}

for key in person.keys():
    print(key, ":", person[key])


person = {"name": "John", "age": 30, "city": "New York"}

for value in person.values():
    print(value)


```

Your understanding of the `range` function in Python is correct! Here’s a refined version with additional details and an example for better clarity.

---

**Iterating Using `range()` Function in Python**
</br>
In Java, a `for` loop is written as:
```java
for(int i = 0; i < 5; i++) {
    System.out.println(i);
}
```
In Python, the equivalent loop can be achieved using the `range()` function:
```python
for i in range(0, 5):  # 0 is inclusive, 5 is exclusive
    print(i)
```
This will output:
```
0
1
2
3
4
```

---

### **Understanding `range(start, stop, step)`**
The `range()` function in Python can take up to three arguments:
```python
range(start, stop, step)
```
- **`start`**: The starting number (inclusive, defaults to `0` if not provided).
- **`stop`**: The stopping number (exclusive).
- **`step`**: The step value (optional, defaults to `1`).

---

### **Examples of `range()`**
#### **1. Basic Iteration**
```python
for i in range(5):  # Equivalent to range(0,5)
    print(i)
```
**Output:**
```
0
1
2
3
4
```

#### **2. Using a Step Value**
```python
for i in range(0, 10, 2):  # Start at 0, go up to 10 (exclusive), increment by 2
    print(i)
```
**Output:**
```
0
2
4
6
8
```

#### **3. Iterating in Reverse**
```python
for i in range(5, 0, -1):  # Start at 5, decrement by 1 until 0 (exclusive)
    print(i)
```
**Output:**
```
5
4
3
2
1
```

**8. How do you create a list of dictionaries in Python?**

```python
list = [
         {"name":"A","age":1},
         {"name":"B","age":2},
         {"name":"C","age":3},
         {"name":"D","age":4}
        ]


print(list[1]['age']) # 2
print(list[2].get('age')) # 3

for item in list:
    print(item)
    print(f"Name: {item['name']}, Age: {item['age']}")

#Output    
#{'name': 'A', 'age': 1}
#Name: A, Age: 1
#{'name': 'B', 'age': 2}
#Name: B, Age: 2
#{'name': 'C', 'age': 3}
#Name: C, Age: 3
#{'name': 'D', 'age': 4}
#Name: D, Age: 4

```

**9.How do you create a list of tuple in Python?**

```python

list = [
         ("A",1),
         ("B",2),
         ("C",3),
         ("D",4)
        ]


print(list[1]) # ('B',2)
print(list[1][0]) # (B)

for key,value in list:
    print(f"Key: {key} and value : {value} ")

#Output    
#Key: A and value : 1 
#Key: B and value : 2 
#Key: C and value : 3 
#Key: D and value : 4 

```

### **Lambda Function in Python**
A **lambda function** in Python is an **anonymous function** (a function without a name). It is defined using the `lambda` keyword and can have multiple arguments but only a single expression.

Lambda functions are often used for **short, simple functions** that are used temporarily in a program, especially as arguments to higher-order functions like `map()`, `filter()`, and `sorted()`.

---

### **Syntax of Lambda Function**
```python
lambda arguments: expression
```
- `lambda` - keyword to define the lambda function.
- `arguments` - input parameters (can be multiple, separated by commas).
- `expression` - a single expression whose result is returned automatically.

---

### **Example 1: Basic Lambda Function**
```python
square = lambda x: x ** 2
print(square(5))  # Output: 25
```
Here, `square` is a lambda function that takes `x` as an argument and returns `x ** 2`.

---

### **Example 2: Lambda with Multiple Arguments**
```python
add = lambda a, b: a + b
print(add(3, 7))  # Output: 10
```
This lambda function takes two arguments and returns their sum.

---

### **Example 3: Using Lambda in `map()`**
```python
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
```
Here, `map()` applies the lambda function to each element of the list.

---

### **Example 4: Using Lambda in `filter()`**
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6, 8]
```
Here, `filter()` selects only the even numbers from the list.

---

### **Example 5: Using Lambda in `sorted()`**
```python
students = [("Alice", 25), ("Bob", 20), ("Charlie", 22)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)
# Output: [('Bob', 20), ('Charlie', 22), ('Alice', 25)]

Here, the list of tuples is sorted based on the second value (age).

num =[3,2,6,1]
print(sorted(num))

# Output: [1,2,3,6]
```
List.sort() sorts the list itself while sorted function returns a new sorted list

---

### **When to Use Lambda Functions**
- When you need a small function temporarily.
- When passing a function as an argument to another function (`map()`, `filter()`, etc.).
- When defining simple functions in a concise way.

### **When NOT to Use Lambda Functions**
- If the function is complex and needs multiple expressions/statements.
- If the function needs to be reused multiple times (better to use `def` instead).
  
Would you like more advanced examples? 😊


### Exception handling in Python

Exception handling in Python is done using the `try`, `except`, `else`, and `finally` blocks. Here’s a simple breakdown:

- **`try`**: This block lets you test a block of code for errors.
- **`except`**: Here, you handle the error.
- **`else`**: If there is no error, this block of code can run.
- **`finally`**: This block of code runs regardless of the result of the try- and except blocks, often used for cleaning up resources.

### Basic Example
Here's a basic example to show how these blocks work together:

```python
try:
    # Code block where you suspect an error might occur
    result = 10 / 0
except ZeroDivisionError:
    # What to do if there is a ZeroDivisionError
    print("You can't divide by zero!")
else:
    # Executes if the try block succeeds
    print("Division successful!")
finally:
    # This code block always executes
    print("Operation complete.")
```

### Catching Multiple Exceptions
You can catch multiple exceptions by specifying them as a tuple after `except` or by having multiple `except` blocks:

```python
try:
    value = int(input("Please enter a number: "))
    result = 10 / value
except (ValueError, ZeroDivisionError) as e:
    # Handles both ValueError and ZeroDivisionError
    print(f"An error occurred: {e}")
```

### Generic Exception Handling
For catching any exception (which is not generally recommended unless you're logging errors or need to catch a broad range of issues), you can use `except Exception as e`, which catches all "exception" instances but not system-exiting exceptions:

```python
try:
    # risky code
    result = 10 / 0
except Exception as e:
    print(f"An error occurred: {e}")
```

### Custom Exceptions
You can define your own exceptions by extending the `Exception` class. This can be useful for creating meaningful error messages or handling specific error cases in your application:

```python
class MyCustomError(Exception):
    """Exception raised for custom purposes."""
    def __init__(self, message):
        self.message = message

try:
    raise MyCustomError("Something went wrong!")
except MyCustomError as e:
    print(e.message)
```

### File I/O in python

File I/O (Input/Output) in Python is quite straightforward and is primarily handled through the built-in `open()` function, which returns a file object. This object can then be used to read from or write to a file. The basic operations involve opening a file, reading or writing to it, and then closing it.

**`Opening a File`**
To open a file, you use the `open()` function. It requires the name of the file you want to open and also takes a mode as a second argument, determining the action (read, write, append, etc.) to be performed on the file:

- `'r'`: Open for reading (default).
- `'w'`: Open for writing, truncating the file first.
- `'x'`: Open for exclusive creation, failing if the file already exists.
- `'a'`: Open for writing, appending to the end of the file if it exists.
- `'b'`: Binary mode.
- `'t'`: Text mode (default).
- `'+'`: Open for updating (reading and writing).

**`Reading from a File`**
To read the content of a file:

```python
# Open the file in read mode ('r' is default so it can be omitted)
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
```

The `with` statement is used here to ensure that the file is properly closed after its suite finishes, even if an exception is raised. The `read()` method reads the entire file content.

If you want to read the file line by line:

```python
with open('example.txt', 'r') as file:
    for line in file:
        print(line, end='')
```

**readLines function**
In Python, the readlines() function is used to read all the lines of a file and return them as a list of string

```python

# read the file and store all the lines in list
# reverse the list
# write the list back to the file

with open(‘test.txt', 'r') as reader:
    content = reader.readlines()  # [abc, bvdsf, cat, dog, elephant]
    content.reverse()  # [elephant, dog, cat, bvdsf, abc]

    with open('test1.txt', 'w') as writer:
      for line in content:
        writer.write(line)


```

**`Writing to a File`**
To write to a file, you open it in write (`'w'`) or append (`'a'`) mode:

```python
# This will overwrite the file if it exists, or create it if it doesn't
with open('example.txt', 'w') as file:
    file.write("Hello, World!\n")
    file.write("This is another line.\n")
```

To append to a file, change the mode to `'a'`:

```python
with open('example.txt', 'a') as file:
    file.write("Appending a new line.\n")
```

**`Binary Mode`**
For binary files, you should add `'b'` to the mode string. This is useful for non-text files like images or executables:

```python
# Reading a binary file
with open('image.png', 'rb') as file:
    content = file.read()

# Writing to a binary file
with open('copy_image.png', 'wb') as file:
    file.write(content)
```

**`Closing Files`**
When you’re done with a file, you need to close it to free up system resources. The `with` statement does this automatically for you. However, if you open a file without `with`, you should close it manually:

```python
file = open('example.txt', 'r')
content = file.read()
print(content)
file.close()  # It's important to close the file
```

Remember, handling files properly is important to prevent data loss or corruption. Always make sure files are closed after their use is complete, preferably using the `with` statement for its automatic handling of resource management.


 ### Understanding class and constructor in python

 A constructor in python always has name **__init__()**. It is automatically executed when an object of the class is created. self parameter is similar to this in java which refers to the current instance of a class and it is mandatory parameter within constructor and all methods within the class.self should always be the first parameter within constructor and instance methods.It is not required to pass self parameter explicitly when calling methods.

 ```python

class Person:
    country = "India"
    def __init__(self, name, age):  # Constructor
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age} , Country : {Person.country}")

# Creating an object of the class
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

# Calling the method
person1.display()  # Name: Alice, Age: 25 , Country : India
person2.display()  # Name: Bob, Age: 30 , Country : India

```

### **Inheritance in Python**
Inheritance is a fundamental concept in Object-Oriented Programming (OOP) that allows a class (child class) to inherit attributes and methods from another class (parent class). This promotes code reusability and modularity.

---

## **1. Types of Inheritance in Python**
Python supports several types of inheritance:
1. **Single Inheritance** (One parent → One child)
2. **Multiple Inheritance** (Multiple parents → One child)
3. **Multilevel Inheritance** (Parent → Child → Grandchild)
4. **Hierarchical Inheritance** (One parent → Multiple children)
5. **Hybrid Inheritance** (Combination of multiple types)

---

## **2. Syntax of Inheritance**
```python
class ParentClass:
    # Parent class attributes and methods
    pass

class ChildClass(ParentClass):
    # Child class inherits from ParentClass
    pass
```

---

## **3. Example of Single Inheritance**
```python
# Parent Class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

# Child Class (Inheriting from Animal)
class Dog(Animal):
    def speak(self):  # Method Overriding
        print(f"{self.name} barks.")

# Creating an object of the child class
dog = Dog("Buddy")
dog.speak()
```
### **Output:**
```
Buddy barks.
```
### **Explanation:**
1. The `Animal` class has an `__init__()` constructor and a `speak()` method.
2. The `Dog` class inherits from `Animal` and overrides the `speak()` method.
3. When calling `dog.speak()`, the overridden method in `Dog` is executed.

---

## **4. Example of Multiple Inheritance**
In **multiple inheritance**, a child class can inherit from multiple parent classes.
```python
# Parent Class 1
class Father:
    def skills(self):
        print("Father: Good at Math.")

# Parent Class 2
class Mother:
    def skills(self):
        print("Mother: Good at Cooking.")

# Child Class (Inheriting from both Father and Mother)
class Child(Father, Mother):
    def own_skill(self):
        print("Child: Good at Painting.")

# Creating an object of Child class
c = Child()
c.skills()  # Calls the first inherited class's method (Father)
c.own_skill()
```
### **Output:**
```
Father: Good at Math.
Child: Good at Painting.
```
**Note:** Python follows the **Method Resolution Order (MRO)**, where it looks for methods in the first inherited class (`Father`) before the second (`Mother`). If you want to access both parent methods, you can call them explicitly.

```python
class Child(Father, Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("Child: Good at Painting.")
```

---

## **5. Example of Multilevel Inheritance**
In **multilevel inheritance**, a child class inherits from another child class.
```python
# Grandparent Class
class Grandparent:
    def grandparent_method(self):
        print("This is Grandparent's method.")

# Parent Class (Inheriting from Grandparent)
class Parent(Grandparent):
    def parent_method(self):
        print("This is Parent's method.")

# Child Class (Inheriting from Parent)
class Child(Parent):
    def child_method(self):
        print("This is Child's method.")

# Creating an object of Child class
c = Child()
c.grandparent_method()
c.parent_method()
c.child_method()
```
### **Output:**
```
This is Grandparent's method.
This is Parent's method.
This is Child's method.
```

---

## **6. Example of Hierarchical Inheritance**
In **hierarchical inheritance**, multiple child classes inherit from the same parent class.
```python
# Parent Class
class Vehicle:
    def vehicle_info(self):
        print("This is a vehicle.")

# Child Class 1
class Car(Vehicle):
    def car_info(self):
        print("This is a car.")

# Child Class 2
class Bike(Vehicle):
    def bike_info(self):
        print("This is a bike.")

# Creating objects
car = Car()
bike = Bike()

car.vehicle_info()
car.car_info()

bike.vehicle_info()
bike.bike_info()
```
### **Output:**
```
This is a vehicle.
This is a car.
This is a vehicle.
This is a bike.
```

---

## **7. Using `super()` to Call Parent Methods**
The `super()` function is used to call methods from the parent class.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Calling Parent Constructor
        self.breed = breed

    def speak(self):
        super().speak()  # Calling Parent Method
        print(f"{self.name} is a {self.breed} and barks.")

# Creating object
dog = Dog("Buddy", "Labrador")
dog.speak()
```
### **Output:**
```
Buddy makes a sound.
Buddy is a Labrador and barks.
```

---

## **Summary**
| Inheritance Type       | Description |
|------------------------|-------------|
| **Single Inheritance** | One child class inherits from one parent class. |
| **Multiple Inheritance** | A child class inherits from multiple parent classes. |
| **Multilevel Inheritance** | A child class inherits from a parent class, which in turn inherits from another class. |
| **Hierarchical Inheritance** | One parent class has multiple child classes. |
| **Hybrid Inheritance** | A mix of two or more inheritance types. |

---

