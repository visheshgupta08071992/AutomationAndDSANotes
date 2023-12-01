### Understanding CAP Therom

# CAP Theorem in Distributed Computing

The **CAP theorem** is a concept in distributed computing that highlights the trade-offs between three desirable properties in a distributed system: **Consistency**, **Availability**, and **Partition Tolerance**.

Here's a brief explanation of each term:

- **Consistency (C):** All nodes in a distributed system have the same data at the same time. In other words, when a write operation is completed, all subsequent read operations will return the updated data.

- **Availability (A):** Every request to the system receives a response, without a guarantee that it contains the most recent version of the information. Availability, in this context, means that every node (or server) in the system is responsive.

- **Partition Tolerance (P):** The system continues to operate even when network partitions occur, meaning communication between nodes is unreliable or delayed. Partition tolerance is crucial for systems that need to withstand network failures.

The CAP theorem posits that in a distributed system, it's impossible to achieve all three properties simultaneously. According to the theorem, a distributed system can prioritize at most two out of the three: Consistency, Availability, and Partition Tolerance. The actual choice depends on the specific requirements and goals of the system.

### Examples:

- In scenarios where consistency is critical (e.g., financial systems), one might sacrifice availability during network partitions.

- In systems prioritizing high availability (e.g., web applications), consistency might be relaxed in favor of responding to user requests.

Understanding the CAP theorem helps architects and developers make informed decisions when designing and implementing distributed systems.


### Referance

https://www.youtube.com/watch?v=rb2R5I9S5d8

https://www.youtube.com/watch?v=3qRBeZsUa18&list=PL6W8uoQQ2c63W58rpNFDwdrBnq5G3EfT7&index=3

https://www.youtube.com/watch?v=pSoKUfLTe8Y

https://www.youtube.com/watch?v=kwCFHLbIhak

