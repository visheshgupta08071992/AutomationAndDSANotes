## Understanding Pytest

# Pytest Comprehensive Notes

## Introduction to Pytest
Pytest is a powerful testing framework for Python that makes it easy to write simple and scalable test cases. It is widely used due to its simplicity, ease of use, and rich feature set.

## Installation and checking version
You can install pytest using pip:
```bash
pip install pytest
```

```
pytest --version
```

## Test Discovery
Pytest automatically discovers tests by looking for files that start with `test_` or end with `_test.py`. Inside those files, it looks for functions that start with `test_`.


## Writing Your First Test
Create a file named `test_sample.py` and add the following code:
```python
def test_addition():
    assert 1 + 1 == 2

def test_subtraction():
    assert 2 - 1 == 1
```

To run the tests, execute the following command in your terminal:
```bash
pytest
```

or

```
pytest test_sample.py

```

## Assertions
Pytest uses simple `assert` statements to check if a condition is true.
```python
def test_string():
    assert "hello".upper() == "HELLO" # Pass
    assert "pytest" in "pytest framework"  # Pass
    assert [1, 2, 3] == [1, 2, 3]  # Pass

def test_failing():
    assert 1 == 2  # Fails
    
```


In **pytest**, when an assertion fails, the test function immediately stops execution, and pytest marks the test as **failed**.  Consider below example

```python
assert "hello".upper() == "HELLOE"  # This will fail
assert "pytest" in "pytest framework"  # Pass
assert [1, 2, 3] == [1, 2, 3]  # Pass

```

Then the next assertions:

```python
assert "pytest" in "pytest framework"  # Not executed
assert [1, 2, 3] == [1, 2, 3]  # Not executed
```

will **not be executed** because pytest stops running the test function as soon as it encounters a failed assertion.

### Solution: Using `pytest.mark.parametrize` or `pytest.check`
If you want **all assertions to be evaluated** even if some fail, you can use:

1. **`pytest.mark.parametrize`** – Useful for independent test cases:
   ```python
   import pytest

   @pytest.mark.parametrize("actual, expected", [
       ("hello".upper(), "HELLOE"),
       ("pytest" in "pytest framework", True),
       ([1, 2, 3], [1, 2, 3])
   ])
   def test_multiple_cases(actual, expected):
       assert actual == expected
   ```

2. **`pytest-check`** – Allows multiple assertions within a single test function without stopping:
   ```python
   import pytest_check as check

   def test_string():
       check.equal("hello".upper(), "HELLOE")  # Fails but doesn't stop
       check.is_in("pytest", "pytest framework")  # Still executed
       check.equal([1, 2, 3], [1, 2, 3])  # Still executed
   ```
   Install `pytest-check` with:
   ```
   pip install pytest-check
   ```

This way, all assertions will run, and you can see **all failures** in one test execution. 🚀



## Fixtures
Fixtures are used to set up some context before a test runs. They help manage test setup and teardown just like @Before and @After in TestNg .They can be defined using the `@pytest.fixture` decorator.
```python
import pytest

@pytest.fixture
def sample_list():
    return [1, 2, 3, 4, 5]

def test_sample_list_length(sample_list):
    assert len(sample_list) == 5
```

```python
import pytest

@pytest.fixture()
def setup():
    print("I will be executing first")  #setup
    yield  # pauses the execution and allows the test to run
    print("I will execute last") #TearDown

def test_fixtureDemo(setup):
    print("I will execute steps in fixtureDemo method")
```

### Explanation:
1. **Fixture (`setup` function)**:
   - The `@pytest.fixture()` decorator defines `setup` as a pytest fixture.
   - The first `print` statement executes before the test.
   - `yield` temporarily pauses execution and allows the test to run.
   - After the test completes, the execution resumes after `yield`, running the second `print` statement.

2. **Test Function (`test_fixtureDemo`)**:
   - The function `test_fixtureDemo` takes `setup` as an argument, meaning it will execute the `setup` fixture before running.
   - The test prints its statement while the fixture is active.

### Expected Output:
When running `pytest -s` (to allow print statements):
```
I will be executing first
I will execute steps in fixtureDemo method
I will execute last
```

Would you like me to explain more about pytest fixtures or add enhancements? 🚀



## Parameterized Tests
You can use the `@pytest.mark.parametrize` decorator to run a test with different sets of data.
```python
import pytest

@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 2),
    (2, 3, 5),
    (4, 5, 9)
])
def test_addition(a, b, expected):
    assert a + b == expected
```

## Running Specific Tests
You can run specific tests by specifying the file name or the test name.
```bash
pytest test_sample.py
pytest test_sample.py::test_addition
```

## Markers
Markers are used to group tests or to add metadata to tests. You can define custom markers and use built-in markers.
```python
import pytest

@pytest.mark.slow
def test_slow_function():
    import time
    time.sleep(5)
    assert True
```

Run tests with a specific marker:
```bash
pytest -m slow
```

## Skipping Tests
You can skip tests using the `@pytest.mark.skip` decorator or the `pytest.skip` function.
```python
import pytest

@pytest.mark.skip(reason="Skipping this test for now")
def test_not_ready():
    assert False
```

