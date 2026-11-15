# API Automation Framework – Overview

In our API Automation Framework, we are using **Maven** as our build tool and for managing project dependencies.

Some of the key external dependencies used in our project are:

- **Rest Assured:** For API automation and validating REST API requests and responses.
- **Jackson:** For serialization and deserialization of JSON request and response bodies.
- **TestNG:** For writing and executing test cases, managing test execution and performing assertions.
- **Java Faker:** For generating dynamic test data.
- **JSON Schema Validator:** For validating API response structures against predefined JSON schemas.

We use **TestNG** for writing assertions and managing test execution through `testng.xml` files, where we define different test suites and configure their execution.

For version control, we use **Git**, and GitHub is our remote repository for maintaining and collaborating on the framework's source code.

# Project Structure

Now, let's explore the project structure and understand the responsibilities of different folders.

### 1. src/main/java

This folder contains the reusable components of our framework.

- **Payload Package:** Contains Payload classes with different static and parameterized methods that return request bodies. These methods help us generate different request payloads dynamically based on the input parameters.
- **POJO Request Package:** Contains Java POJO classes representing different API request bodies. These classes are used for serialization of Java objects into JSON.
- **POJO Response Package:** Contains Java POJO classes representing different API response bodies. These classes are used for deserializing JSON responses into Java objects.

### 2. src/test/java

This folder contains our test implementation and supporting classes.

- **Test Package:** Contains all our API test classes, where we write different test scenarios for various API endpoints.
- **BaseTest Class:** Contains common configurations and reusable components required by our test classes. It is primarily used to define generic Request Specification and Response Specification builders using Rest Assured, helping us avoid duplicating common configurations across test classes.

### 3. src/test/resources

This folder contains external resources required for test execution.

- **TestNG XML Files:** Contains different TestNG suite files used to organize and control test execution.
- **JSON Schema Files:** Contains predefined JSON schemas for different API responses, which are used for schema validation.
- **Properties Files:** Used to maintain framework configurations such as base URI, database URL and other environment-specific properties.

### 4. Utility Package

We also have a Utility package under `src/test/java`, which contains reusable utility classes and helper methods required by the framework.

For example:
- **Listeners:** We use TestNG listeners to capture test execution events and integrate with Extent Reports for generating execution reports.
- **Utility Methods:** Contains common reusable methods that help us avoid code duplication and simplify test implementation.

----------------------------------------------------------------------------------------------------------------------------------------------------------

In out API automation framework we are using Maven as Build tool and for managing our dependencies.
Some of the external dependencies which we are using in our project are Obviously RestAssured,Jackson Dependency for Serialization and Deserialization,TestNg,Faker Liber for generating Test Data,Json Schema Validator for validating Json schema.

 We are using TestNg for writing assertions and managing execution of our Tests through TestNg.xml file.The version control tool is git and the remote repository is on GitHub.


Now exploring our project structure


src/main/java contains Payload folder which contain Payload class having different static paramterized methods returning different request bodies

We hava Pojo request folder which contain Pojo classes for request bodies

We have POJO response folder which contains pojo classes for response bodies


src/test/java contains test folder which has all our test classes and even basetest class which is used to define generix request and response spec builder

Then there is a src/test folder also contains resource folder which contains different TestNg.xml suite, Json Schema files for different response schemas,properties file for maintaining configurations like baseURI,db url


src/test folder also contains utility folder containing utility classes like listners for extent report,utility methods
