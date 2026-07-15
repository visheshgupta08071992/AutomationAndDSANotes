## Understanding Playwright with Python


**Why Playwright?**  

Playwright is a powerful automation tool for web testing and browser automation.

1. **Multi-Language Support:** Playwright supports JavaScript, Python, C#, and Java.
2. **Web & API Testing:** Designed for both web and API testing

3. **Multi-Browser & OS Compatibility:** It supports major browsers like Chrome, Firefox, and WebKit, across Windows, macOS, and Linux.

4. **Automatic Waiting Mechanism:** Playwright automatically waits for elements to be actionable, reducing test flakiness and avoiding manual wait commands.

5. **Inbuilt Logging and Screenshots:** It provides built-in logs and screenshot capabilities, aiding in debugging and capturing detailed trace data for failures.



In the Python ecosystem,pytest serves as a testing framework that allows us to execute Playwright tests using the playwright-pytest plugin. It is similar to TestNg in Java.

<img width="386" height="428" alt="image" src="https://github.com/user-attachments/assets/a8807157-e001-44a7-b633-5227f7681361" />


---

## 1.2 Playwright Architecture vs. Selenium Architecture

To truly understand Playwright's speed and reliability, we have to look under the hood.

### The Old Way: Selenium (HTTP Webdriver Protocol)

Selenium operates on a **request-response model** via the W3C WebDriver standard.

* Every single command you write (e.g., `page.click()`) is serialized into an HTTP REST request.
* It is sent across a network port to a browser-specific driver executable (like `chromedriver.exe`).
* The driver translates it for the browser, executes it, and sends an HTTP response back.

This overhead introduces latency. More importantly, it is **stateless and unidirectional**. Selenium sends a command and hopes the browser is ready. If the browser is in the middle of a JavaScript rerender, Selenium throws an exception unless you have manually littered your code with explicit waits.

### The Modern Way: Playwright (WebSocket over CDP/BiDi)

Playwright completely bypasses the HTTP request-response bottleneck. It establishes a single, persistent **WebSocket connection** directly to the browser’s native debugging engine:

* **Chromium:** Chrome DevTools Protocol (CDP)
* **Firefox:** Firefox DevTools Protocol
* **WebKit:** WebKit's internal debugging protocol

```
[ Your Python Test Script ]
          │
          ▼ (Playwright Library)
   [ Node.js Driver Process ] 
          │
          ▼ ◄─── (Single, Persistent WebSocket Connection)
[ Browser Debug Engine (CDP / Firefox / WebKit) ]

```

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

Install specific browser

```bash
playwright install chromium
```

or

```bash
playwright install firefox
```

or

```bash
playwright install webkit
```

---

Verify installation

```bash
playwright --version
```

---

---
## Playwright Python API Modes

**sync_api** — Synchronous API (simpler for beginners)

**async_api** — Asynchronous API (for concurrency and advanced use)

---

# Launching a Browser in Playwright



---

## 🔹 Example 1: Manual Browser and Context Creation

<img width="994" height="877" alt="image" src="https://github.com/user-attachments/assets/36bfcc9a-78eb-4a9a-992a-3b5eb4a3054d" />


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
- `page.get_by_label("Username:").fill("rahulshettyacademy")` : **-** **Matches a form control by its associated <label>**.


- `page.locator("//input[@type='password']").fill("learning")`  **-** **Using XPATH**
- `page.get_by_role("combobox").select_option("teach")`
- <img width="756" height="286" alt="image" src="https://github.com/user-attachments/assets/f3c267c6-ee1e-477e-8e35-75174e505931" />

- `page.locator("#terms").check()`  **-** **Using CSS**
- `page.get_by_role("button", name="Sign In").click()`
- `page.locator("app-card").filter(has_text="iphone X")`
- `page.get_by_role("link", name="Top").click()`
- `page.get_by_placeholder("Hide/Show Example").click()`
- `page.get_by_text("Hide/Show Example").click()`
- `page.click("text='Login'")`  **- Clicking directly by passing locater**
- `page.fill('input[name="username"]', 'my_user')` **- filling directly by passing locater and value**
-  `page.get_by_role("listitem").filter(has_text="Product A")` **-** **Filter by visible text**
-  `page.get_by_role("listitem").filter(has=page.get_by_role("button", name="Out of stock"))` **-** **Filter by presence of a nested locator**
-  `page.get_by_role("listitem").filter(has_not=page.get_by_role("button", name="Out of stock"))`  **-** **Filter by ABSENCE of a nested locator**
-  `page.get_by_role("listitem").filter(has_not_text="Sold out")`  **-** **Filter by NOT having certain text**


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

