## Database Concepts

Databases are the backbone of every design, no matter the scale, stack, or domain.

If you understand how data is stored, queried, indexed, replicated, and partitioned, you already understand 70% of system design.

Don’t get distracted by every new shiny component; queues, caches, and orchestrators come and go.
But databases are forever.

Every system eventually fails or scales at its data layer first, not its API or cache. That's why strong database design, indexing, and query optimization are the real foundations of scalability.

Anyone can name-drop 'Kafka' or 'Redis.' But the candidates who can have a deep conversation about index trade-offs (e.g., 'read-heavy vs. write-heavy'), isolation levels, and sharding strategies are the ones who can actually be trusted to build a robust system. It does'nt make sense if your algorithmn is o(1) but your query is still scanning the entire table.


### Understanding indexes

Index helps you to find the data faster without scanning the entire table. Indexes make reads faster but writes(Insert/Update/Delete) slower as Indexes also needs to be updated.


There are two types of indexes -

1.Clustered Index
2.Non Clustered Index.


**Clustered Index** - Data is physically sorted based on the Clustered Index. Each table can have only one clustered index because data can only be physically ordered in one way. Most databases automatically make the primary key a clustered index. eg. Dictonary where word are sorted in Alphabetically.


**Non Clustered Index** - Data is not physically sorted instead a separate reference that helps you find the data quickly, Think of it as a book’s index page — it lists the topic and the page number where the topic appears. We can have many non clustered index on a table. Non-clustered indexes for columns that are frequently searched or filtered and are not a Primary key. In our project we had PortfolioID as a clustered Index but generally client used to search Portfolios based on PortfolioName, So we created Non Clustered index on PortfolioName. 



## 🧩 1. Clustered Index

### 🔹 Concept:

A **clustered index** determines **how the data is physically stored** in the table.

* Think of it like a **sorted book** — where the actual **pages (data)** are arranged in order of the index.
* Each table can have **only one clustered index**, because data can only be physically ordered one way.

### 📊 Example:

Let’s say we have a table called `Students`:

| StudentID | Name  | Age | City     |
| --------- | ----- | --- | -------- |
| 103       | John  | 21  | London   |
| 101       | Alice | 20  | New York |
| 102       | Bob   | 22  | Paris    |

Now, if we create a **clustered index** on `StudentID`:

```sql
CREATE CLUSTERED INDEX idx_studentid ON Students(StudentID);
```

Then the **table’s data** will be physically arranged like this:

| StudentID | Name  | Age | City     |
| --------- | ----- | --- | -------- |
| 101       | Alice | 20  | New York |
| 102       | Bob   | 22  | Paris    |
| 103       | John  | 21  | London   |

👉 The data itself is **sorted** and stored in order of `StudentID`.

When you run:

```sql
SELECT * FROM Students WHERE StudentID = 102;
```

The database can directly go to the right place — like opening a sorted book to a known page.

---

## 🧩 2. Non-Clustered Index

### 🔹 Concept:

A **non-clustered index** is like a **separate list** that helps you find data **without changing** how it’s stored.

* Think of it as a **book’s index page** — it lists the topic and the page number where the topic appears.
* You can have **many non-clustered indexes** on a table.

### 📊 Example:

Let’s use the same `Students` table (still physically sorted by `StudentID` due to the clustered index).

Now, create a **non-clustered index** on the `Name` column:

```sql
CREATE NONCLUSTERED INDEX idx_name ON Students(Name);
```

The database will create a **separate structure** that looks like this:

| Name  | Pointer to actual row     |
| ----- | ------------------------- |
| Alice | points to StudentID = 101 |
| Bob   | points to StudentID = 102 |
| John  | points to StudentID = 103 |

So when you run:

```sql
SELECT * FROM Students WHERE Name = 'Bob';
```

👉 The database uses the **non-clustered index** to find that “Bob” corresponds to `StudentID = 102`,
then it goes to the actual table (clustered index) to get the full row.

