# Python Interview Questions

**1. What is the difference between a list and a tuple?**

```python
# Lists are mutable, tuples are imutable

eg.
list = [1,2,3]
list[0] = 100
print(list) #[100,2,3]

tuple = (1,2,3)
tuple[0] = 100 # Given operation is not supported and would result in TypeError with message tuple object does not support item assignment while running the program
print(tuple) #Error would be thrown

```


2. What are Python’s built-in data types?
3. How do you implement inheritance and the `super` keyword in Python?
4. What is `__init__()` in Python?
5. How do you read and write files in Python?
6. What are Fixtures in Pytest? When are they used?
7. How do you use `yield` for WebDriver setup and teardown in Pytest?
8. How do you create a list of dictionaries in Python?
9. What is a lambda function in Python?
10. How does a lambda function apply to `map()` & `filter()` functions?
11. How do you sort a list in Python?
12. Is Python asynchronous or synchronous by default? What is `asyncio`?
13. Why is the `self` convention used in Python? Explain with an example.
14. How do you reverse the elements of a list?
15. Explain the difference between `@classmethod` and instance methods.
16. What is the use of `conftest.py` in Python Pytest?
17. How do you execute only failed test cases in Pytest?
18. How do you apply a custom marker to a test case in Pytest?
19. What is the Python `with` statement designed for?
20. How do you handle exceptions in Python? Where does the `finally` keyword come into play?
