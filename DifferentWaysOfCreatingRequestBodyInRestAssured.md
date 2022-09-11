## Different ways of creating request body in Rest Assured

* #### Passing the RequestBody as String

we can directly send request body as a String as shown in the below image.

![image](https://user-images.githubusercontent.com/52998083/188301805-51fefd81-2df3-4dd1-bdea-90e9992a167c.png)

The above approach is not recommended and should only be used when we need to quickly check the behavior. The given approach should not be used for long and dynamic json. Also if one uses the given approach then if the request body is updated the he would need to update request body in all the class where it is passed as string.


* #### Passing the RequestBody from external file
we can directly pass the json file to body as shown in the below image. The disadvantages of the given approach are that it can only be used for Static data. 

![image](https://user-images.githubusercontent.com/52998083/188302514-73f5ad58-3453-469f-8c2a-43ef5de3d44d.png)

Another disadvantage is that the request content does not gets logged if directly send the file to body,Only the file path is logged  (![image](https://user-images.githubusercontent.com/52998083/188302794-bbef84f2-a84d-4c31-8c06-1020bee53076.png)




* #### Passing the RequestBody from external file and converting to String

We can send the request from an external file and converting into string as shown in the below image. The Given approach is not suitable when we have lot of dynamic attributes.
we always send the new dynamic values using faker library. 

![image](https://user-images.githubusercontent.com/52998083/188302357-885ceddc-8168-4eb6-8b7e-071447c8b04f.png)


* #### Creating  RequestBody using HashMap and List

We can create the request body using Map and List as shown in below image. Below Request body is created using Map and and List.

```js

{
        "id":{{$randomInt}},
        "first_name": "{{$randomFirstName}}",
        "last_name": "{{$randomLastName}}",
        "email": "{{$randomEmail}}",
        "jobs":["Tester","Trainer"],
        "favFoods":{
            "breakfast":"idly",
            "lunch":"rice",
            "dinner":["Chapati","Milk"]
        }
}

```

![image](https://user-images.githubusercontent.com/52998083/188307145-edd8c8da-1524-40b9-8343-b8bb41133e06.png)

While using the given approach ensure to add Jackson data bind dependency in your project so that RestAssured internally converts the Java Map Object into Json.
If Jackson DataBind is not added then it would result in serialization error as shown in below image ![image](https://user-images.githubusercontent.com/52998083/188307302-1570e0f9-2122-47ad-9e4f-815ba4c9cfd7.png)

The given approach is not very useful when we have very large json files. Also in the given approach we need to mention the generic type. You can see we have created HashMap which is storing Object in order to ensure that it stores values of String,Integer and Boolean.


* #### Creating  RequestBody using JsonObject and JsonArray

To use this approach we need add json dependency in our project.

![image](https://user-images.githubusercontent.com/52998083/188307984-f71d020e-0d98-45c1-82ca-5a4a9ba4e115.png)

Ensure converting body to String as body is a JsonObject and RestAssured doesnot serialize JsonObject.


* #### Creating  RequestBody by defining static methods returning String Body within a class

As we can see in the below image we have created RequestBodies class which has method addEmployee returing the String Body

![image](https://user-images.githubusercontent.com/52998083/188346280-2fe2c722-8c32-4954-b031-ce33c203af20.png)

![image](https://user-images.githubusercontent.com/52998083/188346360-5d9f32e6-6712-432d-8046-81bf086e69e3.png)

We are directly able to call addEmployee method of RequestBodies class as we have used Static import to import static methods of class RequestBodies. Static import is used to import static methods of a class

![image](https://user-images.githubusercontent.com/52998083/188346487-0574f8ca-c870-4419-901a-1c6b566070d4.png)


* #### Creating  RequestBody using Pojo Classes

One of the advantage of creating request bodies using Pojo is they can be used both for serialization as well as deserialization. Also Pojo bodies are used by 
developers as well, So the same pojo body can be reused in Testing Frameworks, Please refer below screenshot for understanding creation of request bodies using Pojo. We have used Lombok for generating - Getters,Setter and Constructers of Pojo Classes.


```js

{
        "id":{{$randomInt}},
        "first_name": "{{$randomFirstName}}",
        "last_name": "{{$randomLastName}}",
        "email": "{{$randomEmail}}",
        "jobs":["Tester","Trainer"],
        "favFoods":{
            "breakfast":"idly",
            "lunch":"rice",
            "dinner":["Chapati","Milk"]
        }
}

```

**Corresponding POJO Classes**

![image](https://user-images.githubusercontent.com/52998083/189514244-e6597286-075e-4d08-a82e-8b8c83b9d6ff.png)


![image](https://user-images.githubusercontent.com/52998083/189514241-26d11605-d736-4018-a1fb-80ce80453f28.png)

![image](https://user-images.githubusercontent.com/52998083/189514251-d10b0c1e-5a9e-48a3-b0ff-f648ddde2946.png)


**Corresponding RestAssured Code**

![image](https://user-images.githubusercontent.com/52998083/189514284-22932e4b-e540-462a-b8fd-ba27680ff2a9.png)

























