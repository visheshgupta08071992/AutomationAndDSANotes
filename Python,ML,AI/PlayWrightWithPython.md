## Understanding Playwright with Python


**Why Playwright?**  

Playwright is a powerful automation tool for web testing and browser automation.

1. **Multi-Language Support:** Playwright supports JavaScript, Python, C#, and Java.
2. **Web & API Testing:** Designed for both web and API testing

3. **Multi-Browser & OS Compatibility:** It supports major browsers like Chrome, Firefox, and WebKit, across Windows, macOS, and Linux.

4. **Automatic Waiting Mechanism:** Playwright automatically waits for elements to be actionable, reducing test flakiness and avoiding manual wait commands.

5. **Inbuilt Logging and Screenshots:** It provides built-in logs and screenshot capabilities, aiding in debugging and capturing detailed trace data for failures.



In the Python ecosystem,pytest serves as a testing framework that allows us to execute Playwright tests using the playwright-pytest plugin. It is similar to TestNg in Java.

---

## Steps to Install Playwright with Python

1.Install python
```
To check which version of python is installed on your machine

python --version

To check where python exe file is stored after installation

where python
```
2.Install Pytest - **pip install pytest** </br>
3.Install Pytest playwright plugin - **pip install pytest-playwright** </br>
4.Install required browsers supported by playwright - **playwright install** </br>

---
## Playwright Python API Modes

**sync_api** — Synchronous API (simpler for beginners)

**async_api** — Asynchronous API (for concurrency and advanced use)

---

# Launching a Browser in Playwright



---

## 🔹 Example 1: Manual Browser and Context Creation

```python
from playwright.sync_api import Playwright                # Playwright is class in playwright.sync_api package

def test_playwrightBasics(playwright: Playwright):        # playwright is the instance of Playwright driver
    browser = playwright.chromium.launch(headless=False)  # Launches a Chromium browser with GUI
    #browser=playwright.firefox.launch(headless=False)    # To Launch Firefox browser
    #browser=playwright.webkit.launch(headless=False)     # To Launch webkit  browser
    context = browser.new_context()                       # Creates a new browser context (like a new browser profile)
    page = context.new_page()                             # Opens a new tab/page in the context
    page.goto("https://www.linkedin.com/feed/")           # Navigates to LinkedIn
```


## 🔹 Example 2: Using a Fixture - Page Shortcut

```python
from playwright.sync_api import Page                # Page is class in playwright.sync_api package
def test_playwrightShortCut(page: Page):            # page is the instrance of Playwright Page.
    page.goto("https://www.linkedin.com/feed/")     # Navigates to LinkedIn
    page.screenshot(path="example.png")             # Takes a screenshot of the current page
```

### ✅ Key Concepts

* **`page: Page`**: This is usually provided by a pytest fixture (`pytest-playwright` plugin).
* Automatically handles launching a browser, creating context, and opening a page.


---

# Playwright Page Methods - Quick Reference


- `page.goto("https://www.linkedin.com/feed/")`
- `page.screenshot(path="example.png")`
- `page.screenshot(path="fullpage.png", full_page=True)`
- `page.get_by_label("Username:").fill("rahulshettyacademy")`
- `page.locator("//input[@type='password']").fill("learning")`  **-** **Using XPATH**
- `page.get_by_role("combobox").select_option("teach")`
- `page.locator("#terms").check()`  **-** **Using CSS**
- `page.get_by_role("button", name="Sign In").click()`
- `page.locator("app-card").filter(has_text="iphone X")`
- `page.get_by_role("link", name="Top").click()`
- `page.get_by_placeholder("Hide/Show Example").click()`
- `page.get_by_text("Hide/Show Example").click()`
- `page.click("text='Login'")`  **- Clicking directly by passing locater**
- `page.fill('input[name="username"]', 'my_user')` **- filling directly by passing locater and value**

---

# Playwright Assertions - Quick Reference

```
 expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
 expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()
 expect(page.locator("//div[@class='media']")).to_have_count(2)
 expect(pageFrame.locator("body")).to_contain_text("Happy Subscibers")
 assert "mentor@rahulshettyacademy.com"  in text
 assert email == "mentor@rahulshettyacademy.com"

``python




