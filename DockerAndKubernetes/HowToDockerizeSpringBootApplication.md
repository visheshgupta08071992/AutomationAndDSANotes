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

This Dockerfile is used to create a Docker image that runs a Java application. Here's a breakdown of each line:

1. **Base Image:**
   ```dockerfile
   FROM openjdk:8
   ```
   - This line specifies the base image for your Docker image. The `openjdk:8` image is an official Docker image that contains a Java 8 runtime environment, allowing your Java application to run.

2. **Expose Port:**
   ```dockerfile
   EXPOSE 8080
   ```
   - This line makes port 8080 available for use by processes outside the container. In other words, it tells Docker that your application inside the container will be listening on port 8080, which is commonly used for web applications.

3. **Add JAR File:**
   ```dockerfile
   ADD target/SDETSpring-0.0.1-SNAPSHOT.jar SDETSpring-0.0.1-SNAPSHOT.jar
   ```
   - This line copies the `SDETSpring-0.0.1-SNAPSHOT.jar` file from the `target` directory on your host machine into the container. The JAR file is the packaged Java application that the container will run.

4. **Set Entry Point:**
   ```dockerfile
   ENTRYPOINT ["java","-jar","SDETSpring-0.0.1-SNAPSHOT.jar"]
   ```
   - This line sets the command that will be executed when the container starts. In this case, it runs the Java application by executing the `java -jar SDETSpring-0.0.1-SNAPSHOT.jar` command.



3.Once the docker file is created we need to build it to create an image using below syntax

When you build and run this Dockerfile, it creates a container that starts your Spring application and makes it accessible on port 8080.

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


###  Dockerize the Spring Boot Application with MySql 

1. **Create a Dockerfile for the Spring Boot application:**

   Here's an example Dockerfile:

   ```dockerfile
   # Start with a base image containing Java runtime
   FROM openjdk:17-jdk-slim

   # Set the working directory in the container
   WORKDIR /app

   # Copy the Spring Boot jar file into the container
   COPY target/myapp-0.0.1-SNAPSHOT.jar app.jar

   # Expose the port that the application will run on
   EXPOSE 8080

   # Run the jar file
   ENTRYPOINT ["java", "-jar", "app.jar"]
   ```

   - **Base Image**: Uses an official OpenJDK image.
   - **WORKDIR**: Sets the working directory inside the container.
   - **COPY**: Copies the Spring Boot JAR file from the target directory of your build to the container.
   - **EXPOSE**: Exposes port 8080, where the Spring Boot application will listen.
   - **ENTRYPOINT**: Defines the command to run the application when the container starts.

2. **Build the Docker image:**

   Run the following command from the directory containing your Dockerfile:

   ```bash
   docker build -t myapp .
   ```

### Step 2: Create a Docker Compose File

A `docker-compose.yml` file is used to define and manage multi-container Docker applications. For a Spring Boot application with MySQL, the file might look like this:

```yaml
version: '3.8'

services:
  # Spring Boot application
  app:
    image: myapp
    container_name: springboot_app
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "8080:8080"
    environment:
      - SPRING_DATASOURCE_URL=jdbc:mysql://db:3306/mydb
      - SPRING_DATASOURCE_USERNAME=root
      - SPRING_DATASOURCE_PASSWORD=rootpassword
    depends_on:
      - db

  # MySQL database
  db:
    image: mysql:8.0
    container_name: mysql_db
    environment:
      - MYSQL_DATABASE=mydb
      - MYSQL_ROOT_PASSWORD=rootpassword
    ports:
      - "3306:3306"
    volumes:
      - db_data:/var/lib/mysql

# Volumes
volumes:
  db_data:
```

### Explanation of the `docker-compose.yml` File:

- **version:** Specifies the version of Docker Compose syntax.

