## TestingMiniBytes Automation

### What is Rest
Rest is Representational State Transfer. Wheneve we send request from service to another,we dont send the object instead we send the representational state of that
object(eg Json,xm,yaml) at that particular time.

### Serialization/Marshelling
Conversion of Java Object into Json is know as Serialization or Marshelling.

### DeSerialization/UnMarshelling
Conversion of  Json into Java Object is know as DeSerialization or UnMarshelling.

### Json rules
1. {} - Json Object</br>
2. [] - Json Array</br>
3. Key-Value pair</br>
4. Each Key-Value pair is separated by commma</br>
5. All the Keys are of type String</br>
6. Values can be String,Integer,Boolean,JsonObject,JsonArray

### Rest API's are StateLess?
It means that while sending any request from client to server,One must ensure to send complete details within the request and not rely on the server remembering previous requests, REST applications require each request to contain all of the information necessary for the server to understand it. Storing session state on the server violates the REST architecture's stateless requirement.

As per the REST (REpresentational “State” Transfer) architecture, the server does not store any state about the client session on the server-side. This restriction is called Statelessness.

Each request from the client to the server must contain all of the necessary information to understand the request. The server cannot take advantage of any stored context on the server.

The application’s session state is therefore kept entirely on the client. The client is responsible for storing and handling the session related information on its own side.

This also means that the client is responsible for sending any state information to the server whenever it is needed. There should not be any session affinity or sticky session between the client and the server.


### PostMan Terminologies

 **Collection(Folder)** - Collection is a folder which is a group of similar request
 
 **Query and Path Parameters** 
 Query Parameter are used to find or filter the resources(Eg.Searching a specific product with name),It defines sort, pagination, or filter operations.These are appended to the end of the request URL, Query parameters are appended to the end of the request URL, following '?' and listed in key-value pairs, separated by '&' Syntax:

**?id=1&type=new**  
 
Path Parameter are used to identify specific resource.The path parameter defines the resource location.Path parameters are part of the endpoint and are required. For example, `/users/{id}`, `{id}` is the path parameter of the endpoint `/users`- it is pointing to a specific user's record. An endpoint can have multiple path parameters, like in the example `/organizations/{orgId}/members/{memberId}


### Import Data in Postman 
(https://www.youtube.com/watch?v=BqmZNlAIZSI&list=PLnxpMuIcxn1T4CM48trVVKybEesQWzeHm&index=1)

We can import data in Postman through

1.File </br>
2.Folder</br>
3.Link (Can be a swagger URL)</br>
4.Raw Text</br>
5.Code Repository (Github)</br>

![image](https://user-images.githubusercontent.com/52998083/185784425-a2c6a18c-4f31-4ea8-b091-d0dd754b8d5e.png)


### Dynamic Variables in Postman
(https://www.youtube.com/watch?v=5-FiYWbCbNM&list=PLnxpMuIcxn1T4CM48trVVKybEesQWzeHm&index=2)
(https://learning.postman.com/docs/writing-scripts/script-references/variables-list/)

We can dynamically set the value of Key with postman.Postman uses the faker library to generate sample data, including random names, addresses, email addresses, and much more. You can use these pre-defined variables multiple times to return different values per request.

You can use these variables like any other variable in Postman. Their values are generated at the time of execution and their names start with a $ symbol, for example $guid or $timestamp. We need to place these variables within **{{}}**

**Syntax** - {{$randomFirstName	}}

![image](https://user-images.githubusercontent.com/52998083/185784309-6de4cea6-a9c7-4cb4-84b0-66bc9e45669a.png)




