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
   - **Definition:** Isolation ensures that two transactions do not interfere with each other.
   - **Example:** If a read operation is happening on an account balance while a write operation is simultaneously updating the balance, isolation ensures that the read operation doesn't know about the ongoing write operation. It prevents one transaction from affecting the outcome of another.

4. **Durability (D):**
   - **Definition:** Durability ensures that once a transaction is committed, the changes are permanent and will survive any subsequent failures.
   - **Example:** Durability is achieved through mechanisms like logging and persistence to disk storage. It ensures that the data and details of updates are securely stored, even in the event of a system failure.


### Reference
  
https://www.youtube.com/watch?v=O_c7lzNbcKo  

https://www.youtube.com/watch?v=hl65apHxp64

https://www.youtube.com/watch?v=fG8c-huFt70
