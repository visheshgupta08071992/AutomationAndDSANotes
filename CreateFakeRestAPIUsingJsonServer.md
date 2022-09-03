## Create Fake Rest API Using Json Server

1. To create a Fake Rest API we need to install node.js.
2. Once Node.js is installed, run command **npm install -g json server** within command prompt. The given command would install json-sevrer npm module on your machine.
3. Now let’s create a new JSON file with name db.json. This file contains the data which should be exposed by the REST API. For objects contained in the JSON structure CRUD entpoints are created automatically. Take a look at the following sample db.json file:

```js

{
  "employees": [
    {
      "id": 1,
      "first_name": "Sebastian",
      "last_name": "Eschweiler",
      "email": "sebastian@codingthesmartway.com"
    },
    {
      "id": 2,
      "first_name": "Steve",
      "last_name": "Palmer",
      "email": "steve@codingthesmartway.com"
    },
    {
      "id": 3,
      "first_name": "Ann",
      "last_name": "Smith",
      "email": "ann@codingthesmartway.com"
    }
  ]
}

```

The JSON structure consists of one employee object which has three data sets assigned. Each employee object is consisting of four properties: id, first_name, last_name and email.

4. Run the Json server at location where your db.json file is present using command **json-server --watch db.json** . Watch parameter ensures that the server is started in watch mode which means that it watches for file changes and updates the exposed API accordingly.

5.The following htttp end points are created by Json Server

```js

GET    /employees
GET    /employees/{id}
POST   /employees
PUT    /employees/{id}
PATCH  /employees/{id}
DELETE /employees/{id}

```

### Note
1.By default Json-Server runs on port 3000, If you wish to run on different port use command **json-server -p 4000 db.json**

### References
1.https://medium.com/codingthesmartway-com-blog/create-a-rest-api-with-json-server-36da8680136d
2.https://github.com/typicode/json-server
3.https://www.youtube.com/watch?v=tvOiM_4zOzs
4.https://www.youtube.com/watch?v=6194_vuMDxo&list=PL9ok7C7Yn9A-JaUtcMwevO_FfbFNRYLfU&index=5
