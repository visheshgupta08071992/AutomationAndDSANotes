
# Question 1 
Suppose implicit wait in selenium is of 10 seconds and explicit webdriverwait is of 5 sec.

What will be the output of my below program if the element is not found for 5 second

WebElement textBoxFill = wait.until(ExpectedConditions.VisibilityOfElementLocated(By.id("abc")));


Let’s break this down step by step 👇

---

### ⚙️ Given

* **Implicit wait** = 10 seconds
* **Explicit wait (WebDriverWait)** = 5 seconds
* Locator: `By.id("abc")`
* Element **is not found for 5 seconds**

---

### 🧠 How Selenium Waits Work

1. **Implicit Wait**

   * Tells WebDriver to poll the DOM for a specified amount of time **when trying to find any element**.
   * Applies globally to all `findElement()` calls.
   * Example: if implicit wait = 10 seconds, `driver.findElement(By.id("abc"))` will keep checking for up to 10 seconds before throwing `NoSuchElementException`.

2. **Explicit Wait**

   * Used for specific conditions (like visibility, clickability, etc.).
   * `WebDriverWait` polls periodically until the condition is true or timeout is reached.
   * Example: `wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("abc")))` waits for **visibility** for up to 5 seconds.

---

### ⚠️ Important Interaction Between Implicit and Explicit Waits

* When both are used **together**, **they add up in an undesirable way**.
* The **explicit wait** internally calls `findElement()` repeatedly.
* Each internal call to `findElement()` is **affected by the implicit wait**.
* So, each poll (usually every 500ms) can itself wait up to **10 seconds** due to the implicit wait.

This causes **unexpectedly long total wait times** — the waits are not cumulative linearly (5 + 10), but multiplicative due to nested waiting.

---

### 🧩 So What Happens in Your Case

* The `WebDriverWait` (5 seconds) will keep polling until timeout.
* Each poll internally calls `driver.findElement(By.id("abc"))`, which itself can wait **up to 10 seconds** (implicit wait).
* As a result, the total time Selenium waits could be **much longer than 5 seconds**, typically close to **10 seconds** or even more depending on polling frequency.

---

### 🧨 Final Outcome

Since the element **is not found at all**:

✅ The program will eventually throw:

```
org.openqa.selenium.TimeoutException: Expected condition failed: waiting for visibility of element located by By.id("abc")
```

🕒 But the **actual wait time** will be around **10 seconds or slightly more**, **not just 5 seconds**, due to the implicit wait being active.

---

### 💡 Best Practice

> **Never mix implicit and explicit waits.**
> It causes unpredictable and inconsistent wait times.

Use **only explicit waits** for controlled and predictable behavior:

```java
driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(0)); // Disable implicit
WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(5));
WebElement textBoxFill = wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("abc")));
```


## ⚙️ Your assumption

> *“Explicit wait should take preference over implicit wait, so total wait should be 5 seconds.”*

Sounds logical, but **that’s not how Selenium actually behaves** under the hood.

---

## 🧩 What Really Happens Internally

When you call:

```java
WebElement textBoxFill = wait.until(
    ExpectedConditions.visibilityOfElementLocated(By.id("abc"))
);
```

the following sequence occurs:

1. The **explicit wait (WebDriverWait)** runs for up to **5 seconds**, polling every 500 ms by default.
2. Each time it polls, it internally calls:

   ```java
   driver.findElement(By.id("abc"))
   ```
3. But since **implicit wait = 10 seconds**,
   each `findElement()` call itself can take **up to 10 seconds** before throwing `NoSuchElementException`.

So effectively, each poll can **block for up to 10 seconds**.
And because `WebDriverWait` expects the `findElement()` call to finish before checking again,
the **explicit wait’s 5-second timeout** only starts counting *after each `findElement()` returns or fails*.

That’s why Selenium documentation explicitly warns that:

> 🔸 Mixing implicit and explicit waits can cause unpredictable wait times.

---

