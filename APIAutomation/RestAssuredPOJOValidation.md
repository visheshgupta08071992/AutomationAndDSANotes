
When using **RestAssured** for API automation and mapping JSON responses to a **POJO (Plain Old Java Object)**, how the mapping behaves depends largely on the JSON content relative to your POJO's structure, and the deserialization engine — typically **Jackson** or **Gson** (RestAssured defaults to Jackson). Here's what happens in both cases you mentioned:

---

## 1. **JSON Response Contains Additional Properties (More than POJO)**

### **Behavior:**

* **By default**, **Jackson** **ignores unknown properties** that are not declared in the POJO.
* This means the extra fields in the JSON response **won't cause an error**, and the known fields (those present in the POJO) will still be populated correctly.

### **Example:**

**JSON Response:**

```json
{
  "id": 1,
  "name": "John",
  "age": 30
}
```

**POJO:**

```java
public class User {
    private int id;
    private String name;

    // getters and setters
}
```

**Result:**

* `id` and `name` are mapped.
* `age` is ignored silently.

### **Approach A: Globally**

## ✅ 1. **Fail on Unknown Properties (No Extra Fields Allowed)**

To ensure that your POJO **does not accept any additional fields**, configure Jackson to **fail on unknown properties**:


```java
ObjectMapper mapper = new ObjectMapper();
mapper.configure(DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES, true);
```

### **Approach B: Per-POJO**

Add this annotation to your POJO:

```java
import com.fasterxml.jackson.annotation.JsonIgnoreProperties;

@JsonIgnoreProperties(ignoreUnknown = false)
public class User {
    private int id;
    private String name;

    // Getters and setters
}
```

> `ignoreUnknown = false` makes Jackson fail if the JSON contains extra fields not in the POJO.

---

## 2. **JSON Response Contains Fewer Properties (Less than POJO)**

### **Behavior:**

* Any fields in the POJO that are **not present in the JSON** will be **set to their default values**.

  * For objects: `null`
  * For primitives: `0`, `false`, etc.

### **Example:**

**JSON Response:**

```json
{
  "id": 1
}
```

**POJO:**

```java
public class User {
    private int id;
    private String name;

    // getters and setters
}
```

**Result:**

* `id` is set to `1`
* `name` is `null`

### **Note:**

This is **safe behavior** and typically doesn't cause issues unless your code expects the missing fields to be non-null or initialized.

---

## Summary Table:

| Scenario                           | Result                               | Configurable?                  |
| ---------------------------------- | ------------------------------------ | ------------------------------ |
| JSON has **additional** properties | Ignored by default                   | Yes, can fail with strict mode |
| JSON has **fewer** properties      | Missing POJO fields = default values | Not typically configurable     |

---
