# How would one validate the correct Json Schema

With microservice or API testing, it is very important to ensure schema is always validated and is correct. Lets analyze some of the ways of Validating schemas:

**1. Validating Schema's using Json Schema Validator**

To Validate Json Schema using Json Schema Validator, We need to add Json Schema Validator dependency in our project(https://mvnrepository.com/artifact/io.rest-assured/json-schema-validator)

Once Json Schema Validator dependency is added within our project, we must get the schema of our json which need to be validated. We can get the schema of our json by 
pasting the json here https://www.liquid-technologies.com/online-json-to-schema-converter. Finally we can have this schema stored in our resources folder.
