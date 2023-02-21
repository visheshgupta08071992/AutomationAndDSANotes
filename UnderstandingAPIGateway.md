## API Gateway

An API Gateway is the single point of entry to the clients of an application. It sits between the clients and a collection of backend services for the application.
We can use open source API Gateway Implementation known as zuul provided by Netflix in our system.

### Uses of API gateway

**1.Authentication,Authorization and SSL Certficate**

SSL Certificate, Authetification and Authorization Logic can be added as part of API Gateway Class separating it from the Application business logic.

**2.Routing Feature**</br>
If there are multiple Mirco services then using the routing system we could directly provide access to the requested api which is requested  by client.

**3.Caching**</br>
Caching can also be added within API gateway Class.

**4.Protocol Adapter**</br>
It changes the protocol of the request and response if both protocol are different. Consider client is sending HTTP2 protocol request and our application accepts HTTP1 
protocol request then Protocol Adaptor would help to resolve the issue.

**5.Logging and Monitoring**

**6.Load Balancer**</br>
Load Balancer can also be added within API Gateway ensuring load is correctly balanced between PODs of different services.



### API Gateway Workflow

![image](https://user-images.githubusercontent.com/52998083/220303233-918604d0-a923-44dd-92be-62d7fa55c7f9.png)

![image](https://user-images.githubusercontent.com/52998083/220307377-84c7dbcb-bf5f-4900-9fa8-669c73202e3e.png)