- **services:** Defines the services (containers) that make up your application.

  1. **app (Spring Boot Application):**
     - **image:** Specifies the Docker image to use. In this case, `myapp` refers to the image we built earlier.
     - **container_name:** The name of the container.
     - **build:** Specifies the context and Dockerfile to build the image if it doesn't exist.
     - **ports:** Maps the container's port 8080 to the host's port 8080, making the application accessible via `localhost:8080`.
     - **environment:** Sets environment variables for the Spring Boot application. This is where you configure the database connection.
     - **depends_on:** Ensures the MySQL container (`db`) starts before the Spring Boot application.

  2. **db (MySQL Database):**
     - **image:** Specifies the MySQL Docker image.
     - **container_name:** The name of the MySQL container.
     - **environment:** Sets environment variables for the MySQL container, such as the database name and root password.
     - **ports:** Maps the container's port 3306 to the host's port 3306, allowing access to the MySQL database.
     - **volumes:** Mounts a Docker volume to persist the database data, so it's not lost when the container stops.

- **volumes:** Defines named volumes to persist data. In this case, `db_data` stores MySQL data.

### Step 3: Running the Application

1. **Run Docker Compose:**

   In the directory containing your `docker-compose.yml` file, run:

   ```bash
   docker-compose up --build
   ```

   This command builds the Docker images (if needed) and starts the containers.

2. **Access the Application:**

   - **Spring Boot Application:** Access the Spring Boot application at `http://localhost:8080`.
   - **MySQL Database:** The database is accessible on `localhost:3306` using the credentials defined in the `docker-compose.yml` file.

This setup creates a fully Dockerized environment for your Spring Boot application with a MySQL database, enabling easy deployment and testing.

---

### To build and push docker image whenever new build is created we need to use Maven Plugin

`dockerfile-maven-plugin` is used to build and push docker image whenever new build is created

The `dockerfile-maven-plugin` does **not** automatically generate a `Dockerfile`. You must provide your own `Dockerfile` when using this plugin because it relies on your specific instructions for building the Docker image.


### **Workflow**
1. **You Create a `Dockerfile`:**
   You provide the `Dockerfile` with the specific instructions for building the image, such as the base image, copying files, installing dependencies, and defining the entry point.

   Example:
   ```dockerfile
   FROM openjdk:11-jre-slim
   ARG JAR_FILE
   COPY target/${JAR_FILE} app.jar
   ENTRYPOINT ["java", "-jar", "/app.jar"]
   ```

2. **`dockerfile-maven-plugin` Executes the Build:**
   The plugin executes the `docker build` command using the `Dockerfile` and any optional build arguments or configurations you specify in your Maven `pom.xml`.

```xml
   <build>
    <plugins>
        <plugin>
            <groupId>com.spotify</groupId>
            <artifactId>dockerfile-maven-plugin</artifactId>
            <version>1.4.13</version>
            <executions>
                <execution>
                    <id>build-image</id>
                    <phase>package</phase>
                    <goals>
                        <goal>build</goal>
                    </goals>
                </execution>
            </executions>
            <configuration>
                <repository>your-docker-repository/your-image-name</repository>
                <tag>${project.version}</tag>
                <buildArgs>
                    <JAR_FILE>${project.build.finalName}.jar</JAR_FILE>
                </buildArgs>
            </configuration>
        </plugin>
    </plugins>
</build>

```



**Referance Project**

https://github.com/visheshgupta08071992/SDETSpring

**To Dockerize SpringBoot Application with MySql refer below video**

https://www.youtube.com/watch?v=6hMHziv0T2Y&list=PLA7e3zmT6XQUTHCBMgkM9qoOrLdaOO5Gi&index=7

**To build and push docker image whenever new build is created we need to use Maven Plugin, Refer below video, Plugin used dockerfile-maven-plugin**

https://www.youtube.com/watch?v=2v0-aIO_R08&list=PLVz2XdJiJQxzMiFDnwxUDxmuZQU3igcBb&index=4&t=414s











