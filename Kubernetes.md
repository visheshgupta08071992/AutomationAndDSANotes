## Understanding Kubernetes

Kubernetes is a container orchestration tool. It helps to manage containerized applications in different deployment environments.

**Container** + **Orchestration**

Container is nothing but running version of a docker image. When we talk about microservice architecture, we are talking about maybe 10-15 microservices and maybe multiple containers for each of these microservices, so in general we are talking about hundreds or thousands of containers, so what we need to identify is which container is working well,which container needs to be replaced, how many requests are coming in, Should we increase the number of container or should we decrease the no of containers, Kubernetes helps to solve all the mentioned orchestration problem. In general it helps to orchestrate containers belonging to multiple microservices.
Container Orchestration or kubernetes helps to manage 100's of containers belonging to multiple microservices.

Kubernetes simplifies the use and deployment of microservices, because whenever we look at microservices, these microservices can be built in different languages be it Java,Python or Nodejs. The way one deploy Java microservice can be entirely different from the way we deploy Python microservice, Also to solve a Production problem the way we get logs from a python application might be different from a Java Application. So once you have the Container Orchestrater and you are making use of containers all these things are standardized. So once you have the container image, it does not matter what is inside the container, The way you deploy it is the same,the way you get metrics or even logs out of it is the same. With Kubernetes you don't requires any external service discovery, Kuberneters has its own service discovery which helps microservices to discover each other. Another feature when we talk about kubernetes is centralized configuration with the help of config map,secrets.

### How do we deploy Java Application in Kubernetes

1. The first foremost step to deploy Java Application in Kubernetes is to create an image of Java application and push it to a container repository

![image](https://user-images.githubusercontent.com/52998083/221773863-9cb3b258-c418-4f8c-b569-9866ffce3fb7.png)

2. Once you have the container image, The first step when you need to deploy something on Kubernetes is to create Kubernetes Cluster. Cluster is nothing but set of Hardware or Virtual Machines where you need to deploy this application. In Kubernetes Terminology this are called nodes.

![image](https://user-images.githubusercontent.com/52998083/221774794-e2159cf1-4581-48e9-a8b2-a472034254eb.png)

3.Run the image on the kubernetes cluster.


The cluster creation is done only once and Once the Cluster is created we could run the images multiple times.

### Understanding Kubernetes Cluster.

Kubernetes Cluster have two types of Nodes namely Master Nodes and the Worker Nodes-

**Master Nodes**
Master Nodes are the ones that are managing the Worker Nodes. Lets say we want to have 10 instances of a microservice, To have 10 instances of Microservice we need to give kubectl command which goes to the Master Node. The Master node would then decide which worker node has space to meet the spefice requirement. It would then deploy those things to specific node.

**Worker Nodes**
Worker Nodes are the Nodes where your microservices are actually run.

### Terminolgies in Kubernetes

**Deployment**  -  A deployment directly relates to application or microservice.

**Pod** - A pod is nothing but specific running version of a microservice.

**Service** - Service is something which is used to expose the deployment to the outside world.

**Replica Set** - Replica Set maps to different version of microservice.

### Different ways to setup Kubernetes cluster

1. With the help of MiniKube on your Local Machine. But your machine should be powerful enough to run that.
2. With the help cloud -</br>
     AWS provides (EKS)Elastic Kubernetes Service. No free Tier.</br>
     Azure provides (AKS)Azure Kubernetes Service.No free Tier.</br>
     Google provide (GKE)Google Kubernetes Engine.Offers free tier.</br>
     
### Understanding ConfigMap and Secrets

**ConfigMap**



     
     