<img width="700" height="639" alt="image" src="https://github.com/user-attachments/assets/67ba3920-c851-4fff-a593-33a0f4978822" />


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

<img width="1113" height="781" alt="image" src="https://github.com/user-attachments/assets/d0b7a2e5-f418-4aca-aee2-9b745843c329" />


<img width="996" height="865" alt="image" src="https://github.com/user-attachments/assets/1ef9994f-25ab-4a83-ad39-e710de4f84a2" />



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
These examples demonstrate one of Playwright's most powerful features: **Network Interception**.

Instead of interacting only with the UI, Playwright can intercept HTTP requests made by the browser and allow you to:

* Block requests
* Modify requests
* Mock responses
* Redirect requests
* Monitor network traffic

This is extremely useful for automation testing because you no longer have to depend on the backend.

---

# How Playwright Routing Works

When your application makes an HTTP request, the normal flow is

```
Browser
   │
   ▼
Application
   │
   ▼
HTTP Request
   │
   ▼
Server
   │
HTTP Response
   │
   ▼
Browser UI
```

When using `page.route()`, Playwright inserts itself between the browser and the server.

```
Browser
   │
   ▼
Application
   │
   ▼
Playwright Route
   │
   ├── Continue to server
   ├── Modify request
   ├── Return fake response
   ├── Redirect elsewhere
   └── Abort request
```

Think of it like a security guard standing at the network gate.

---

# Concept 1 : page.route()

```python
page.route(url_pattern, handler)
```

This tells Playwright:

> "Whenever a request matching this URL pattern occurs, don't send it immediately. First give me a chance to inspect or modify it."

Syntax

```python
page.route(
    "url pattern",
    callback_function
)
```

Example

```python
page.route(
    "**/api/users/*",
    intercept
)
```

Whenever any request matches

```
/api/users/123

/api/users/10

/api/users/abc
```

Playwright calls

```python
intercept(route)
```

---

# Example 1 : Mock Response

## Step 1

```python
fakePayloadResponse = {
    "message": "No Product in Cart"
}
```

This is simply fake JSON.

Normally the backend returns something like

```json
{
   "orders":[
      {
         "id":"123",
         "product":"iPhone"
      }
   ]
}
```

Instead, we want to force the application to receive

```json
{
    "message":"No Product in Cart"
}
```

---

## Step 2

```python
page.route(
    "https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*",
    intercept
)
```

This means

Whenever this API is called

```
GET

/api/ecom/order/get-orders-for-customer/12345
```

Don't let it go directly to the server.

Instead call

```python
intercept(route)
```

---

## Step 3

After login

```python
page.get_by_role(
    "button",
    name="ORDERS"
).click()
```

The Orders page automatically makes this API call

```
GET

/api/ecom/order/get-orders-for-customer/<userId>
```

Instead of going to the backend

Playwright intercepts it.

---

## Step 4

```python
def intercept(route):
```

`route` represents the intercepted network request.

Think of it as

```
Request Object
```

containing

* URL
* Headers
* Method
* Body
* Cookies

and methods like

```
continue_()

fulfill()

abort()

fetch()
```

---

## Step 5

```python
route.fulfill(
    json=fakePayloadResponse
)
```

This is the important part.

Instead of sending the request to the server,

Playwright immediately returns

```json
{
   "message":"No Product in Cart"
}
```

The server is never contacted.

Internally

```
Browser
   │
Request
   ▼
Playwright
   │
   ├── Stops request
   │
   └── Returns fake JSON
```

---

## Step 6

The frontend now believes

```
Server responded
```

Although it never did.

Therefore

```python
expect(page.locator(".mt-4"))
```

checks that

```
You have No Orders to show...
```

is displayed.

This is called **API Mocking**.

---

# route.fulfill()

This creates an entire fake HTTP response.

Example

```python
route.fulfill(
    status=200,
    headers={
        "Content-Type":"application/json"
    },
    json={
        "orders":[]
    }
)
```

Equivalent server response

```
HTTP/1.1 200 OK

Content-Type: application/json

{
    "orders":[]
}
```

You can even return HTML

```python
route.fulfill(
    body="<h1>Hello</h1>",
    content_type="text/html"
)
```

---

# Why Mock Responses?

Suppose

Backend is down

```
404

500

Timeout

Database unavailable
```

Without mocking

Your UI test fails.

With mocking

```
Backend ignored

↓

UI tested independently
```

This makes UI automation

* Faster
* Stable
* Predictable

---

# Example 2 : Redirect Request

Here the request is **not mocked**.

Instead

