# How would one validate the correct Json Schema

With microservice or API testing, it is very important to ensure schema is always validated and is correct. Lets analyze some of the ways of Validating schemas:

**1. Validating Schema's using Json Schema Validator**

To Validate Json Schema using Json Schema Validator, We need to add Json Schema Validator dependency in our project(https://mvnrepository.com/artifact/io.rest-assured/json-schema-validator)

Once Json Schema Validator dependency is added within our project, we must get the schema of our json which need to be validated. We can get the schema of our json by 
pasting the json here https://www.liquid-technologies.com/online-json-to-schema-converter. Ensure to remove attribute "$schema" attribute which is added in schema after converting json into schema. Finally we can have this schema stored in our resources folder.


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


**Code Validate the Json against the response body**

```js

respnose.then().body(JsonSchemaValidator.matchesJsonSchema(new File("./src/test/resources/Schema.json")));

```

Json Schema validater would not only validate all the attributes within the schema but would also validate their type, If the validation fails then the assertion error is thrown.

**2. Validating Json Schema does not have addtional properties**

It is important to Validate that response schema does not have additional attributes, This validation is important to ensure our API does not send additional
attributes apart from the ones mentioned in the contract, If Additional attributes are received then the TC should fail. This scenario could have been
covered within schema validation test but covering it within a separate test gives a clear picture with regards to Test Failure

To validate test for additional properties, we must have additionalProperties Tag set to false within the json schema

we can get schema of our json with additionalProperties set as false with below steps -

1.Paste json here https://www.liquid-technologies.com/online-json-to-schema-converter.
2.Click on Options button and uncheck defaultAdditionalProperties checkbox
3.Click on generate Schema
4.Ensure to remove attribute "$schema" attribute which is added in schema after converting json into schema


**Referance** - https://www.youtube.com/watch?v=PCtqZTO9Hac&list=PL9ok7C7Yn9A-JaUtcMwevO_FfbFNRYLfU&index=15





