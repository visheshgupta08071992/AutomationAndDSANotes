# Understanding Builder Design Pattern

**What is a design pattern?**

Design pattern is the predefined solution/template to an already existing desing problem. Problems can be creational,structural and behavioral. Example of Structural
Pattern is the Page Object Model which is widely used in Automation Frameworks and where Page Object are structured separate to test files.

**Builder Design Pattern** is the pattern which solves Creational Problem. Now what exact problem does Builder Pattern Solves? 

**Problem Statement -** </br> 
Without breaking the immuatability we need to ensure that complex objects  having large no of mandatory and optional properties can be
easily created.</br>

Different approaches which we could think of to solve the given problem - </br>

1. **Using Setter method** - Using Setter method we can set only the mandatory fields and ignore the optional field as per our needs. But if we use setter method then
we cannot ensure the object to be immuatable and anyone can update the different field of object using setter methods. So Using Setter method would'nt solve the problem as it would break the immutability condition.

2.  **Using Constructors** - With the help of constructors and not providing setter methods we can ensure that the immutability condition of Object is maintained. But consider a scenario where a class object has around 50 fields and all the 50 fields are optional and the object should be created based on the user requirment. In this case we need to create many constructors so that the user requirement is met based on his different requirements. This can be really time consuming,And it would Also  make the code too clumsy.


So to solve the above problem, we would be using **Builder Patter**.






**Referance** - https://www.youtube.com/watch?v=ILvWj9ZLkqY&list=PL9ok7C7Yn9A-JaUtcMwevO_FfbFNRYLfU&index=15



