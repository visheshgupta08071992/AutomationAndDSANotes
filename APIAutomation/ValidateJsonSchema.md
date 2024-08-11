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

To validate test for additional properties, we must have **additionalProperties** Tag set to false within the json schema

we can get schema of our json with additionalProperties set as false with below steps -</br>

1.Paste json here https://www.liquid-technologies.com/online-json-to-schema-converter. </br>
2.Click on Options button and uncheck defaultAdditionalProperties checkbox </br>
3.Click on generate Schema </br>
4.Ensure to remove attribute "$schema" attribute which is added in schema after converting json into schema </br>


**Referance** - https://www.youtube.com/watch?v=PCtqZTO9Hac&list=PL9ok7C7Yn9A-JaUtcMwevO_FfbFNRYLfU&index=15


## NOTE

1.When using `JsonSchemaValidator` in RestAssured, if there are multiple mismatches in the JSON response compared to the schema, the `SchemaValidationException` typically reports all of them. The exception message will list all the fields that do not match the schema, rather than stopping at the first mismatch.

This means that if multiple fields have type mismatches, are missing, or have other issues, the exception will include details about each of these problems in a single exception message.

For example, if the JSON response has several fields that do not conform to the schema, the exception might look like this:

```
SchemaValidationException: json does not match the expected JSON schema.
Expected: A valid JSON schema for the response
Actual: A JSON document that does not match the schema

Validation errors:
- [field1]: expected type: String, found: Number
- [field2]: expected type: Boolean, found: String
- [field3]: missing but it is required
```

In summary, RestAssured's JsonSchemaValidator is designed to report all validation errors in a single exception, making it easier to identify and correct multiple issues in the JSON response.



2.When additional fields are present in a JSON response that are not defined in the schema, the error message thrown during validation will typically indicate that the response contains properties that are not allowed. This is controlled by the `additionalProperties` keyword in the JSON schema.

**Example Error Message**

If your schema has `additionalProperties: false`, and the response contains an extra field, the error message might look like this:

```
io.restassured.internal.validation.JsonSchemaValidationException: 
Schema validation failed for the response body.
Validation errors:
- Additional properties not allowed: extrafield
```

**Implementation in Schema**

To ensure that additional fields are not allowed, you need to include `additionalProperties: false` in your schema definition. Here’s an example of how to structure your schema:

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "name": { "type": "string" },
    "email": { "type": "string" }
  },
  "required": ["name", "email"],
  "additionalProperties": false
}
```

In summary, if there are additional fields in the JSON response that are not defined in the schema, the validation will fail, and the error message will clearly indicate which additional properties are not allowed. This feature is crucial for maintaining strict adherence to the expected data structure.





