## How to Dockerize SpringBoot Application

To Dockerize Spring Boot Application we need to follow below steps.

1.Create a jar of your spring boot application by using below command

```js
mvn -Dmaven.test.skip=true package
```

The above command would create a jar file in your Target folder as shown in below screenshot. The name of the given jar file should be mentioned in the DockerFile which
we would create in next step.

![image](https://user-images.githubusercontent.com/52998083/206895620-59fdf6a9-431f-41a2-bf2b-5c9896da7a93.png)

2.Create a file named DockerFile in your project directory

```js

# Start with a base image containing Java runtime
FROM openjdk:8

# Make port 8080 available to the world outside this container
EXPOSE 8080

ADD target/SDETSpring-0.0.1-SNAPSHOT.jar SDETSpring-0.0.1-SNAPSHOT.jar

# Run the jar file
ENTRYPOINT ["java","-jar","SDETSpring-0.0.1-SNAPSHOT.jar"]

```

![image](https://user-images.githubusercontent.com/52998083/206895676-cb28f4be-c6b3-4f8e-84e2-9e3d21ccb8c5.png)


3.Once the docker file is created we need to build it to create an image using below syntax

**syntax**

```js

docker build -t {owner}/{imagename} .

```

**.** -> In above command **.** represents that the DockerFile which is being built resides in current directory where the command is executed.

**example**

```js
docker build -t visheshdocker/sdetspringprojects .
```

4.Once the image is created we can check the image using commaned

```js
docker images
```

![image](https://user-images.githubusercontent.com/52998083/206896002-ac69070d-2874-45ac-8c9b-f118b1c84996.png)

5.We can push the created image to docker hub by following belwo commands-

**Docker Login**

```js
docker login
```

Provide your username and password after executing docker login command.

**Push the Image**

```js
docker push {imagename}
```

**example**

```js
docker push visheshdocker/sdetspringprojects
```

![image](https://user-images.githubusercontent.com/52998083/206896256-a199bda9-aba1-42f1-a90a-92a6a6507b23.png)


6.Finally we should pull and run the image

**Syntax**

```js
docker pull {imagename}
```

```js
docker run {imagename}
```

**Example**

**To Pull Docker Image**

```js
docker pull visheshdocker/sdetspringprojects
```

**To Run Docker Image**

```js
docker run -p 9090:8080 visheshdocker/sdetspringprojects
```

In the above command port 9090 is the local machine port mapped to container port 8080.

**Referance Project**

https://github.com/visheshgupta08071992/SDETSpring

**To Dockerize SpringBoot Application with MySql refer below video**

https://www.youtube.com/watch?v=6hMHziv0T2Y&list=PLA7e3zmT6XQUTHCBMgkM9qoOrLdaOO5Gi&index=7

**To build and push docker image whenever new build is created we need to use Maven Plugin, Refer below video**

https://www.youtube.com/watch?v=2v0-aIO_R08&list=PLVz2XdJiJQxzMiFDnwxUDxmuZQU3igcBb&index=4&t=414s











