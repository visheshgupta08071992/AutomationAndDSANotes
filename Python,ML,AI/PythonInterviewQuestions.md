# Python Interview Questions

**1. What is the difference between a list and a tuple?**

```python
# Lists are mutable, tuples are imutable
# This immutability means that once a tuple is created, the elements inside it cannot be changed, removed, or added. In contrast, lists are mutable, allowing for modification of their elements.

# A tuple is defined by enclosing its elements within parentheses (), whereas a list is defined with square brackets [].

eg.
list = [1,2,3]
list[0] = 100
print(list) #[100,2,3]

tuple = (1,2,3)
tuple[0] = 100 # Given operation is not supported and would result in TypeError with message tuple object does not support item assignment while running the program
print(tuple) #Error would be thrown

```

**2. What are Python’s built-in data types?**

```python
# int,float,double,bool,str,list,tuple,dict
```

**3. How do you implement inheritance and the `super` keyword in Python?**

4. What is `__init__()` in Python?
5. How do you read and write files in Python?
6. What are Fixtures in Pytest? When are they used?
7. How do you use `yield` for WebDriver setup and teardown in Pytest?</br>

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

10. What is a lambda function in Python?
11. How does a lambda function apply to `map()` & `filter()` functions?
12. How do you sort a list in Python?
**13. Is Python asynchronous or synchronous by default? What is `asyncio`?**

```
By Default Python is Synchronous

- Python executes code **line by line** in a **blocking** manner.
- Each operation must complete before the next one starts.
- This is how Python **normally** works unless explicitly told to run asynchronously.

**Python Supports Asynchronous Execution Using asyncio**  
- Python can run **non-blocking tasks** using **asyncio**.  
- Instead of waiting for one task to finish, multiple tasks **run concurrently**.  

```    
14. Why is the `self` convention used in Python? Explain with an example.
15. How do you reverse the elements of a list?
16. Explain the difference between `@classmethod` and instance methods.
17. What is the use of `conftest.py` in Python Pytest? - In Pytest, the conftest.py file is a special configuration file used to share fixtures, hooks, and configuration across multiple test files in a directory (and its subdirectories).
18. How do you execute only failed test cases in Pytest?
19. How do you apply a custom marker to a test case in Pytest?
20. What is the Python `with` statement designed for?

    ![image](https://github.com/user-attachments/assets/0760356e-81c2-43f3-b667-44605bc7e5b0)

22. How do you handle exceptions in Python? Where does the `finally` keyword come into play?
