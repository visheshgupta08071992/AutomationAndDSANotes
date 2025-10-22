### Understanding different databases

| Aspect                           | SQL Database           | NoSQL Database          |
|----------------------------------|------------------------|-------------------------|
| **Structure**                    |   Schema is predefined and data is Structured which is stored in Tables having rows and columns                     |     Schema is not predefined and is used to stored unstructured.Four types: Key-Value, Document, Column-Wise, Graph                   |
|                                  |                        |                         |
| **Nature**                       |        Entire data is generally stored on one server and relationship between Tables is maintained using Primary and Foreign Key                |    Distributed nature: Data is distributed across multiple nodes                     |
|                                  |                        |                         |
| **Scalability**                  |      **Vertical Scaling** is readily supported by increasing RAM and storage capacity.</br>**Horizontal Scaling** can be supported with Sharding but it is complex and challenging when compared with NoSQL                |      **Horizontal Scaling** is easily supported by addng more nodes.Well Suited for handling large volume of dynamic data                   |
|                                  |                        |                         |
| **Property (ACID/BASE)**         |       ACID properties (Atomicity, Consistency, Isolation, Durability).                |   BASE properties (Basically Available, Soft State,  Eventually Consistent).                    |
|                                  |                        |                         |
| **When to Choose**               |        1.When your data is well-organized and fits into a structured, tabular format.</br>2.Scalability is not a concern and you are fine with vertical scaling with increased capacity.</br>3.When Data Integrity is Critical:  Applications like financial systems where consistency is paramount.              |     1.When your data is semi-structured or unstructured, and you need flexibility. in the data model.</br>2.Easily supports horizontal scaling by adding more servers to database cluster. </br>3. When Eventual consistency is acceptable. Applications like social networking sites.                 |


### ACID Properties in Databases

1. **Atomicity (A):**
   - **Definition:** Atomicity ensures that a transaction in a database is either fully completed or does'nt happen at all.
   - **Example:** Consider an Example where I am transfering some money to you, It should not happen that Money is  debited from my Account and it is'nt credited in your account, Atomicity would ensure that there is no Partial Transaction, The Transaction would either fully completed or would not happen at all. 

2. **Consistency (C):**
   - **Definition:** Consistency ensures that, at any given point in time, the state of the database is always consistent.
   - **Example:** In a scenario where two requests are trying to read the account balance simultaneously, consistency guarantees that both requests will receive the same value. It prevents situations where simultaneous reads result in different values.

3. **Isolation (I):**
   - **Definition:** Isolation ensures that two transactions do not interfere with each other and each transaction happens independently.
   - **Example:** If a read operation is happening on an account balance while a write operation is simultaneously updating the balance, isolation ensures that the read operation doesn't know about the ongoing write operation. It prevents one transaction from affecting the outcome of another.
   - **Example**:
Let’s say:

You’re transferring ₹100 (Transaction 1)

Someone else is checking your balance (Transaction 2)

If Transaction 2 runs in the middle of Transaction 1, it might see the balance after ₹100 is deducted but before it’s added to the other account — leading to confusion.

4. **Durability (D):**
   - **Definition:** Durability ensures that once a transaction is committed, the changes are permanent and will survive any subsequent failures.
   - **Example:** If you transferred ₹100 and got a success message, that change is permanent.
Even if the power goes out right after, when the system restarts, the database will remember that transaction (thanks to transaction logs).
  

### BASE Properties in NoSQL Databases

**BASE:** Basically Available, Soft state, Eventual Consistency.

**Basically Available**

The term "Basically Available" signifies the high availability of data . Unlike the vertical scaling approach of SQL databases, NoSQL databases grow horizontally storing data on multiple nodes, making it highly available. Even if one node fails, others can seamlessly handle requests, ensuring continuous service.

**Soft State**

Soft State refers that The system’s data can change over time, even without new input.

That’s because in distributed systems, data is often being replicated (copied) across multiple servers — and updates might reach different servers at different times.

The concept of "Soft State" in BASE implies that the state of data can change without requiring an explicit interaction from the user. In a distributed environment, where data is stored across various nodes or servers, each node maintains its version of the data. Through mechanisms like Vector Clocks, nodes automatically synchronize and update themselves. This enables the system to adapt and change data states without direct user interaction, contributing to a dynamic and flexible environment.



**Eventual Consistency**

"Eventual Consistency" acknowledges that, at any given moment, a query might yield stale data. However, over time, as the distributed nodes synchronize, the system strives to converge towards the most up-to-date information. Users may initially receive data that is not the latest, but with subsequent queries, the system aims to provide consistent and current results. This property allows for a balance between availability and consistency in a distributed NoSQL environment.

It's essential to note that BASE properties represent a departure from the strict guarantees of ACID. NoSQL databases prioritize availability and partition tolerance over immediate consistency, making them suitable for scenarios where rapid and scalable data access is critical.

### Types of NoSQL Databases
1. **Key-Value Databases**
   - Data stored as key-value pairs. Only queries on keys are supported. They are often used for Caching purpose.
   - **Example:** Redis, DynamoDB

2. **Document Databases**
   - Stores data in key-value pairs but allows querying on values, typically stored as JSON or XML. Document-oriented databases store data in semi-structured documents, usually in JSON or BSON format. Each document contains key-value pairs or key-document pairs, making them flexible for storing and retrieving complex data structures.
   - **Example:** MongoDB

3. **Column-Wise Databases**
   - Data is stored in columns rather than rows.
   - Each key has a list of column-value pairs. Columns can be dynamic, Some keys can have more no of columns while some keys can have less no og columns.
  
     ![image](https://github.com/visheshgupta08071992/AutomationAndDSANotes/assets/52998083/bf5e3e47-da5e-47bc-9104-7e6ae2cb1d23)

   -  **Example:** Apache Cassandra, HBase

4. **Graph Databases**
   - Data stored in nodes and edges, representing relationships.
   - Ideal for social networks and recommendation engines.


### Reference
  
https://www.youtube.com/watch?v=O_c7lzNbcKo  

https://www.youtube.com/watch?v=hl65apHxp64

https://www.youtube.com/watch?v=fG8c-huFt70
