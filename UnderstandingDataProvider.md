# Understanding DataProvider

**What is a DataProvider**

Data Provider in TestNg is used when one needs to execute a Test against different input parameters

**Syntax and Explanation**

As shown in the below screenshot, the first parameter of two dimensioanl object mentions the number of times you want to execute a test while the second parameter indicates
number of parameter sent to a method. The below example would execute dpTest 3 times with 3 different username,password,email,address and rescode. 

![image](https://user-images.githubusercontent.com/52998083/192131795-75b99a5d-d787-4b94-9b82-2cc37b4bcae9.png)


**Implement DataProvider using HashMap**

If we need to Test Scenarios which has lot of different parameters then we make use of HashMap as shown in below screenshot

![image](https://user-images.githubusercontent.com/52998083/192131972-4b542162-ca43-4047-b6d2-bda3c447619c.png)

![image](https://user-images.githubusercontent.com/52998083/192131996-a5319c1c-8d41-48ba-90be-6a8d40e18046.png)

 