## 🕒 Practical Outcome in Your Case

* **Implicit wait:** 10 s
* **Explicit wait:** 5 s
* **Element never appears**

➡️ You will get

```text
TimeoutException: Expected condition failed: waiting for visibility of element located by By.id("abc")
```

✅ **Exception type:** `TimeoutException`
❌ **Not** `NoSuchElementException`

But ⏱ the **real wait time** will be **around 10 seconds (or slightly more)**,
**not 5 seconds**, because implicit wait affects every internal `findElement()` call.

---

## 🧠 Key Insight

* Selenium does **not “prioritize”** explicit wait over implicit wait.
* Both are **active at the same time**, and the implicit wait slows down each poll of the explicit wait.
* The explicit wait doesn’t *cancel* or *override* the implicit wait duration.

---

## ✅ Best Practice

To avoid confusion and unpredictable timing:

```java
driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(0));  // Disable implicit wait
WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(5));
wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("abc")));
```

Now the timeout will be **exactly 5 seconds**, as you’d intuitively expect.

---

# Question 2

I have map in java as below with key as Vishesh and value as 1 as shown below

Vishesh  1

How can I get the value of first key if dont know the keyID

Good question 👏 — this is a subtle one about how **maps** work in Java.
Let’s go step by step.

---

## 🧩 Problem

You have a map like:

```java
Map<String, Integer> map = new HashMap<>();
map.put("Vishesh", 1);
```

Now you want to **get the value of the first key**,
but you **don’t know the key name** (`"Vishesh"`).

---

## ⚠️ Important: Maps Don’t Have “Order” (in `HashMap`)

A `HashMap` **does not guarantee order** — meaning:

* The concept of *“first key”* doesn’t exist.
* The iteration order can change depending on hash codes and resizing.

So if you truly need “first key,” you must use an **ordered map** (like `LinkedHashMap` or `TreeMap`).

But let’s handle both cases 👇

---

## ✅ Case 1: If You’re Using `HashMap`

You can **get any one key-value pair** (e.g., the first returned during iteration):

```java
Map<String, Integer> map = new HashMap<>();
map.put("Vishesh", 1);

if (!map.isEmpty()) {
    Map.Entry<String, Integer> entry = map.entrySet().iterator().next();
    System.out.println("Key: " + entry.getKey());
    System.out.println("Value: " + entry.getValue());
}
```

### Output

```
Key: Vishesh
Value: 1
```

> ⚠️ Note: This works but is **not guaranteed to always return the same entry**
> if your map has multiple keys — order is not fixed.

---

## ✅ Case 2: If You Want a *Predictable “First” Key*

Use a **`LinkedHashMap`**, which maintains insertion order:

```java
Map<String, Integer> map = new LinkedHashMap<>();
map.put("Vishesh", 1);
map.put("John", 2);

Map.Entry<String, Integer> firstEntry = map.entrySet().iterator().next();
System.out.println(firstEntry.getKey() + " = " + firstEntry.getValue());
```

### Output

```
Vishesh = 1
```

✅ In this case, the “first” key means the **first inserted** key, and it’s guaranteed.

---

## ✅ Java 8 Stream Alternative (works on all Map types)

If you just want to quickly grab the first entry:

```java
Map.Entry<String, Integer> firstEntry = map.entrySet().stream().findFirst().orElse(null);
if (firstEntry != null) {
    System.out.println(firstEntry.getKey() + " = " + firstEntry.getValue());
}
```

---

## 🧠 Summary

| Scenario                      | Recommended Map Type | Code to Get First Value            | Order Guaranteed?     |
| ----------------------------- | -------------------- | ---------------------------------- | --------------------- |
| You just want any value       | `HashMap`            | `map.entrySet().iterator().next()` | ❌ No                  |
| You want *first inserted* key | `LinkedHashMap`      | Same code                          | ✅ Yes                 |
| You want sorted by key        | `TreeMap`            | Same code                          | ✅ Yes (sorted by key) |

---





