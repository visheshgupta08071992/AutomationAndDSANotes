## Understanding Kubernetes

Kubernetes is a container orchestration tool. It helps to manage containerized applications in different deployment environments.

**Container** + **Orchestration**

Container is nothing but running version of a docker image. When we talk about microservice architecture, we are talking about maybe 10-15 microservices and maybe multiple containers for each of these microservices, so in general we are talking about hundreds or thousands of containers, so what we need to identify is which container is working well,which container needs to be replaced, how many requests are coming in, Should we increase the number of container or should we decrease the no of containers, Kubernetes helps to solve all the mentioned orchestration problem. In general it helps to orchestrate containers belonging to multiple microservices.
Container Orchestration or kubernetes helps to manage 100's of containers belonging to multiple microservices.

Kubernetes simplifies the use and deployment of microservices, because whenever we look at microservices, these microservices can be built in different languages be it Java,Python or Nodejs. The way one deploy Java microservice can be entirely different from the way we deploy Python microservice, Also to solve a Production problem the way we get logs from a python application might be different from a Java Application. So once you have the Container Orchestrater and you are making use of containers all these things are standardized. So once you have the container image, it does not matter what is inside the container, The way you deploy it is the same,the way you get metrics or even logs out of it is the same. With Kubernetes you don't requires any external service discovery, Kuberneters has its own service discovery which helps microservices to discover each other.

### How do we deploy Java Application in Kubernetes

1. The first foremost step to deploy Java Application in Kubernetes is to create an image of Java application and push it to a container repository

![image](https://user-images.githubusercontent.com/52998083/221773863-9cb3b258-c418-4f8c-b569-9866ffce3fb7.png)

2. Once you have the container image, The first step when you need to deploy something on Kubernetes is to create Kubernetes Cluster. Cluster is nothing but set of Hardware or Virtual Machines where you need to deploy this application. In Kubernetes Terminology this are called nodes.

![image](https://user-images.githubusercontent.com/52998083/221774794-e2159cf1-4581-48e9-a8b2-a472034254eb.png)

3.Run the image on the kubernetes cluster.


The cluster creation is done only once and Once the Cluster is created






### What features do Orchestration Tool Offer

![image](https://user-images.githubusercontent.com/52998083/221558712-bb2acda3-9558-4e42-a8b3-4edf22f7c53e.png)