---

## ⚖️ Summary Table

| Feature                 | Clustered Index                  | Non-Clustered Index                             |
| ----------------------- | -------------------------------- | ----------------------------------------------- |
| Data storage            | Physically rearranges table data | Separate structure                              |
| Number per table        | Only one                         | Many allowed                                    |
| Speed for range queries | Very fast                        | Slower (extra lookup)                           |
| Space usage             | No extra space                   | Requires extra space                            |
| Example use             | Primary key (e.g., ID)           | Frequently searched columns (e.g., Name, Email) |

---

## 🧩 Real-Life Analogy

* **Clustered Index** → Like a phonebook arranged by last name — data itself is in sorted order.
* **Non-Clustered Index** → Like a bookmark list — separate from the actual pages, pointing to where things are.

---

## ✅ Quick Tips

* Most databases automatically make the **primary key** a clustered index.
* Use **non-clustered indexes** for columns often used in `WHERE`, `JOIN`, or `ORDER BY` clauses.
* Too many indexes can **slow down INSERT/UPDATE/DELETE** operations — because each index must also be updated.
* Tip: Measure Selectivity and Frequency

Before creating an index, always ask:

Is this column frequently queried in WHERE, JOIN, or ORDER BY?
→ If yes, consider indexing.

Is this column frequently updated?
→ If yes, avoid indexing it.


----------------------------------------------------------------------------------------------------------------

## All SQL important concepts

https://www.tutorialspoint.com/sql/sql-create-table.html


Let’s break down the **difference between `CHAR` and `VARCHAR`** step-by-step — from basic concept to examples and performance implications 👇

---

## 🧩 1. Basic Definition

| Data Type      | Meaning                                                                                         |
| -------------- | ----------------------------------------------------------------------------------------------- |
| **CHAR(n)**    | Fixed-length character string — always **reserves exactly `n` bytes** (or characters).          |
| **VARCHAR(n)** | Variable-length character string — **uses only as much space as needed**, up to `n` characters. |

---

## 🧠 2. Conceptual Difference

### 🔹 `CHAR(n)` → Fixed-length

* If you declare a column as `CHAR(10)`, it **always takes 10 characters of storage**.
* If you store `'Cat'`, it becomes `'Cat       '` (7 spaces padded to reach length 10).
* Useful when all data values have **uniform length**.

### 🔹 `VARCHAR(n)` → Variable-length

* If you declare a column as `VARCHAR(10)`, and store `'Cat'`, it only uses **3 characters** (plus 1 or 2 bytes for length info).
* Useful when data values **vary in length**.


---

**Understanding Constraints**

🧠 What Are Constraints?

Constraints are rules defined on a table to enforce data integrity — i.e., they ensure that only valid data gets stored in the database.

Common constraints include:

PRIMARY KEY – ensures uniqueness and non-null

UNIQUE – ensures no duplicates

NOT NULL – ensures a column can’t be empty

CHECK – enforces a logical condition

FOREIGN KEY – enforces relationship consistency between tables

<img width="992" height="758" alt="image" src="https://github.com/user-attachments/assets/6a5dd8b2-d47d-4a65-b5c8-14624586faee" />


<img width="1017" height="848" alt="image" src="https://github.com/user-attachments/assets/5f719a62-7bb3-4307-882d-69fc1948ffd4" />



---

## 🧠 1. What is a View?

A **View** in a database is a **virtual table** — it doesn’t store data physically like a real table.
Instead, it’s a **saved SQL query** that dynamically fetches data from one or more tables whenever you access it.

Think of it like:

> “A window (view) that shows data from underlying tables, filtered or joined in a specific way.”

---

## 🧩 2. Why Use Views? (Use Cases)