## Expected Failures
You can mark a test as an expected failure using the `@pytest.mark.xfail` decorator.
```python
import pytest

@pytest.mark.xfail
def test_expected_failure():
    assert False
```

## Fixtures with Scope
Fixtures can have different scopes such as `function`, `class`, `module`, and `session`.


**function** : A fixture with scope function would be executed before each test method and if yield is also provided then it would be executed after each test method.<\br>

**class** : A fixture with scope class would be executed before all test method defined in class and if yield is also provided then it would be executed after all test method defined within class.<\br>

**module** : A fixture with module function would be executed before all test method defined in module and if yield is also provided then it would be executed after all test method defined within method.<\br>

**session** : A fixture with session function would be executed before all test method running in session and if yield is also provided then it would be executed after all test method running in session.<\br>



```

Syntax
@pytest.fixture(scope="function")
@pytest.fixture(scope="module")
@pytest.fixture(scope="class")
@pytest.fixture(scope="session")

```


```python
import pytest

@pytest.fixture(scope="module")
def db_connection():
    connection = create_db_connection()
    yield connection
    connection.close()
```


## Understanding conftest.py file :
we can define the fixture in conftest.py file and then the fixture defined in conftest.py file can be chained to any test within any testfile. It is beneficial to keep a fixture in conftest file when you think that a particular fixture would be shared by tests in multiple files.
The workflow is that first the test tries to find a fixture in its own local file if it is not found in its own local file then it checks the given fixture in conftest file


## Understanding Paramterized fixtures

Parameterized fixtures in pytest, useful for running the same test with multiple values.

The provided code demonstrates **parameterized fixtures** in pytest, useful for running the same test with multiple values.

### **Understanding the Code**

#### **1. Fixture with Parameterization**
```python
import pytest

@pytest.fixture(params=["chrome", "Firefox", "IE"])
def crossBrowser(request):
    return request.param
```
- The `params` argument in `@pytest.fixture` allows the test to run multiple times with different values.
- Here, the test will execute **three times**, once for each browser (`"chrome"`, `"Firefox"`, `"IE"`).
- `request.param` provides the current parameter value.

#### **2. Test Function Using the Fixture**
```python
def test_crossBrowser(crossBrowser):
    print(crossBrowser)
```
- This test function takes the `crossBrowser` fixture as an argument.
- The fixture injects one of the browser names into the test.
- It will print the browser name for each execution.

### **How the Tests Run**
Executing:
```bash
pytest -s
```
will output:
```
chrome
Firefox
IE
```
(`-s` ensures print statements are shown in the console.)


## Understanding @pytest.mark.usefixtures("fixtureName")

@pytest.mark.usefixtures("fixtureName"): The given annotation is used applied over a class to apply a fixture to all methods within the class


```python
import pytest

@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixtureDemo(self):
        print("I will execute steps in fixtureDemo method")

    def test_fixtureDemo1(self):
        print("I will execute steps in fixtureDemo1 method")

    def test_fixtureDemo2(self):
        print("I will execute steps in fixtureDemo2 method")

    def test_fixtureDemo3(self):
        print("I will execute steps in fixtureDemo3 method")
```

### Explanation:

1. **`@pytest.mark.usefixtures("setup")`**:
   - This applies the `"setup"` fixture to all methods in the `TestExample` class.
   - This means the `setup` fixture will run before each test method.

2. **Class-Based Test Approach**:
   - The class `TestExample` contains multiple test methods.
   - Each test method (`test_fixtureDemo`, `test_fixtureDemo1`, etc.) prints a message.

3. **Fixture Execution**:
   - The `"setup"` fixture (defined separately, but assumed to be available) will run **before each** test method in the class.
   - If `setup` contains a `yield` statement, the code after `yield` will execute **after each** test.

### Expected Output (if using a `setup` fixture like before):

```plaintext
I will be executing first
I will execute steps in fixtureDemo method
I will execute last

I will be executing first
I will execute steps in fixtureDemo1 method
I will execute last

I will be executing first
I will execute steps in fixtureDemo2 method
I will execute last

I will be executing first
I will execute steps in fixtureDemo3 method
I will execute last
```


## General Summary


1.Run all the tests : pytest

2.Run specific test : pytest testFileName

3.Run specific function of specific test : pytest testFileName:functionName

4.Run all Test with matching keyword: pytest -k "addition"    (Note:Here matching keyword is addition,So it would run all tests which has addition in its name)

5.Run test such that it prints metadata and logs of test : pytest -v -s  (Note -v is used add more data about test and -s is used to print log specifically print statement)

6.You can mark(tag) tests with @pytest.mark.markName eg  @pytest.mark.smoke and then run with commnand pytest -m smoke. It would run all tests which are marked as smoke.

7.When a test is annotated with @pytest.mark.skip it would skip the test.

8.You can mark a test as an expected failure using the @pytest.mark.xfail decorator.

9.fixtures are used as setup and teardown method for testcases. Fixtures can have different scopes such as function, class, module, and session.






