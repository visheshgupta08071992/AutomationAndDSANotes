## Different ways of creating request body in Rest Assured

* #### Passing the RequestBody as String

we can directly send request body as a String as shown in the below image.

![image](https://user-images.githubusercontent.com/52998083/188301805-51fefd81-2df3-4dd1-bdea-90e9992a167c.png)

The above approach is not recommended and should only be used when we need to quickly check the behavior. The given approach should not be used for long and dynamic json.


* #### Passing the RequestBody from external file
we can directly pass the json file to body as shown in the below image. The disadvantages of the given approach are that it can only be used for Static data. 

![image](https://user-images.githubusercontent.com/52998083/188302514-73f5ad58-3453-469f-8c2a-43ef5de3d44d.png)

Another disadvantage is that the request content does not gets logged if directly send the file to body,Only the file path is logged  (![image](https://user-images.githubusercontent.com/52998083/188302794-bbef84f2-a84d-4c31-8c06-1020bee53076.png)




* #### Passing the RequestBody from external file and converting to String

We can send the request from an external file and converting into string as shown in the below image. The Given approach is not suitable when we have lot of dynamic attributes.
we always send the new dynamic values using faker library. 

![image](https://user-images.githubusercontent.com/52998083/188302357-885ceddc-8168-4eb6-8b7e-071447c8b04f.png)



