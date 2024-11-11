### Connection Pooling

Connection Pooling is a technique of reusing DataBase Connections effliciently by maintaining a pool of reusable connections,rather
than opening and closing a new connection for every database request.

### How Connection Pooling Works
**Initialization:** A connection pool is initialized with a certain number of connections to the database. These connections are established and stored in the pool, ready for use.

**Borrow and Return:** When an application needs a database connection, it borrows one from the pool instead of creating a new one. Once it's done using the connection, it returns it to the pool for future reuse.

**Pool Management:** The pool monitors the number of active connections. If all connections are in use and a new one is needed, the pool may create a new connection (up to a specified maximum) or make the application wait until a connection is released back into the pool.
