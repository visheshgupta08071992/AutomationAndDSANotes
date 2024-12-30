## API Gateway

An API Gateway is the single point of entry to the clients of an application. It sits between the clients and a collection of backend services for the application.
We can use open source API Gateway Implementation known as zuul provided by Netflix in our system.

### Uses of API gateway

**1.Routing Feature**</br>
The API Gateway directs incoming requests to the appropriate backend service which is requested  by client.

**2.Authentication,Authorization and SSL Certficate**

SSL Certificate, Authetification and Authorization Logic can be added as part of API Gateway Class separating it from the Application business logic.

**3.Adapter**</br>
There could be multiple calls from client, API Gateway can act as adapter by converting this multiple calls to a single call and then passing the calls to respective microservice, It again converts the response from Multiple mircroservices to a single response and sends it to client. For example consider an Amazon Cart page, The cart page has n number of details like Order Details, Customer Details, Product suggestion details which could be bought with the Product in cart. These all details would require call to multiple microservices, API Gateway converts this multiple call into single call and pass the request to appropriate microservice, It again converts the response from Multiple mircroservices to a single response and sends it to Amazon Cart Page i.e Aggregating responses from multiple services and sends them as a single response to the client.


**4.Caching**</br>
Caching can also be added within API gateway Class.

**5.Protocol Adapter**</br>
It changes the protocol of the request and response if both protocol are different. Consider client is sending HTTP2 protocol request and our application accepts HTTP1 
protocol request then Protocol Adaptor would help to resolve the issue.

**6.Logging and Monitoring**

**7.Load Balancer**</br>
Load Balancer can also be added within API Gateway ensuring load is correctly balanced between PODs of different services.

**8.Circuit Breaker**</br>

Circuit Breaking Capabilities at API Gateway helps us in eliminating unnecessary calls when services is down due to some problems. This helps in reducing unnecessary resources consumption by fallback mechanisms.

Take a scenario of hotel booking website, to get latest information of all hotels (+availability) , their corresponding rooms and other meta info, we need to exchange/access data(information) from hotel system. For exchanging information we need to make external service calls(HTTP Calls) between applications(or systems). We can consider external services calls as third party calls as it is outside our system or internal calls if we are hitting some internal service.

If status of destination service is healthy and also its availability is 99.99% then we can assume that all the calls made by us will be succeeded every time. This can be seen as Happy/Best Case.

Due to some unexpected scenario, status of application becomes unhealthy(down) but still our system have no idea about its health. So we keep hitting their services and in response we are getting error response i.e may be 5xx with some timeout or something else. As we are bombarding the external system, what actually we are doing wrong on our side is unnecessary exhausting our system resources. So there should be some mechanism to handle this failure. Here Circuit Breaker comes as Saviour.

Circuit Breaker can be considered as request interceptor means all the external request will go through it only. In Circuit Breaker configuration we need to define some threshold for maximum number of calls we can make in case of failure.

Now when this threshold is reached then circuit will be open i.e no more calls will be done to server for configured time. When this circuit is open for each request we made, we get some fallback(default) response. Now when the configured time is completed Circuit Breaker will partially close the circuit means it enables few request with external system.

When with this partially closed circuit if calls start succeeding then Circuit Breaker will close the circuit and will start serving requests at full intensity. If with partially request failed then it will again open the circuit and start serving fallback response.

Note: Circuit Breaker will not open the circuit for each failure call as that may be due to some intermittent issue. For example we can define configuration like it should open if 9 out 10 fails.

To conclude above discussion we can Circuit Breaker have three states:

Circuit Closed ( Everything is working fine)
Circuit Open (Destination service is failing and we are sending fall back response)
Half/Partially Open (Making few calls to check whether service is up or not)
One of most famous Circuit Breaker used by most of bug organisations is Hystrix (available for almost all the languages).



### API Gateway Workflow

![image](https://user-images.githubusercontent.com/52998083/220303233-918604d0-a923-44dd-92be-62d7fa55c7f9.png)

![image](https://user-images.githubusercontent.com/52998083/220307377-84c7dbcb-bf5f-4900-9fa8-669c73202e3e.png)


### Worth a read

https://hub.packtpub.com/api-gateway-and-its-need/

https://medium.com/@rishabh171192/system-design-api-gateway-backend-for-frontend-bff-cache-stampede-circuit-breaker-9c77101e8d54

https://www.itprotoday.com/cloud-computing-and-edge-computing/understanding-api-gateways-benefits-and-disadvantages



