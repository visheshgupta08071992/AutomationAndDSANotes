# Connection Pooling

Connection Pooling is a technique for reusing existing database connections by maintaining a pool of database connections instead of opening and closing a new connection each time a database request is made.

## How Connection Pooling Helps

### Prior to Connection Pooling

Suppose an user has requested some information to the Application, The Application server would internally call Database Server, To perform operation on Database, The Application need to open a new connection to database, execute the query and then close the connection.

Suppose if there are n no of requests and everytime each Application request needs to interact with Database then each time the Application server would Open the Connection, Execute the query and close the connection.

These Opening and closing of connections is an expensive process and drastically impact the query response time and in turn response time of the API endpoint.

### With Connection Pooling

1. As soon as the Application Server start, Certain number of connection are established to Database. These Minimum no of connections are configurable.
2. When an Application server needs to interact with Database then instead of Opening a new connection, It would borrow a connection from Connection Pool, Once the Application is done with its Database operation, It would return the connection back to Connection Pool.
3. If an Application requires a connection and all the connection from pool are in use then the pool may create a new connection upto configured maximumn no of connection or make the application wait until a connection is released back to pool. 

### Example Configuration

Suppose you have:

- **7 Application Pods**
- **3 Databases**
- **Min Pool Connections** = 10
- **Max Pool Connections** = 20

Each application pod will maintain a minimum of 10 connections to each database. Therefore, when the application starts, there will be:

```
7(Number of Pods)×3(Databases)×10(Min Idle Connections)=210 active connections
```


 It’s generally best practice to set an appropriate maximum connection count alongside a moderate minimum idle setting. Setting the minimum idle connection count too high can lead to wasted resources(CPU and Memory) on both the database and application servers, longer restart/failover times, connection leaks and potentially increased costs. Using a lower minimum idle count with an appropriate maximum connection cap allows the system to allocate resources more efficiently and only use what’s necessary
