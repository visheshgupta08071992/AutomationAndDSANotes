# Connection Pooling

Connection Pooling is a technique for reusing existing database connections by maintaining a pool of database connections instead of opening and closing a new connection each time a database request is made.

## How Connection Pooling Helps

### Prior to Connection Pooling

Consider a scenario where a user requests some information from an application. The application server would internally call the database server, which requires opening a new connection to the database, executing the query, and then closing the connection.

If there are numerous requests, and each application request needs to interact with the database, the application server would open, execute, and close a connection each time. This repeated opening and closing of connections is an expensive process that can significantly impact the query response time and, ultimately, the response time of the API endpoint.

### With Connection Pooling

1. When the application server starts, a certain number of connections are established to the database. This minimum number of connections is configurable.
2. When the application server needs to interact with the database, it borrows a connection from the connection pool instead of opening a new one. Once the application is done with its database operation, it returns the connection back to the pool.
3. If an application requires a connection but all connections in the pool are in use, the pool can either create a new connection up to the configured maximum number or make the application wait until a connection is released back to the pool.

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