| Use Case                              | Description                                                                                                 |
| ------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **Data Abstraction / Simplification** | Hide complex joins or logic — users query a simple view instead of writing long SQL.                        |
| **Security**                          | Restrict access to sensitive columns or rows by exposing only what’s needed.                                |
| **Reusability**                       | Save common queries so you don’t repeat them everywhere.                                                    |
| **Logical Independence**              | Applications use the view, not the raw table — so if the table structure changes, you just update the view. |
| **Aggregation / Reporting**           | Create summarized or filtered datasets for dashboards or analytics.                                         |

---

## 🧩 3. Example — Basic Tables

Let’s start with two tables:

```sql
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    Name VARCHAR(50),
    City VARCHAR(50)
);

CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    Amount DECIMAL(10,2),
    OrderDate DATE,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);
```

---

## 🧱 4. CREATE VIEW Syntax

### ✅ Basic Syntax

```sql
CREATE VIEW view_name AS
SELECT columns
FROM table
WHERE condition;
```

### 📘 Example — Simple View

```sql
CREATE VIEW View_Customers_London AS
SELECT CustomerID, Name
FROM Customers
WHERE City = 'London';
```

Now, you can query it like a normal table:

```sql
SELECT * FROM View_Customers_London;
```

✅ This shows only customers from London.

---

### 📘 Example — View with Join

```sql
CREATE VIEW View_CustomerOrders AS
SELECT 
    c.CustomerID,
    c.Name,
    c.City,
    o.OrderID,
    o.Amount,
    o.OrderDate
FROM Customers c
JOIN Orders o ON c.CustomerID = o.CustomerID;
```

Now you can run:

```sql
SELECT * FROM View_CustomerOrders WHERE City = 'Paris';
```

It dynamically fetches matching rows from both tables.

---

## 🧩 5. Updating Data Through a View

Some views are **updatable**, meaning you can use `INSERT`, `UPDATE`, or `DELETE` on them, **but only if**:

* The view is based on **a single table**
* It doesn’t contain **aggregates**, **GROUP BY**, **DISTINCT**, **joins**, or **computed columns**

### Example (Updatable View)

```sql
CREATE VIEW View_CustomerNames AS
SELECT CustomerID, Name FROM Customers;
```

You can do:

```sql
UPDATE View_CustomerNames
SET Name = 'Alice Johnson'
WHERE CustomerID = 1;
```

✅ This will actually update the `Customers` table behind the scenes.

---

### Example (Non-Updatable View)

```sql
CREATE VIEW View_TotalOrders AS
SELECT CustomerID, SUM(Amount) AS TotalSpent
FROM Orders
GROUP BY CustomerID;
```

If you try:

```sql
UPDATE View_TotalOrders SET TotalSpent = 2000 WHERE CustomerID = 1;
```

❌ You’ll get an error — because aggregated views cannot be updated directly.

---

## 🧩 6. ALTER VIEW Syntax

Use `ALTER VIEW` when you want to **change the query definition** of an existing view.

### ✅ Syntax

```sql
ALTER VIEW view_name AS
SELECT columns
FROM tables
WHERE conditions;
```

### 📘 Example

```sql
ALTER VIEW View_Customers_London AS
SELECT CustomerID, Name, City
FROM Customers
WHERE City IN ('London', 'Paris');
```

✅ This modifies the view definition without dropping it.

---

## 🧩 7. DROP VIEW Syntax

Use this to **remove** a view completely.

### ✅ Syntax

```sql
DROP VIEW view_name;
```

### 📘 Example

```sql
DROP VIEW View_CustomerOrders;
```

✅ The view definition is deleted — but **no data** is lost, since the data lives in base tables.

---

## 🧩 8. DELETE Data Through a View

You can delete data **via a view** only if:

* The view references a single base table.
* There’s no aggregation, grouping, or computed columns.

### 📘 Example

```sql
DELETE FROM View_CustomerNames WHERE CustomerID = 5;
```

✅ This will delete the row from the `Customers` table.

---

## 🧩 9. SHOW / LIST Views (Depending on DB)

