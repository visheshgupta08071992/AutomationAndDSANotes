## Understanding Javascript

## How to run Javascript applications

To run Javascript application one needs to install Node.js, Node.js is just runtime environment for running your JavaScript application

**Reference video to install Node.js** - https://www.youtube.com/watch?v=Gu9KdbpzSvk&list=PL6flErFppaj2TYXXee5Zt_rR_RpOTBfm1&index=3

Once Node.js is installed, Open command prompt and hit below commands to ensure that it is perfectly installed

**node -v** - To check node version</br>
**npm -v** - To check Node Package Manager version. npm is similar to maven/gradle in Java</br>
**npm --help** - Is used for getting help on npm commands

![image](https://github.com/visheshgupta08071992/AutomationAndDSANotes/assets/52998083/b8408ff3-a38b-4585-b38d-7956d568c55e)

**To run Javascript program use command** - node filename.js

## Understanding different concepts in Javascript

| Concept | Explanation |
| -------- | -------- |
| For Printing   | console.log("Hello World")    |
| Declaring variables in Javascript   |  In Javascript variables are very loosely type. It means variables can hold data of any type </br></br> eg. **var a =4, var b="Hello",var c =5.678,let z=67,let m="Test"** </br> </br> Uptill Javascript 5 we could declare variable only using var keyword but from ES6 i.e JavaScript 6 we could also declare varaibles using let and const keywords.</br></br> **Difference between var and let keyword** </br> 1. we cannot redeclare variable using let but we can do it using var keyword. </br> ![image](https://github.com/visheshgupta08071992/AutomationAndDSANotes/assets/52998083/71e277a9-fd4f-4750-8448-1802eb80a28c) </br>![image](https://github.com/visheshgupta08071992/AutomationAndDSANotes/assets/52998083/80fbeaf8-004c-4564-aa7b-e2b6f4a44fa7) </br> Reassigning is allowed by let but redeclaring is not allowed. </br></br> **Difference between let and const keyword** </br> Const keyword is used to define constant variables, We cannot changes the value of Const variable but we can change the value of variable declare with let|
|   How to know dataType of variable in Javascript  | typeOf() method is used to determine the dataType of variable in JavaScript.</br></br> ![image](https://github.com/visheshgupta08071992/AutomationAndDSANotes/assets/52998083/5c51b1b1-513d-4dd2-882f-fa3202b2b45d) |


 **For Printing** 
 
 ```js
 console.log("Hello World") 
 ```

 **Declaring variables in Javascript**
 
 In Javascript variables are very loosely type. It means variables can hold data of any type </br></br> eg. **var a =4, var b="Hello",var c =5.678,let z=67,let m="Test"** </br> </br> Uptill Javascript 5 we could declare variable only using var keyword but from ES6 i.e JavaScript 6 we could also declare varaibles using let and const keywords.</br></br> **Difference between var and let keyword** </br> 1. we cannot redeclare variable using let but we can do it using var keyword. </br> ![image](https://github.com/visheshgupta08071992/AutomationAndDSANotes/assets/52998083/71e277a9-fd4f-4750-8448-1802eb80a28c) </br>![image](https://github.com/visheshgupta08071992/AutomationAndDSANotes/assets/52998083/80fbeaf8-004c-4564-aa7b-e2b6f4a44fa7) </br> Reassigning is allowed by let but redeclaring is not allowed. </br></br> **Difference between let and const keyword** </br> Const keyword is used to define constant variables, We cannot changes the value of Const variable but we can change the value of variable declare with let
 
 
 **How to know dataType of variable in Javascript**
 
 typeOf() method is used to determine the dataType of variable in JavaScript.</br></br> ![image](https://github.com/visheshgupta08071992/AutomationAndDSANotes/assets/52998083/5c51b1b1-513d-4dd2-882f-fa3202b2b45d)
 
 **Differnet ways of Declaring Array**
 
 ```js
 //Declaring and initializing Array using 1st Way
let a=new Array(6)
for(let i=0;i<a.length;i++){
    a[i] = i
}
console.log(a) // [ 0, 1, 2, 3, 4, 5 ]

//Declaring and initializing Array 2nd way

let b= new Array(1,2,3,4,5,6)
console.log(b) // [ 1, 2, 3, 4, 5, 6 ]

//Declaring and initializing Array 3rd way

let c =[1,2,3,4,5,6]
console.log(c) // [ 1, 2, 3, 4, 5, 6 ]

 ```
 
 **Understanding Different methods in Arrays**
 
 ```js
 //Declaring and initializing Array using 1st Way
let a=new Array(6)
for(let i=0;i<a.length;i++){
    a[i] = i
}
console.log(a) // [ 0, 1, 2, 3, 4, 5 ]

/*To add and remove element from end push and pop methods are used respectively  
  -push adds element to end of array
  -pop removes element  from end of array */

a.push(6)
console.log(a) //[ 0, 1, 2, 3, 4, 5 ,6]

a.pop()
console.log(a)  //[ 0, 1, 2, 3, 4, 5]


/*To add and remove element from start unshift and shift methods are used respectively  
  -unshift adds element to start of the array
  -shift removes element from start of the array*/

a.unshift(-1)
console.log(a) //[ -1,0, 1, 2, 3, 4, 5]


a.shift()
console.log(a) //[ 0, 1, 2, 3, 4, 5]


/*To add,remove or replace an  element in middle of an array we need to use splice method

Syntax: array.splice(startIndex, deleteCount, item1, item2, ..., itemX)

Parameters:

- `startIndex`: An integer value that specifies the position where to start adding or removing elements in the array (required).
- `deleteCount`: An integer value that specifies the number of elements to be removed from the array (optional). If set to 0, no elements are removed.
- `item1, item2, ..., itemX`: The elements to be added to the array (optional).
*/

let fruits = ['apple', 'banana', 'mango', 'orange'];

// removing an element
fruits.splice(1, 1); // remove 'banana'

console.log(fruits); // Output: ['apple', 'mango', 'orange']

// adding an element
fruits.splice(1, 0, 'pear'); // add 'pear' at index 1

console.log(fruits); // Output: ['apple', 'pear', 'mango', 'orange']

// replacing an element
fruits.splice(2, 1, 'grape'); // replace 'mango' with 'grape'

console.log(fruits); // Output: ['apple', 'pear', 'grape', 'orange']


/*The slice() method in JavaScript allows us to extract a section of an array and return it as a new array.

Syntax - array.slice(startIndex, endIndex)

Parameters:

startIndex: Required. Specifies the index position where the extraction should begin. This parameter is inclusive (i.e., the element at this index position will be included in the new array).
endIndex: Optional. Specifies the index position where the extraction should end. This parameter is exclusive (i.e., the element at this index position will not be included in the new array). If you omit this parameter, slice() will extract all elements from the startIndex to the end of the array.

*/

const fruit = ['apple', 'banana', 'cherry', 'orange', 'watermelon']

// Extract elements from index 1 to index 3 (exclusive) and store them in a new array
const selectedFruits = fruit.slice(1, 3)

console.log(selectedFruits) // Output: ['banana', 'cherry']

/* concat() method is used to combine two or more array and return a new Array */

let arr1=[1,2,3]
let arr2=[4]
let arr3=[5,6]

arr4 = arr1.concat(arr2).concat(arr3)

console.log(arr4) // [1,2,3,4,5,6]

/* Sorting an Array
   -Array of String can be sorted in ascending order using sort method
   -Array of string can be sorted in descending prder using reverse method
   -To sort Array of integer we need to pass comparator within sort method
*/

let arr5=[ 'banana', 'cherry', 'apple', 'watermelon','orange']

//Sort in ascending order
arr5.sort()
console.log(arr5) // [ 'apple', 'banana', 'cherry', 'orange', 'watermelon' ]

//Sort in descending order
arr5.reverse()
console.log(arr5) // [ 'watermelon', 'orange', 'cherry', 'banana', 'apple' ]

let arr6=[6,5,4,3,2,1]

//Sort in ascending order
arr6.sort((a,b) => a-b)
console.log(arr6) //[ 1, 2, 3, 4, 5, 6 ]

//Sort in descending order
arr6.sort((a,b) => b - a)
console.log(arr6) //[ 6, 5, 4, 3, 2, 1 ]



 
 ```







