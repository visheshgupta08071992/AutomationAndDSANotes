# How would one validate the correct Json Schema

With microservice or API testing, it is very important to ensure schema is always validated and is correct. Lets analyze some of the ways of Validating schemas:

**1. Validating Schema's using Json Schema Validator**

To Validate Json Schema using Json Schema Validator, We need to add Json Schema Validator dependency in our project(https://mvnrepository.com/artifact/io.rest-assured/json-schema-validator)

Once Json Schema Validator dependency is added within our project, we must get the schema of our json which need to be validated. We can get the schema of our json by 
pasting the json here https://www.liquid-technologies.com/online-json-to-schema-converter. Finally we can have this schema stored in our resources folder.


**Json**

```js

{
    "id": 877251703,
    "firstName": "Jude",
    "lastName": "Hayes",
    "email": "cletus.gottlieb@gmail.com",
    "jobs": [
        "Tester,Trainer"
    ],
    "favFoods": {
        "breakfast": "idly",
        "lunch": "rice",
        "dinner": [
            "Chapati",
            "Milk"
        ]
    }
}

```


**Corresponding Json Schema**

```js

{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "id": {
      "type": "integer"
    },
    "firstName": {
      "type": "string"
    },
    "lastName": {
      "type": "string"
    },
    "email": {
      "type": "string"
    },
    "jobs": {
      "type": "array",
      "items": [
        {
          "type": "string"
        }
      ]
    },
    "favFoods": {
      "type": "object",
      "properties": {
        "breakfast": {
          "type": "string"
        },
        "lunch": {
          "type": "string"
        },
        "dinner": {
          "type": "array",
          "items": [
            {
              "type": "string"
            },
            {
              "type": "string"
            }
          ]
        }
      },
      "required": [
        "breakfast",
        "lunch",
        "dinner"
      ]
    }
  },
  "required": [
    "id",
    "firstName",
    "lastName",
    "email",
    "jobs",
    "favFoods"
  ]
}

```

**Json Schema Stored in resource folder**

![image](https://user-images.githubusercontent.com/52998083/189519447-3fbbcfc8-13ad-4ec1-91c0-ae48bbee3607.png)


**Code Validate the Json against the response body

```js

respnose.then().body(JsonSchemaValidator.matchesJsonSchema(new File("./src/test/resources/Schema.json")));

```