| Database       | Command                                                                        |
| -------------- | ------------------------------------------------------------------------------ |
| **SQL Server** | `SELECT * FROM sys.views;` or `sp_helptext 'view_name';`                       |
| **MySQL**      | `SHOW FULL TABLES WHERE Table_type = 'VIEW';`                                  |
| **PostgreSQL** | `SELECT table_name FROM information_schema.views WHERE table_schema='public';` |
| **Oracle**     | `SELECT view_name FROM user_views;`                                            |

---

## 🧠 10. Practical Use Cases

| Scenario               | View Example                      | Purpose                             |
| ---------------------- | --------------------------------- | ----------------------------------- |
| **Security**           | Hide salary column in `Employees` | Expose only `Name`, `Department`    |
| **Simplification**     | Join multiple tables              | Make complex queries reusable       |
| **Reports**            | Aggregate sales per region        | Used by BI tools / dashboards       |
| **API / App layer**    | Consistent schema                 | Underlying tables can change freely |
| **Performance tuning** | Pre-filtered subsets              | Reduce read load on full tables     |

---

## 🧩 11. Materialized Views (FYI)

> A **Materialized View** is a **stored snapshot** of the result of a query (not virtual).
> It’s **physically stored** and can be **refreshed periodically**.

Supported in: PostgreSQL, Oracle, etc.
Use it when you have **expensive aggregations** or **reporting queries** that don’t need real-time data.

```sql
CREATE MATERIALIZED VIEW mv_sales_summary AS
SELECT CustomerID, SUM(Amount) AS TotalSpent
FROM Orders
GROUP BY CustomerID;
```

---

## ✅ 12. Summary

| Operation                  | Syntax                                      | Description                     |
| -------------------------- | ------------------------------------------- | ------------------------------- |
| **Create View**            | `CREATE VIEW v AS SELECT ...;`              | Creates a new view              |
| **Alter View**             | `ALTER VIEW v AS SELECT ...;`               | Modify existing view definition |
| **Drop View**              | `DROP VIEW v;`                              | Delete a view definition        |
| **Select from View**       | `SELECT * FROM v;`                          | Query data (like a table)       |
| **Update/Delete via View** | `UPDATE v SET ...;` / `DELETE FROM v;`      | Works only if updatable         |
| **Show Views**             | `SHOW FULL TABLES WHERE Table_type='VIEW';` | List all views                  |

---

## 🧩 13. Real-Life Analogy

Think of a **View** like a **read-only Excel sheet** linked to your raw data:

* You can create different “views” (tabs) showing filtered or summarized info.
* The source data (base tables) stay untouched.
* When data in the base changes, the view shows the latest version automatically.

---


Perfect 👍 — this is one of the **most fundamental** and **powerful** SQL concepts you’ll use in real projects.

Let’s go step-by-step so you understand **what joins are**, **why we use them**, and the **different types of joins** with clear diagrams, syntax, and examples 👇

---

## 🧠 1. What Is a JOIN?

A **JOIN** in SQL is used to **combine rows from two or more tables** based on a **related column** between them — usually a **primary key and foreign key** relationship.

Think of it like:

> “Match rows from Table A with rows from Table B wherever they share a common value.”

---

## 🧩 2. Sample Tables

Let’s use these two simple tables for all our examples 👇

### `Customers` table

| CustomerID | Name    | City   |
| ---------- | ------- | ------ |
| 1          | Alice   | London |
| 2          | Bob     | Paris  |
| 3          | Charlie | Berlin |
| 4          | Diana   | Rome   |

### `Orders` table

| OrderID | CustomerID | Amount |
| ------- | ---------- | ------ |
| 101     | 1          | 200    |
| 102     | 2          | 150    |
| 103     | 2          | 300    |
| 104     | 5          | 400    |

> Notice: CustomerID = 5 in `Orders` doesn’t exist in `Customers`.

---

## 🧩 3. Types of Joins in SQL

There are mainly **five** types of joins you’ll use most often:

