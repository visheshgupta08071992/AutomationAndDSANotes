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
```python
import pytest

@pytest.fixture(scope="module")
def db_connection():
    connection = create_db_connection()
    yield connection
    connection.close()
```

## Temporary Directories
Pytest provides a built-in fixture `tmpdir` to create temporary directories for tests.
```python
def test_temp_file(tmpdir):
    temp_file = tmpdir.join("test.txt")
    temp_file.write("Hello, World!")
    assert temp_file.read() == "Hello, World!"
```

## Capturing Output
Pytest can capture output from print statements and log messages.
```python
def test_output(capsys):
    print("Hello, Pytest!")
    captured = capsys.readouterr()
    assert captured.out == "Hello, Pytest!\n"
```

## Plugins
Pytest has a rich ecosystem of plugins that extend its functionality. Some popular plugins include:
- `pytest-cov`: For measuring test coverage.
- `pytest-mock`: For mocking objects in tests.
- `pytest-django`: For testing Django applications.

Install plugins using pip:
```bash
pip install pytest-cov pytest-mock pytest-django
```

## Running Tests with Coverage
Use the `pytest-cov` plugin to measure test coverage.
```bash
pytest --cov=my_project
```

## Mocking
Use the `pytest-mock` plugin to mock objects in your tests.
```python
def test_mocking(mocker):
    mock = mocker.patch('my_module.my_function')
    mock.return_value = "mocked value"
    assert my_module.my_function() == "mocked value"
```

## Testing Django Applications
Use the `pytest-django` plugin to test Django applications.
```python
import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_view(client):
    response = client.get(reverse('my_view'))
    assert response.status_code == 200
```

## Debugging Tests
You can use the `--pdb` option to drop into the Python debugger on test failure.
```bash
pytest --pdb
```

## Summary
Pytest is a versatile and powerful testing framework for Python. With its simple syntax, powerful fixtures, and rich ecosystem of plugins, it makes testing easier and more enjoyable. These notes cover the basics, but pytest has many more features to explore. Happy testing!
