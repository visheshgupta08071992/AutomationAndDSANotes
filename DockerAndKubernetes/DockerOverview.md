# Docker Overview

Docker is a tool to streamline the development, deployment, and management of applications using containerization technology.

---

## Use Cases of Docker in Test Automation

### 1. Setting Up Test Automation Framework

One common challenge in test automation is when a client requests to set up the automation framework at their end and execute the test automation scripts. This often involves:

- Compatibility issues, such as differences in Selenium versions, browser versions, TestNG versions, or operating system versions.
- A tedious setup process at the client’s side.

**Solution:**

Docker simplifies this process by enabling the creation of an image of the automation framework, which includes all dependencies. This image can be pushed to Docker Hub, allowing the client to pull and run the image to execute automation tests seamlessly.

**Sample Dockerfile for an Automation Framework:**

```dockerfile
FROM maven:3.6.3-jdk-8
COPY src /home/apiframework/src
COPY index.html /home/apiframework/index.html
COPY pom.xml /home/apiframework/pom.xml
COPY testng.xml /home/apiframework/testng.xml
WORKDIR /home/apiframework
ENTRYPOINT mvn clean test
```

---

### 2. Simplifying Selenium Grid Setup with Docker-Compose

Docker also simplifies setting up a Selenium Grid using a `docker-compose.yml` file. This file defines and manages multi-container Docker applications, allowing you to run and network multiple containers easily.

**Sample `docker-compose.yml` for Selenium Grid:**

```yaml
version: "3.9"
services:
  selenium-hub:
    image: selenium/hub:4.12.0  # Adjust the version as needed
    container_name: selenium-hub
    ports:
      - "4444:4444"  # Exposes the Selenium Grid Hub

  chrome-node:
    image: selenium/node-chrome:4.12.0
    container_name: chrome-node
    depends_on:
      - selenium-hub
    environment:
      - HUB_HOST=selenium-hub

  firefox-node:
    image: selenium/node-firefox:4.12.0
    container_name: firefox-node
    depends_on:
      - selenium-hub
    environment:
      - HUB_HOST=selenium-hub
```

**Commands:**

- To run the Docker Compose file:
  ```bash
  docker-compose up -d
  ```

- To scale Firefox and Chrome nodes:
  ```bash
  docker-compose up --scale chrome-node=3 --scale firefox-node=3
  ```

---

## Docker Workflow

The typical workflow involves several steps:

1. **Dockerfile** → Build (`docker build -t imageName .`) → **Image**
2. **Push** (`docker login` followed by `docker push imageName`) → **DockerHub**
3. **Pull** (`docker pull imageName`) → **Image**
4. **Run** (`docker run imageName`) → **Container**

---

## Important Docker Commands

| Command                                       | Description                                                                                     |
|-----------------------------------------------|-------------------------------------------------------------------------------------------------|
| `docker login`                                | Logs into Docker Hub.                                                                           |
| `docker images`                               | Displays all images on the local machine.                                                      |
| `docker pull <imageName>`                     | Pulls an image from Docker Hub.                                                                |
| `docker run <imageName>`                      | Runs an image to create a container. A container is a running image.                           |
| `docker ps`                                   | Displays all running containers.                                                               |
| `docker ps -a`                                | Displays all running and stopped containers.                                                   |
| `docker stop <containerID>`                   | Stops a running container.                                                                     |
| `docker logs <containerID>`                   | Displays logs of a container.                                                                  |
| `docker logs <containerID> -f`                | Streams logs of a container.                                                                   |
| `docker exec -it <containerID> /bin/bash`     | Opens a terminal in a running container. Use `exit` to leave the container.                    |
| `docker run -d -it <imageName>`               | Runs an image in the background with attached input/output.                                     |
| `docker run --name <name> -d -it <imageName>` | Runs an image with a specific container name.                                                  |
| `docker run -P <hostPort>:<containerPort>`    | Maps a host port to a container port.                                                          |
| `docker run -v <hostDir>:<containerDir>`      | Maps a volume between the host machine and the container.                                       |
| `docker build -t <imageName>`               | Builds an image from a Dockerfile. The `.` indicates that the Dockerfile is in the current directory. |
| `docker commit <container-id> my-image-name:latest`               | Used to create an image from containerID, Replace <container-id> with the actual container ID and my-image-name:latest with your desired image name and tag. |

---

## Understanding How to Dockerize SpringBoot Application an dockerfile-maven-plugin

https://github.com/visheshgupta08071992/AutomationAndDSANotes/blob/master/DockerAndKubernetes/HowToDockerizeSpringBootApplication.md
