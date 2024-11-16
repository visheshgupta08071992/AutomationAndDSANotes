### Understanding CAP Therom

# CAP Theorem in Distributed Computing

The **CAP theorem** is a concept in distributed computing that highlights the trade-offs between three desirable properties in a distributed system: **Consistency**, **Availability**, and **Partition Tolerance**. The CAP theorem states that in a distributed system, it's impossible to achieve all three properties simultaneously. 

Here's a brief explanation of each term:

- **Consistency (C):** All nodes in a distributed system have the same data at the same time. In other words, when a write operation is completed, all subsequent read operations will return the updated data.That is every rrad receives the most recent write.

- **Availability (A):** Every request to the system receives a response, without a guarantee that it contains the most recent version of the information. Availability, in this context, means that every node (or server) in the system is responsive. Every request (read or write) receives a response, even if it might not be the latest.

- **Partition Tolerance (P):** The system continues to operate even when network partitions occur, meaning communication between nodes is unreliable or delayed. Partition tolerance is crucial for systems that need to withstand network failures. To ensure partition tolerance, the system has to make trade-offs between consistency and availability. That during Partition Tolerance System can either be Consistent or Avaiable.

According to the theorem, a distributed system can prioritize at most two out of the three: Consistency, Availability, and Partition Tolerance. Partition tolerance is typically non-negotiable (distributed systems must handle network partitions). The trade-off is usually between consistency and availability, based on application needs.

### Examples:

- In scenarios where consistency is critical (e.g., financial systems), one might sacrifice availability during network partitions.

- In systems prioritizing high availability (e.g., web applications), consistency might be relaxed in favor of responding to user requests.

Understanding the CAP theorem helps architects and developers make informed decisions when designing and implementing distributed systems.


### Referance

https://www.youtube.com/watch?v=rb2R5I9S5d8

https://www.youtube.com/watch?v=3qRBeZsUa18&list=PL6W8uoQQ2c63W58rpNFDwdrBnq5G3EfT7&index=3

https://www.youtube.com/watch?v=pSoKUfLTe8Y

https://www.youtube.com/watch?v=kwCFHLbIhak

