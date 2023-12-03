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




### Reference
  
https://www.youtube.com/watch?v=O_c7lzNbcKo  

https://www.youtube.com/watch?v=hl65apHxp64

https://www.youtube.com/watch?v=fG8c-huFt70
