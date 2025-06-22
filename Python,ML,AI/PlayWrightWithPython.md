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
```bash
#To check which version of python is installed on your machine

python --version

#To check where python exe file is stored after installation

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

```python
 expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
 expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()
 expect(page.locator("//div[@class='media']")).to_have_count(2)
 expect(pageFrame.locator("body")).to_contain_text("Happy Subscibers")
 assert "mentor@rahulshettyacademy.com"  in text
 assert email == "mentor@rahulshettyacademy.com"

```
---

# Playwright Methods on Selectors - Quick Reference

```python
text=childPage.locator(".red").text_content()  #Gives the textContent of Selector

page.locator("//table//thead//tr//th").count() #Gives total matching element against selector
```

---

# Playwright How to handle new page - Quick Reference

```python
def test_childWindowHandle(page:Page):

    with page.expect_popup() as newPage:
        page.goto("https://rahulshettyacademy.com/loginpagePractise/")
        page.locator(".blinkingText").click()
        childPage = newPage.value
        text=childPage.locator(".red").text_content()
        print(text)
        assert "mentor@rahulshettyacademy.com"  in text
        words = text.split("at")
        email = words[1].strip().split(" ")[0]
        assert email == "mentor@rahulshettyacademy.com"

```

---

# Playwright How to handle AlertBox - Quick Reference

```python
def test_UIChecks(page:Page):
    #hide/display and placeholder
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button",name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()

    #Alert boxes
    page.on("dialog",lambda dialog:dialog.accept())
    page.get_by_role("button",name="Confirm").click()
    time.sleep(5)


# The following code listens for any dialog (alert, confirmation, or prompt) that appears on the page.
# It then automatically accepts the dialog.

# page.on("dialog", lambda dialog: dialog.accept())

# Breakdown of the code:

# 1. `page.on("dialog", ...)`
#    - This sets up an event listener on the `page` object.
#    - The `"dialog"` event is triggered whenever an alert, confirmation, or prompt dialog appears.
#    - The second argument is a function (callback) that handles the dialog when it appears.

# 2. `lambda dialog: dialog.accept()`
#    - This is an **anonymous function (lambda function)** in Python.
#    - `dialog` is the parameter representing the dialog box object.
#    - `dialog.accept()` is a method that **automatically clicks "OK" or "Accept"** on the dialog.

# Equivalent Expanded Code:
# Instead of using a lambda function, we can use a normal function:

# def handle_dialog(dialog):
#     dialog.accept()
#
# page.on("dialog", handle_dialog)

# Key Takeaways:
# - The `lambda` function is a compact way to define a function inline.
# - `dialog.accept()` ensures that any alert or confirmation dialog is automatically accepted.
# - If you wanted to **dismiss** the dialog instead of accepting it, you could do:
#
#   page.on("dialog", lambda dialog: dialog.dismiss())


```

---
# Playwright How to Handle Frames - Quick Reference

```python

def test_UIChecks1(page:Page):

    #MouseHover
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.locator("#mousehover").hover()
    page.get_by_role("link",name="Top").click()
    time.sleep(2)

    #Frames: Frames are nothing but child html page embedded in another parent html page
    pageFrame=page.frame_locator("#courses-iframe")
    pageFrame.get_by_role("link",name="All Access plan").click()
    expect(pageFrame.locator("body")).to_contain_text("Happy Subscibers")
    expect(pageFrame.get_by_text("Happy Subscibers!")).to_be_visible()


```

---

# Playwright How to route a request

**Route the request and send a mock dummy response**

```python

from playwright.sync_api import Page, expect , Playwright

from utils.apiBase import APIUtils

fakePayloadResponse= {"message":"No Product in Cart"}


def test_net(page:Page):
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept)
    # rahulshetty@gmail.com
    # Iamking@000
    page.get_by_placeholder("email@example.com").fill("rahulshetty@gmail.com")
    page.locator("#userPassword").fill("Iamking@000")
    page.locator("#login").click()
    page.get_by_role("button", name="ORDERS").click()
    noOrderText=page.locator(".mt-4").text_content()
    print(noOrderText)
    expect(page.locator(".mt-4")).to_have_text("You have No Orders to show at this time. Please Visit Back Us")

def intercept(route):
    route.fulfill(
        json=fakePayloadResponse
    )

```

**Route the request to a new url**

```python
rom playwright.sync_api import Page, expect , Playwright

from utils.apiBase import APIUtils

#https://rahulshettyacademy.com/client/dashboard/order-details/67d51e0ac019fb1ad62737ed

def intercept(route):
    route.continue_(url="https://rahulshettyacademy.com/client/dashboard/order-details/67d51e0ac019fb1ad62737ed")

def test_net2(page:Page):
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", intercept)
    # rahulshetty@gmail.com
    # Iamking@000
    page.get_by_placeholder("email@example.com").fill("rahulshetty@gmail.com")
    page.locator("#userPassword").fill("Iamking@000")
    page.locator("#login").click()
    page.get_by_role("button", name="ORDERS").click()
    page.get_by_role("button",name="View").first.click()
    message = page.locator(".blink_me").text_content()
    print(message)

```


---
# Playwright repository for all the above examples

https://github.com/visheshgupta08071992/pythonPlaywrightExamples/tree/master/playwright

---
# Code Generation (Auto Script Recording)

This opens a browser and generates code in real-time as you interact.



```bash

playwright codegen https://example.com


```