| Type                         | Description                                                         |
| ---------------------------- | ------------------------------------------------------------------- |
| **INNER JOIN**               | Returns only matching rows from both tables                         |
| **LEFT JOIN** (LEFT OUTER)   | Returns all rows from the left table + matching rows from the right |
| **RIGHT JOIN** (RIGHT OUTER) | Returns all rows from the right table + matching rows from the left |
| **FULL OUTER JOIN**          | Returns all rows from both tables (matches + non-matches)           |
| **CROSS JOIN**               | Returns all possible combinations (Cartesian product)               |

Let’s look at each with diagrams and examples 👇

---

## 🔹 1. INNER JOIN (Most Common)

**Definition:**
Returns rows that have **matching values** in both tables.

**Syntax:**

```sql
SELECT c.CustomerID, c.Name, o.OrderID, o.Amount
FROM Customers c
INNER JOIN Orders o
ON c.CustomerID = o.CustomerID;
```

**Result:**

| CustomerID | Name  | OrderID | Amount |
| ---------- | ----- | ------- | ------ |
| 1          | Alice | 101     | 200    |
| 2          | Bob   | 102     | 150    |
| 2          | Bob   | 103     | 300    |

🧠 Explanation:

* Only customers who **have placed orders** appear.
* Customer 3 (Charlie) and 4 (Diana) have **no orders**, so they’re excluded.
* Order 104 (CustomerID=5) has no matching customer, so it’s excluded too.

**Diagram:**

```
Customers ●──● Orders
(Returns overlapping area only)
```

---

## 🔹 2. LEFT JOIN (or LEFT OUTER JOIN)

**Definition:**
Returns **all rows from the left table**, plus matching rows from the right table.
If there’s no match, you still get the left table row with **NULLs** for right-side columns.

**Syntax:**

```sql
SELECT c.CustomerID, c.Name, o.OrderID, o.Amount
FROM Customers c
LEFT JOIN Orders o
ON c.CustomerID = o.CustomerID;
```

**Result:**

| CustomerID | Name    | OrderID | Amount |
| ---------- | ------- | ------- | ------ |
| 1          | Alice   | 101     | 200    |
| 2          | Bob     | 102     | 150    |
| 2          | Bob     | 103     | 300    |
| 3          | Charlie | NULL    | NULL   |
| 4          | Diana   | NULL    | NULL   |

🧠 Explanation:

* Includes **all customers**, even those without orders.
* Missing order info is shown as `NULL`.

**Diagram:**

```
(ALL LEFT) ●───● (MATCHED RIGHT)
```

---

## 🔹 3. RIGHT JOIN (or RIGHT OUTER JOIN)

**Definition:**
Returns **all rows from the right table**, plus matching rows from the left table.
If no match, left table columns are `NULL`.

**Syntax:**

```sql
SELECT c.CustomerID, c.Name, o.OrderID, o.Amount
FROM Customers c
RIGHT JOIN Orders o
ON c.CustomerID = o.CustomerID;
```

**Result:**

| CustomerID | Name  | OrderID | Amount |
| ---------- | ----- | ------- | ------ |
| 1          | Alice | 101     | 200    |
| 2          | Bob   | 102     | 150    |
| 2          | Bob   | 103     | 300    |
| NULL       | NULL  | 104     | 400    |

🧠 Explanation:

* Includes **all orders**, even those with no customer record.
* Order 104 (CustomerID=5) appears with `NULL` for customer data.

**Diagram:**

```
(ALL RIGHT) ●───● (MATCHED LEFT)
```

---

## 🔹 4. FULL OUTER JOIN

**Definition:**
Returns **all rows from both tables**, whether they match or not.
If no match, missing values are filled with `NULL`.

**Syntax:**

```sql
SELECT c.CustomerID, c.Name, o.OrderID, o.Amount
FROM Customers c
FULL OUTER JOIN Orders o
ON c.CustomerID = o.CustomerID;
```

**Result:**

