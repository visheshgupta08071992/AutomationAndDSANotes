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


### Building request workflows
(https://www.youtube.com/watch?v=vPUbYpH59rg&list=PLnxpMuIcxn1T4CM48trVVKybEesQWzeHm&index=5)
(https://learning.postman.com/docs/running-collections/building-workflows/)

Typically when you start a [collection run](/docs/running-collections/intro-to-collection-runs/), Postman runs all requests in the same order they appear in your collection. Requests in folders are executed first, followed by any requests in the root of the collection.

In the Collection Runner, you have the option to change the order of the requests before starting a run. However, instead of manually changing the request order each time you run the collection, you can automate this behavior using the `postman.setNextRequest()` function.

As the name suggests, `postman.setNextRequest()` enables you to specify which request Postman runs next, following the current request. Using this function, you can build custom workflows that chain requests, running them one after the other in a specific order.

<img alt="Setting the next request" src="https://assets.postman.com/postman-docs/set-next-request-v9-4.jpg" width="841px">

## Setting the next request

To specify the request to run next, add the following code on the **Tests** tab of a request. Replace `request_name` with the name of the request you want to run next.

```js
postman.setNextRequest("request_name");
```

Postman runs the specified request after completing the current request.

## Looping over a request

If you pass the name of the current request to the `setNextRequest` function, Postman will run the current request repeatedly.

<img alt="Looping over a request" src="https://assets.postman.com/postman-docs/set-next-request-loop-v9-4.jpg" width="841px">

> **Important!** Make sure to wrap `setNextRequest` in some additional logic so the request doesn't loop indefinitely. For example, you might exit the loop after a certain number of iterations or when another condition is met. Otherwise you will need to force close the Collection Runner to end the loop.

## Stopping a workflow

To stop a workflow, add the following code on the **Tests** tab of a request.

```js
postman.setNextRequest(null);
```

The collection run will stop after Postman completes the current request.

## Executing the next request only when we have the desired response code else terminating the runner

![image](https://user-images.githubusercontent.com/52998083/185802056-22f0afc9-e819-4b00-af0e-7f1fd0f08f6a.png)


### Postman Varibales (https://learning.postman.com/docs/sending-requests/variables/)

In order from broadest to narrowest, Postman variable scopes are: global, collection, environment, data, and local.

![image](https://user-images.githubusercontent.com/52998083/192996399-990e04d2-715f-4718-9aa6-a8c966be98a2.png)

So Postman checks all the scopes, starting from outside to inside (so from global towards data). The last scope that has defined the variable Postman gives priority to the same. 


**Global Variables**

Global variables enable you to access data between collections, requests, test scripts, and environments. Global variables are available throughout a workspace. 

Global variables can be defined from Environments -> Global

![image](https://user-images.githubusercontent.com/52998083/192998049-d3a02f3e-f83e-40cc-b84c-fe863a8639f0.png)


**Collection Variables**

Collection variables are available throughout the requests in a collection and are independent of environments. Collection variables don't change based on the selected environment. Collection variables are suitable if you're using a single environment, for example for auth or URL details.

Collection Variables are defined by clicking on the collection -> variables

![image](https://user-images.githubusercontent.com/52998083/193001098-e4f58012-ce42-41a8-b306-1fce52e706a3.png)



**Environment Variables**

Environment variables enable you to scope your work to different environments, for example local development versus testing or production. One environment can be active at a time. If you have a single environment, using collection variables can be more efficient.


Environment variables can be defined from Environments -> New Environment 

![image](https://user-images.githubusercontent.com/52998083/192999059-d7b7e381-c821-4e4e-bbe2-1a2b6e36fefb.png)

To use specific environment variable, Choose the environment from top right corner before running any collection

![image](https://user-images.githubusercontent.com/52998083/193001476-4c951cf9-df34-4530-a22f-95df0668832e.png)


**Local Variables**

Local variables are temporary variables that are accessed in your request scripts. Local variable values are scoped to a single request or collection run, and are no longer available when the run is complete.

```js
pm.variables.set("test","local")
```

![image](https://user-images.githubusercontent.com/52998083/193001217-79ab1c2c-c6cf-407b-a223-bbcca5e8bc92.png)

**Summarizing Variables**

1. **Env Variable** - Used to manage different environments
2. **Collection Variable** - Scope of variable is within collection
3. **Global Variable** - Scope of variable is entire workspace
4. **Local Variable** -


**Using variables**

You can use double curly braces to reference variables throughout Postman. For example, to reference a variable named "username" in your request authorization settings, you would use the following syntax with double curly braces around the name:

```js
{{username}}
```

When you run a request, Postman will resolve the variable and replace it with its current value.

For example, you could have a request URL referencing a variable as follows:

```js
https://postman-echo.com/get?customer_id={{cust_id}}
```


### Using dynamic variables

Postman provides dynamic variables you can use in your requests.

Examples of dynamic variables include:

* `{{$guid}}` : A v4-style GUID
* `{{$timestamp}}`: The current Unix timestamp in seconds
* `{{$randomInt}}`: A random integer between 0 and 1000

See the [Dynamic Variables](/docs/writing-scripts/script-references/variables-list/) section for a full list.


