it is redirected.

---

## Original request

When clicking View,

the application normally requests

```
GET

/api/ecom/order/get-orders-details?id=123
```

---

## Route

```python
page.route(
    "https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*",
    intercept
)
```

Intercept this API.

---

## Intercept function

```python
def intercept(route):
```

Again,

Playwright pauses the request.

---

## Continue

```python
route.continue_(
    url="https://rahulshettyacademy.com/client/dashboard/order-details/67d51e0ac019fb1ad62737ed"
)
```

Normally

```
Request

?id=123
```

becomes

```
?id=67d51e0ac019fb1ad62737ed
```

The request is **still sent to the server**, but with a modified URL.

Flow

```
Original Request

↓

Playwright

↓

Modify URL

↓

New URL

↓

Server

↓

Response
```

Unlike `fulfill()`, the server is contacted.

---

# route.continue_()

This means

> "Continue this request after optionally changing something."

You can modify:

```python
route.continue_(
    url="...",
    method="POST",
    headers={},
    post_data="..."
)
```

Example

Original

```
GET

/api/user/1
```

Modified

```
GET

/api/user/2
```

---

# Difference between fulfill() and continue_()

| Feature        | fulfill()                | continue_()                    |
| -------------- | ------------------------ | ------------------------------ |
| Calls server   | ❌ No                     | ✅ Yes                          |
| Fake response  | ✅ Yes                    | ❌ No                           |
| Modify request | ❌ (doesn't send request) | ✅ Yes                          |
| Fast           | ✅                        | Depends on server              |
| Used for       | Mocking                  | Redirecting/modifying requests |

---

# Lifecycle of a Routed Request

```
Application

↓

HTTP Request

↓

page.route()

↓

Handler

↓

Choose one

route.continue_()

↓

Server

↓

Browser
```

OR

```
Application

↓

HTTP Request

↓

page.route()

↓

route.fulfill()

↓

Browser
```

OR

```
Application

↓

HTTP Request

↓

route.abort()

↓

Browser receives failure
```

---

# Other Useful Route APIs

### 1. Abort a request

```python
page.route(
    "**/*.png",
    lambda route: route.abort()
)
```

All PNG images fail to load.

Useful for

* Speeding up tests
* Blocking ads
* Simulating failures

---

### 2. Modify headers

```python
def intercept(route):
    headers = route.request.headers.copy()

    headers["Authorization"] = "Bearer test-token"

    route.continue_(headers=headers)
```

---

### 3. Modify POST data

```python
def intercept(route):
    route.continue_(
        post_data='{"name":"John"}'
    )
```

---

### 4. Read request information

```python
def intercept(route):
    request = route.request

    print(request.url)
    print(request.method)
    print(request.headers)
    print(request.post_data)

    route.continue_()
```

This is useful for debugging or asserting that your application is sending the expected requests.

---

# When Should You Use Each Approach?

| Scenario                                                      | Recommended API                       |
| ------------------------------------------------------------- | ------------------------------------- |
| Test UI without depending on the backend                      | `route.fulfill()`                     |
| Simulate empty orders, server errors, or custom API responses | `route.fulfill()`                     |
| Redirect an API request to a different endpoint               | `route.continue_(url=...)`            |
| Add authentication headers or modify request payloads         | `route.continue_()`                   |
| Block images, CSS, analytics, or third-party requests         | `route.abort()`                       |
| Inspect outgoing requests for validation                      | `route.request` + `route.continue_()` |

## A small correction about the second example

There appears to be an issue in the sample code:

```python
route.continue_(
    url="https://rahulshettyacademy.com/client/dashboard/order-details/67d51e0ac019fb1ad62737ed"
)
```

`route.continue_(url=...)` is intended to modify the **request URL**, so the replacement URL should point to another **API endpoint**, not a web page (`/client/dashboard/...`). If the goal is to fetch details for a different order, the redirected URL would typically be another API URL, for example:

```python
route.continue_(
    url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=67d51e0ac019fb1ad62737ed"
)
```

Redirecting an API request to an HTML page generally won't work as intended because the frontend expects a JSON API response.

These routing capabilities are among the most valuable Playwright features for SDETs because they enable reliable UI testing independent of backend availability, realistic simulation of edge cases that are difficult to reproduce, and comprehensive validation of how applications behave under different network conditions.


---
# Playwright repository for all the above examples

https://github.com/visheshgupta08071992/pythonPlaywrightExamples/tree/master/playwright

---
# Code Generation (Auto Script Recording)

This opens a browser and generates code in real-time as you interact.



```bash

playwright codegen https://example.com


```



