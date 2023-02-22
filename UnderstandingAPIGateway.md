## API Gateway

An API Gateway is the single point of entry to the clients of an application. It sits between the clients and a collection of backend services for the application.
We can use open source API Gateway Implementation known as zuul provided by Netflix in our system.

### Uses of API gateway

**1.Authentication,Authorization and SSL Certficate**

SSL Certificate, Authetification and Authorization Logic can be added as part of API Gateway Class separating it from the Application business logic.

**2.Adapter**</br>
There could be multiple calls from client, API Gateway can act as adapter by converting this multiple calls to a single call and then passing the calls to respective microservice, It again converts the response from Multiple mircroservices to a single response and sends it to client. For example consider an Amazon Cart page, The cart page has n number of details like Order Details, Customer Details, Product suggestion details which could be bought with the Product in cart. These all details would require call to multiple microservices, API Gateway converts this multiple call into single call and pass the request to appropriate microservice, It again converts the response from Multiple mircroservices to a single response and sends it to Amazon Cart Page.

**3.Routing Feature**</br>
If there are multiple Mirco services then using the routing system we could directly provide access to the requested api which is requested  by client.

**4.Caching**</br>
Caching can also be added within API gateway Class.

**5.Protocol Adapter**</br>
It changes the protocol of the request and response if both protocol are different. Consider client is sending HTTP2 protocol request and our application accepts HTTP1 
protocol request then Protocol Adaptor would help to resolve the issue.

**6.Logging and Monitoring**

**7.Load Balancer**</br>
Load Balancer can also be added within API Gateway ensuring load is correctly balanced between PODs of different services.



### API Gateway Workflow

![image](https://user-images.githubusercontent.com/52998083/220303233-918604d0-a923-44dd-92be-62d7fa55c7f9.png)

![image](https://user-images.githubusercontent.com/52998083/220307377-84c7dbcb-bf5f-4900-9fa8-669c73202e3e.png)


### Worth a read

https://hub.packtpub.com/api-gateway-and-its-need/

https://www.itprotoday.com/cloud-computing-and-edge-computing/understanding-api-gateways-benefits-and-disadvantages



