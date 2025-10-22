## Database Concepts

Databases are the backbone of every design, no matter the scale, stack, or domain.

If you understand how data is stored, queried, indexed, replicated, and partitioned, you already understand 70% of system design.

Don’t get distracted by every new shiny component; queues, caches, and orchestrators come and go.
But databases are forever.

Every system eventually fails or scales at its data layer first, not its API or cache. That's why strong database design, indexing, and query optimization are the real foundations of scalability.

Anyone can name-drop 'Kafka' or 'Redis.' But the candidates who can have a deep conversation about index trade-offs (e.g., 'read-heavy vs. write-heavy'), isolation levels, and sharding strategies are the ones who can actually be trusted to build a robust system. 


### Understanding indexes

Index helps you to find the data faster without scanning the entire table


There are two types of indexes -

1.Clustered Index
2.Non Clustered Index.


**Clustered Index** - Data is physically sorted based on the Clustered Index. Each table can have only one clustered index because data can only be physically ordered in one way. Most databases automatically make the primary key a clustered index. eg. Dictonary where word are sorted in Alphabetically.


**Non Clustered Index** - Data is not physically sorted instead a separate reference that helps you find the data quickly, Think of it as a book’s index page — it lists the topic and the page number where the topic appears. We can have many non clustered index on a table.



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



