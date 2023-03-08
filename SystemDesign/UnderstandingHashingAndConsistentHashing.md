### What is Hashing

Hashing is nothing but converting some kind of data be it a String or a Object or so on into an integer with the help of Hash Function.

![image](https://user-images.githubusercontent.com/52998083/223074500-050cc8a9-3fd7-48c5-ae0f-023ea3911a41.png)


**But what is the actual purpose of Hashing or how converting some kind of data into integer is useful**

Think about a real world example where you have a list of names and you want to search the name. If the names are sorted in alphabetical order then the complexity
is nlogn(Binary Search), And if the names are not sorted in alphabetical order then the complexity becomes o(n) (Linear search).  Can Hashing improve the complexity? Yes with the help of hashFunction we can convert these names into an integer which acts as indices of an array where the names get stored, Making the search easier with help of indices having o(1) complexity.


![image](https://user-images.githubusercontent.com/52998083/223075669-b9bc0b3e-bdcf-401a-8f78-6b712423774c.png)

![image](https://user-images.githubusercontent.com/52998083/223079384-a979ddcd-2cf7-4b4e-bf95-953b77a7346d.png)

The question comes what is the range of the HashValue. The range of the HashValue is from 0 to 2^32, And we should not keep that much big array to store these names. Even if you had 100 to 1000 names it would be a wastage of lot of space by keeping an array of such a large size. So what do we do after calculating the Hash we take 
a modulus, Let's say we have to store 4 names, what we will would do we will twice or thrice the size of array thinking that our data might grow by 2x or 3x. So that's why since we have four values we are thinnking that lets take an array of size 8. Once we take an array of size 8 and we do a mod on all these values, then all these values get converted into single integer. There can be scenario where multiple hashcode can end up at the same index, In this case we try to save list in that index, Instead of saving just one one string we try to save list in that case.


![image](https://user-images.githubusercontent.com/52998083/223077622-7ebc6a40-2966-4e6e-a75d-22e0fde4c1f2.png)

![image](https://user-images.githubusercontent.com/52998083/223082983-0040a2e1-5d11-45ee-bff3-d592829f347f.png)


**What is the use of Consistent Hashing when we have Hashing in place**

As shown in the below image Consider we have four names and four different servers. With the help of hashing each name gets stored correctly stored with each server.

![image](https://user-images.githubusercontent.com/52998083/223084485-a19d95ca-3c98-404e-8aa0-6d60658ba38e.png)


The problem with hashing occurs when we increase or decrease the server based on the increase on decrease of load. Consider now the no of server has been decreased to three. The change in no of sever also results change in our hashing function from modulus 4 to modulus 3 which resulted in in reassinging of 3 names to different server. That is around 75% of our data has bee reassigned. This is the problem with normal hashing function that when you want to increase or decrease the no of server then you might need to move around a lot of data.

Consistent Hashing is the solution to the given problem where we could minimize these movement of data.


![image](https://user-images.githubusercontent.com/52998083/223086327-2d2e8431-d2dc-4160-9849-3551a2948fc4.png)


### What is Consitent Hashing

The problem with simple modulo caching is when we add or remove a server, all our existing mappings will be broken. Hence, we are required to remap  most of our keys to a different server. 

In Consitent Hashing all the Keys and Sevrers are hashed using the same hash function and are placed on the edge of the circle. To find out which server to ask for a given key or store a given key, we need to first locate the key on the circle and move in a clockwise direction until we find a server.Let’s use the above example and place them on the hash ring. In this case, the minimum value on the circle is 0 and the maximum value is 100.

![image](https://user-images.githubusercontent.com/52998083/223719663-a805bb00-68a4-4c7a-82d4-22b545bcf5be.png)

According to consistent hashing rule, bob@example.com and mark@example.com are on server S2, smith@example.com and adam@example.com are on server S3 and alex@example.com and john@example.com are on server S1.

In consistent hashing when a server is removed or added then the only key from that server are relocated. For example, if server S3 is removed then, all keys from server S3 will be moved to server S1 but keys stored on server S1 and S2 are not relocated. But there is one problem when server S3 is removed then keys from S3 are not equally distributed among remaining servers S1 and S2. They were only assigned to server S1 which will increase the load on server S1.

To evenly distribute the load among servers when a server is added or removed, it creates a fixed number of replicas ( known as virtual nodes) of each server and distributed it along the circle. So instead of server labels S1, S2 and S3, we will have S10 S11…S19, S20 S21…S29 and S30 S31…S39. The factor for a number of replicas is also known as weight, depends on the situation.

All keys which are mapped to replicas Sij are stored on server Si. To find a key we do the same thing, find the position of the key on the circle and then move forward until you find a server replica. If server replica is Sij then the key is stored in server Si.

Suppose server S3 is removed, then all S3 replicas with labels S30 S31 … S39 must be removed. Now the objects keys adjacent to S3X labels will be automatically re-assigned to S1X and S2X. All keys originally assigned to S1 and S2 will not be moved.

Similar things happen if we add a server. Suppose we want to add a server S4 as a replacement of S3 then we need to add labels S40 S41 … S49. In the ideal case, one-third of keys from S1 and S2 will be reassigned to S4.


### Referance

Hashing - https://www.youtube.com/watch?v=cITtFpz3a3Y </br>

Conistent Hashing

https://www.youtube.com/watch?v=oKAU6LaYFhw

https://www.youtube.com/watch?v=jqUNbqfsnuw

