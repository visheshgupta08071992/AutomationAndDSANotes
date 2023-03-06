## Microservice Interview Questions


### What is Monolithic Architecture and its drawbacks?

![image](https://user-images.githubusercontent.com/52998083/220589299-4b30cbe1-479c-4eb2-86ea-92b1ac4c4b12.png)

### What is Microservices?

![image](https://user-images.githubusercontent.com/52998083/220590222-55ee8045-9fc1-4f44-a7d2-82e2f5a9dc4b.png)

### What is an API Gateway?

![image](https://user-images.githubusercontent.com/52998083/220590679-88d6b7f6-b8a7-4f83-8fae-8a18511dd61e.png)

### How Microservices communicate with each other?

Microservices can communicate with help of API calls(Synchronous Communication) or through Messaging Queues(Asynchronous Communication) like Kafka.

![image](https://user-images.githubusercontent.com/52998083/220592488-79c716fc-7b6a-47d5-9027-cd6fcfecb705.png)

### What is service discovery in microservices?

![image](https://user-images.githubusercontent.com/52998083/220593422-78fcc0a6-9357-4ea7-a250-42defa531113.png)

### What is Circuit breaker and Fault Taulerance?

![image](https://user-images.githubusercontent.com/52998083/220595621-a0c96264-f897-4739-8f95-dce0dacf6f0d.png)

### What is Spring Cloud Config Server?

Every micorservice would have its configuration defined within its yaml file. Microservice 1 would have its own configuration yml file similarly microservice 2 would have its separate configuration defined within yml. If the given configuration is hardcoded and if we want to change the configuration then in the given case we have to take down our deployment, change the configuration and deploy the new version of our microservice. This is not the best practise, The given problem can be solved with Spring Cloud Config Server which can read configuration from somewhere for example Git, We can checkin our configuration in our Git configuration repo and our Spring Cloud Config Server will read our configuration from Git Configuration Project and whenever we change the git config project, Spring Cloud Config server can read the latest configuration and hand it over to our microservices.


![image](https://user-images.githubusercontent.com/52998083/220596580-da4b11d9-b0ba-4df8-8199-1b1c72a66e2b.png)

### What is the database strategy you follow for microservices?

![image](https://user-images.githubusercontent.com/52998083/220604806-6f1df84b-7df5-4c00-ba62-d65b97481972.png)

### How do you monitor your microservices?

![image](https://user-images.githubusercontent.com/52998083/220605104-74a9347d-00ce-4bff-b7c6-600f5dffb314.png)


## Referance

https://www.youtube.com/watch?v=SZBJNKnOGTw&list=PLHurxyYY5q3Ha_Hs_u0uCh-UAkkyt4QPb&index=6















