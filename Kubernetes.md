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

**Deployment**  -  A deployment directly relates to application or microservice.In deployments you need to mention how many replicas you need to create for your application. 

**StatefulSet** - You need to ensure that database replicas are created so that the load is accordingly balanced. But one of the issues with creating Database replicas is that the Data should be consistently maintained as multiple application POD would be reading or writing data to multiple database POD. To ensure state of 
DB remains consistent we need to create DataBase replicas with Statefulset. StatefulSet ensures that database replicas are consistent. StatefulSet just like deployment would take care of replicating the PODS and scaling them up or scaling them down but making sure that the database reads and writes are synchronized so that no database inconsistencies are offered.However deploying database applications using stateful sets in kubernetes cluster is bit tedious, That's why it's also a common practise to host database applications outside of kubernetes cluster and just have stateless application that replciate and scale with no problem inside of the kubernetes cluster and communicate with external database.

**Pod** - A pod is nothing but specific running version of a microservice.

**Service** - Pod communicate with each other with the help of service. Service is kind of an address to a POD.

**Replica Set** - Replica Set maps to different version of microservice.

**Ingress** - Ingress is an object that allows access to your Kubernetes services from outside the Kubernetes cluster

![image](https://user-images.githubusercontent.com/52998083/222094137-dc1f070c-7c61-438c-90d7-f61189df8942.png)


### Different ways to setup Kubernetes cluster

1. With the help of MiniKube on your Local Machine. But your machine should be powerful enough to run that.
2. With the help cloud -</br>
     AWS provides (EKS)Elastic Kubernetes Service. No free Tier.</br>
     Azure provides (AKS)Azure Kubernetes Service.No free Tier.</br>
     Google provide (GKE)Google Kubernetes Engine.Offers free tier.</br>
     
### Understanding ConfigMap and Secrets

**ConfigMap** </br>

ConfigMap contains external configuration of your application like DataBaseURL. We just need to connect configMap to our POD and the POD starts reading configMap.

**What is the use of ConfigMap when we could provide all the configuration within properties file**

Consider an example where your Application POD is running on Kubernetes cluster, And the Database URL with which your Application communicates is changed, Then  in the given scenario, you might need to stop the application, update the configurtion with updated DB URL, build and push the updated version to the the repo and deploy the updated image of Application to Kubernetes cluster. The given problem is easily solved by Kubernetes ConfigMap as we can maintain all such external configuration within configMap, We could just update the configMap and the POD starts reading the updated configuration from configMap.


**Secret**

Secret is just like configMap but the difference is it is used to store secret data like credentials. It stores data in base64 encoded format. We just need to connect secret to our POD so that POD start reading data from secret.

![image](https://user-images.githubusercontent.com/52998083/222098488-20a6f73c-9ddc-4bd2-bac3-683ddb508329.png)


### Understanding Volumes

Whenever our application is running, we want our data to be Persistent. Consider an example where our Database POD is restarted, We would not want the Database to loose data once it is restarted, To ensure that the POD does not loose data once it is restarted we need to attach it with Volumes(External Physical storage either on same machine or remote machine).

![image](https://user-images.githubusercontent.com/52998083/222099429-bb84ca5a-c43e-4e5f-940a-18434996db5d.png)


### Processes within Worker Node

There are three processes which must be installed on every Node -</br>

1.**Container Runtime** So the first process which need to be run on every Node is the Container Runtime(Docker). Because Application Pods has container running inside them, A container runtime needs to be installed on every node.

2.**Kubelet** The Process that schedules the Pods and the containers underneath is Kubelet. Kubelet interacts with both the container and the node because at the end of the day Kubelet is responsible for running the POD and then assigning resources from the node to the Container like CPU,RAM and storage resources.

3.**Kube Proxy** The third process which is required is KubeProxy. KubeProxy must be installed on every node.KubeProxy has intelligent forwarding logic inside that makes sure that the communication also works in a performant way with low overhead. For example an application myapp replica is making a request to database instead of randonly forwarding request to any replica it will actually forward the request to replica that is runningon the same node as the POD that initiated the request.Thus this way 
it avoids the network overhead to send request to another machine.


![image](https://user-images.githubusercontent.com/52998083/222113199-ac19bb8e-1d83-40ce-b029-671b5a77cff0.png)


### Processes within Master Node

There are four processes running on Master Node that control the Worker Nodes.

**Api Server**  When we as a user wants to deploy new application in a kubernetes cluster, we need to interact with API server using some client it could be UI Or Kubernetes Dashboard or Kubernetes API or Command line tool. So API server is like a cluster gateway which gets the initial request of any updates into the cluster or even the queries from the cluster. It also acts as a gatekeeper for authentication to make sure that only authenticated and authorized request get through the cluster.

**Scheduler**  Once the API server validates your request it would schedule/start the application POD on one of the worker nodes using scheduler process. Scheduler just decides on which Node new Pod should be scheduled, The process which actually starts the container is Kubelet present within node processes.Kublet gets request from scheduler and executes that request on that node.

**Controller Manager**  Controller Manager detects state changes like crashing of PODS for example when Pods die Controller Manager detects that and tries to recover cluster state as soon as possible. For recovering the cluster state, Control manager request Scheduler to reschedule the dead parts.

**etcd**  etcd is a key value store of a cluster state. You could think of it as a cluster brain which means that when a Pod is scheduled, when a POD dies all of these changes gets saved or updated into this key-value store of etcd. ETCD is known as cluster brain because Scheduler, Controller Manager all works based on etcd key value store data.

![image](https://user-images.githubusercontent.com/52998083/222132608-813b95c1-22c7-4e10-a416-8aedbf387582.png)


### How to setup Cluster

![image](https://user-images.githubusercontent.com/52998083/222133406-b0fa77e9-9c5e-46f9-8fe8-fbdbbb8d57ac.png)


### Setting up Minikube on Local Machine for Testing purpose

**MiniKube** MiniKube is a 1 node Kubernetes cluster having both Master and Worker on the same node. Minikube has a preinstalled docker container runtime and it creates a virtual box on your laptop. Node runs in the virtual box. 

Follow - https://minikube.sigs.k8s.io/docs/start/  to setup MiniKube.

Once MiniKube is installed, Hit below commands in cmd.

1.**minikube start** to start minikube </br>
2.**minikube status** to check the status of Minikube</br>

![image](https://user-images.githubusercontent.com/52998083/222897299-0d69b094-a80e-423e-9113-be8a77436ff5.png)

3.**kubectl get nodes** to get the nodes of cluster

![image](https://user-images.githubusercontent.com/52998083/222897338-8dfc8914-b442-42e0-932b-cfd8d7d2fc33.png)

**Note** </br>
If you are working on a machine where kubernetes Minikube Cluster was already created the ensure to delete cluster by using command **minikube delete --all**


### Understanding Kubectl

Kubectl is a kubernetes command line tool to interact with Kubernetes Cluster. Kubectl interacts with APIServer on Master Node to create pods, destroy pods, create ConfigMap and Secrets.

![image](https://user-images.githubusercontent.com/52998083/222139519-0ad40824-d3ff-4ead-b2f8-456d608013f4.png)\


### Kubectl Commands

1.**kubectl get nodes** is used to get list of nodes </br>

2.**kubectl create deployment {deploymentName} --image={imageName}**  is used to run deployment(microservice) and create a POD. In the below example we are running nginx deployment(microservice) which we have named as nginx-depl and creating a POD of nginx. 

**Example** </br>
kubectl create deployment nginx-depl --image=nginx

![image](https://user-images.githubusercontent.com/52998083/222900698-5626afff-5ad7-4743-8c80-80114ef7d0a4.png)

3.**kubectl get deployment** is used to get all the deployments.</br>

![image](https://user-images.githubusercontent.com/52998083/222900762-1331bb22-e399-418c-9681-7ed1a65bc7f3.png)

4.**kubectl get pod** - PODS are created once deployment is running.</br>

5.**kubectl get replicaset** - To get replicaSet. ReplicaSet is created once deployment is running.</br>

![image](https://user-images.githubusercontent.com/52998083/222943482-4111551a-e8e2-42c7-ad10-c974f8571736.png)


6.**kubectl edit deployment {deploymentName}** is used to edit deployment(microservice)</br>

**Example** - kubectl edit deployment nginx-depl

7.**kubectl logs {podName}** is used to get the logs of POD and debug it.</br>

8.**kubectl describe pod {podName}** is used to get complete details of Pod.</br>

9.**kubectl exec -it {podName} -- bin/bash** is used to enter inside POD container.</br>

![image](https://user-images.githubusercontent.com/52998083/222944784-2083283a-9804-4b07-8b0e-59a2a22f57e5.png)

10. **kubectl delete deployment {deploymentName}** is used to delete deployment. Deleting deployment also deletes associated PODs and replicaSets.</br>

11.**kubectl apply -f {config.yaml}** is used to run deployment file and create deployment.

![image](https://user-images.githubusercontent.com/52998083/222945785-edb159ac-691b-49f6-bda5-337172b0add9.png)

![image](https://user-images.githubusercontent.com/52998083/222945800-ec61af9d-de78-49e3-ab01-da9c5f1eb516.png)


























     
     



