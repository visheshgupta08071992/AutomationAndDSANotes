# Pytest Comprehensive Notes

## 1. Introduction to Pytest
Pytest is a powerful testing framework for Python that makes it easy to write simple and scalable test cases. It is widely used due to its simplicity, ease of use, and rich feature set.

### Installation and Checking Version
You can install pytest using pip:
```bash
pip install pytest
```
Check the installed version:
```bash
pytest --version
```

## 2. Test Discovery and Execution
Pytest automatically discovers tests by looking for files that start with `test_` or end with `_test.py`. Inside those files, it looks for functions that start with `test_`.

### Running Tests
To run all tests:
```bash
pytest
```
To run a specific test file:
```bash
pytest test_sample.py
```
To run a specific test function within a file:
```bash
pytest test_sample.py::test_addition
```
To run tests matching a keyword:
```bash
pytest -k "addition"
```
To print logs and detailed metadata:
```bash
pytest -v -s
```

## 3. Writing Test Cases
### Basic Test
Create a file named `test_sample.py` and add the following code:
```python
def test_addition():
    assert 1 + 1 == 2

def test_subtraction():
    assert 2 - 1 == 1
```

### Assertions in Pytest
Pytest uses simple `assert` statements to check conditions.
```python
def test_string():
    assert "hello".upper() == "HELLO"
    assert "pytest" in "pytest framework"
    assert [1, 2, 3] == [1, 2, 3]
```

### Handling Multiple Assertions
By default, Pytest stops execution on the first failed assertion. To evaluate all assertions:
#### Using `pytest.mark.parametrize`
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
#### Using `pytest-check`
```python
import pytest_check as check

def test_string():
    check.equal("hello".upper(), "HELLOE")  # Fails but continues
    check.is_in("pytest", "pytest framework")
    check.equal([1, 2, 3], [1, 2, 3])
```
Install `pytest-check` with:
```bash
pip install pytest-check
```

## 4. Fixtures
Fixtures are function that manage setup and teardown for tests. They are defined using `@pytest.fixture`.
```python
import pytest

@pytest.fixture
def sample_list():
    return [1, 2, 3, 4, 5]

def test_sample_list_length(sample_list):
    assert len(sample_list) == 5
```

### Fixture with Setup and Teardown
```python
import pytest

@pytest.fixture()
def setup():
    print("Setup execution")
    yield  # Pauses execution
    print("Teardown execution")

def test_fixture_demo(setup):
    print("Executing test function")
```
**Execution Order:**
```
Setup execution
Executing test function
Teardown execution
```

### Fixture Scope
Fixtures can have different scopes:
- `function`: Executed before and after each test.
- `class`: Executed once per test class.
- `module`: Executed once per module.
- `session`: Executed once per test session.

```python
@pytest.fixture(scope="module")
def db_connection():
    connection = create_db_connection()
    yield connection
    connection.close()
```

## 5. Parameterized Tests
You can use `@pytest.mark.parametrize` to run tests with multiple inputs.
```python
import pytest

@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 2),
    (2, 3, 5),
    (4, 5, 9)
])
def test_addition(a, b, expected):
    assert a + b == expected


@pytest.mark.parametrize("x, y, expected", [
    (1, 2, 3),  
    (0, 5, 5),  
    (-1, 1, 0),  
    (10, 20, 30)
])
def test_add(x, y, expected):
    assert add(x, y) == expected

@pytest.mark.parametrize("input_string, expected", [
    ("hello", "olleh"),
    ("pytest", "tsetyp"),
    ("12345", "54321"),
    ("", "")  # Edge case: empty string
])
def test_reverse_string(input_string, expected):
    assert reverse_string(input_string) == expected


@pytest.mark.parametrize("a, b, expected", [
    (10, 2, True),  
    (10, 3, False),  
    (15, 5, True),  
    (17, 4, False)
])
def test_is_divisible(a, b, expected):
    assert is_divisible(a, b) == expected

```

## 6. Using `conftest.py` for Shared Fixtures
Fixtures can be placed in `conftest.py` to be available across multiple test files.

## 7. Marking and Skipping Tests
### Using Markers
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

### Skipping Tests
```python
@pytest.mark.skip(reason="Skipping this test for now")
def test_not_ready():
    assert False
```

### Expected Failures
```python
@pytest.mark.xfail
def test_expected_failure():
    assert False
```

## 8. Parameterized Fixtures
Fixtures can also be parameterized to run tests with multiple values.
```python
import pytest

@pytest.fixture(params=["chrome", "Firefox", "IE"])
def cross_browser(request):
    return request.param

def test_cross_browser(cross_browser):
    print(cross_browser)
```
Running:
```bash
pytest -s
```
Outputs:
```
chrome
Firefox
IE
```

## 9. Using `@pytest.mark.usefixtures`
Apply a fixture to all test methods in a class.
```python
import pytest

@pytest.mark.usefixtures("setup")
class TestExample:
    def test_case1(self):
        print("Executing case 1")
    def test_case2(self):
        print("Executing case 2")
```

## 10. How do you execute only failed test cases in pytest

```bash

pytest --last-failed

```

What the above commad does is it checks the pytest report of last run and reexecutes all the failed tests.

## 11. Summary of Pytest Commands
1. Run all tests: `pytest`
2. Run a specific test file: `pytest testFileName`
3. Run a specific function in a test file: `pytest testFileName.py::functionName`
4. Run tests matching a keyword: `pytest -k "keyword"`
5. Run tests with detailed logs: `pytest -v -s`
6. Run tests with a specific marker: `pytest -m markerName`
7. Skip a test using `@pytest.mark.skip`
8. Mark a test as expected failure using `@pytest.mark.xfail`
9. Use fixtures for setup and teardown, with various scopes (`function`, `class`, `module`, `session`).
10. Run only failed tests: `pytest --last-failed`