| CustomerID | Name    | OrderID | Amount |
| ---------- | ------- | ------- | ------ |
| 1          | Alice   | 101     | 200    |
| 2          | Bob     | 102     | 150    |
| 2          | Bob     | 103     | 300    |
| 3          | Charlie | NULL    | NULL   |
| 4          | Diana   | NULL    | NULL   |
| NULL       | NULL    | 104     | 400    |

🧠 Explanation:

* Combines the results of **LEFT** and **RIGHT** joins.
* You see all customers (even without orders) and all orders (even without customers).

**Diagram:**

```
(ALL LEFT + ALL RIGHT)
```

> ⚠️ Note: Some databases like MySQL don’t directly support `FULL OUTER JOIN`;
> you can simulate it using `UNION` of a LEFT and RIGHT join.

---

## 🔹 5. CROSS JOIN (Cartesian Product)

**Definition:**
Returns **every combination** of rows between both tables.

**Syntax:**

```sql
SELECT c.Name, o.OrderID
FROM Customers c
CROSS JOIN Orders o;
```

**Result (4 Customers × 4 Orders = 16 rows):**

| Name  | OrderID |
| ----- | ------- |
| Alice | 101     |
| Alice | 102     |
| Alice | 103     |
| Alice | 104     |
| Bob   | 101     |
| Bob   | 102     |
| …     | …       |

🧠 Explanation:

* No matching condition — combines **every row from A with every row from B**.
* Useful for generating all possible combinations (e.g., promotions, test data).

**Diagram:**

```
ALL × ALL  (Cartesian product)
```

---

## 🧩 4. SELF JOIN

**Definition:**
Join a table **to itself** — useful for hierarchical data (e.g., employees & managers).

**Example:**

```sql
CREATE TABLE Employees (
    EmpID INT,
    EmpName VARCHAR(50),
    ManagerID INT
);

SELECT 
    e.EmpName AS Employee,
    m.EmpName AS Manager
FROM Employees e
LEFT JOIN Employees m
ON e.ManagerID = m.EmpID;
```

🧠 Explanation:

* The same table is used twice (aliased as `e` and `m`).
* Lets you pair each employee with their manager.

---

## 🧩 5. Summary Table of Joins

| Join Type           | Includes Matching Rows | Includes Non-Matching (Left) | Includes Non-Matching (Right) |
| ------------------- | ---------------------- | ---------------------------- | ----------------------------- |
| **INNER JOIN**      | ✅                      | ❌                            | ❌                             |
| **LEFT JOIN**       | ✅                      | ✅                            | ❌                             |
| **RIGHT JOIN**      | ✅                      | ❌                            | ✅                             |
| **FULL OUTER JOIN** | ✅                      | ✅                            | ✅                             |
| **CROSS JOIN**      | Every combination      | N/A                          | N/A                           |

---

## 💡 6. Real-Life Analogy

Imagine:

* `Customers` = list of people
* `Orders` = list of purchases

| Join Type           | Real-life meaning                              |
| ------------------- | ---------------------------------------------- |
| **INNER JOIN**      | Customers who placed orders                    |
| **LEFT JOIN**       | All customers, even those with no orders       |
| **RIGHT JOIN**      | All orders, even if customer record is missing |
| **FULL OUTER JOIN** | All customers + all orders                     |
| **CROSS JOIN**      | Every possible customer-order pair             |

---

## ✅ 7. Quick Recap Syntax

```sql
-- INNER JOIN
SELECT * FROM A INNER JOIN B ON A.id = B.id;

-- LEFT JOIN
SELECT * FROM A LEFT JOIN B ON A.id = B.id;

-- RIGHT JOIN
SELECT * FROM A RIGHT JOIN B ON A.id = B.id;

-- FULL OUTER JOIN
SELECT * FROM A FULL OUTER JOIN B ON A.id = B.id;

-- CROSS JOIN
SELECT * FROM A CROSS JOIN B;
```

---





