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

/*  
  The forEach() method in JavaScript is used to loop over the elements of an array and perform a specific action for each element. 
  It allows you to iterate through an array and execute a function on each element.

  Syntax - array.forEach(callbackFunction)

*/

const numbers = [1, 2, 3, 4, 5];

numbers.forEach((currentValue) => console.log(currentValue));

// Output:
// 1
// 2
// 3
// 4
// 5



/* 
   
  The reduce() method is a built-in method in JavaScript that allows you to calculate a single value from an array of values. 
   You can use it to sum up all the elements in an array, find the maximum or minimum value, or perform any other kind of calculation that reduces an array to a single value.

   Syntax - array.reduce(callbackFunction, initialValue)

   Parameters:

   callbackFunction: This is a function that you provide, which will be called for each element of the array. 
   It takes four parameters: accumulator, currentValue, currentIndex, and array. The accumulator is the value that accumulates the results, 
   and currentValue is the current element being processed. The currentIndex is the index of the current element, and array is the original array.
   
   initialValue: This is an optional parameter. It specifies the initial value of the accumulator. 
   If you don't provide it, the first element of the array will be used as the initial value, and the reduction starts from 
   the second element.

 */


 //Find sum of all elements of an array using reduce method
 
 let marks=[1,2,3,4,5]

 let sum = marks.reduce((accumulater,marks) => accumulater + marks,0)

 console.log(sum) // 15

 //Find Max of all elements using reduce

 let max = marks.reduce((a,b) => a>b?a:b)

 console.log(max) //5

  //Find Min of all elements using reduce

  let min = marks.reduce((a,b) => a>b?b:a)

  console.log(min) // 1


 /* 
   The filter() method in JavaScript is used to create a new array that contains elements from an existing array that pass a certain condition. 

   Syntax - array.filter(callbackFunction)

 */ 

 
 //Print all even nos from an array using filter method
 
 let nos =[1,2,3,4,5,6]

 nos.filter((a) => a%2==0).forEach(a => console.log(a)) // 2 4 6

  //Print all odd nos from an array using filter method

  let oddNos =  nos.filter((a) => a%2!=0)

  console.log(oddNos) // 1,3,5


 /* 
    The map() method  is used  transform the elements of the array and create a new array based on the transformations.
 
    Syntax - array.map(callbackFunction) 
 
 */ 

 // Find squares of No using Map method in Javascript
 
 let no=[1,2,3,4,5]

 let sqrNo = no.map((e) => e*2)

 console.log(sqrNo) // [ 2, 4, 6, 8, 10 ]

 /* 
    The flatMap() method is used to transform a nested array into single array
 
    Syntax - array.flatMap(callbackFunction)

 */

//Transform the below nested array into single array    

let nestedArray = [[1,2],[3,4],[5,6]]

let singleArray = nestedArray.flatMap((e) => e)

console.log(singleArray) // [ 1, 2, 3, 4, 5, 6 ]

//Split each word of an array into individual characters using flatMap

const words = ["hello", "world", "javascript"];

const characters = words.flatMap((currentValue) =>  currentValue.split(""));

console.log(characters); // Output: ["h", "e", "l", "l", "o", "w", "o", "r", "l", "d", "j", "a", "v", "a", "s", "c", "r", "i", "p", "t"]
 
 ```
 
 **Understanding Functions in JS**
 
 ```js
 /* Different ways of declaring functions in js*/

/* Traditional Way */

function add(a,b){
    return a + b
}

let sum = add(2,3)
console.log(sum) //5

/* Using Anyonmus function -- Function expressions
   
   Only Anyonmus function can be assigned to a variable

*/

// Anyonmus function getting assigned to a variable addNos
let addNos = (a,b) => a+b

let sumOfNo = addNos(5,5)

console.log(sumOfNo) //10
 
 ```

**Understanding Strings in JS**

```js

//Declaring String

let day='tuesday'

//Printing the length
console.log(day.length) //7

//Finding substring using slice method, Staring index is inclusive, End Index is exclusive

let partialString=day.slice(1,4) 
console.log(partialString) // ues

//Finding substring using subString method, Staring index is inclusive, End Index is exclusive

let partialString1=day.substring(1,4)
console.log(partialString1) // ues

/* Finding the character at specified index */

console.log(day[0]) // t
console.log(day.charAt(0)) // t


/* 
    split() - Splits a string into an array of substrings 
    based on a specified separator and returns the array.

*/

let str='Hi are you listening'

let strArr=str.split(" ")

console.log(strArr) // [ 'Hi', 'are', 'you', 'listening' ]

/* trim() - Removes whitespace from both ends of a string. */

let str1 = "   Hello   "

console.log(str1.length) // 11
//After trimming

console.log(str1.trim().length) // 5

/* 
   parseInt is used for converting String to a No 
   toString is used for converting No to a String
*/

let a = '25'
let b = '50'

let c = parseInt(a) + parseInt(b)

console.log(c) //75

//Convert no to String
let d = c.toString()
console.log(d + " is " + typeof(d)) // 75 is String


/*concat two string using either concat method or + operator  */

let s1 = 'day'

s2 = s1 + " is funday"

console.log(s2) // day is funday

let m1 = 'day'

m2 = m1.concat(" is funday")

console.log(m2) // day is funday

```

**Commonly used string methods in JavaScript along with their descriptions and examples:**

| Method           | Description                                                                                       | Example                                                     |
|------------------|---------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| `charAt()`       | Returns the character at the specified index of a string.                                        | `const str = "Hello"; console.log(str.charAt(1));`           |
| `concat()`       | Concatenates two or more strings and returns a new string.                                        | `const str1 = "Hello"; const str2 = "World"; console.log(str1.concat(str2));` |
| `indexOf()`      | Returns the index of the first occurrence of a specified value in a string.                       | `const str = "Hello World"; console.log(str.indexOf("World"));` |
| `toLowerCase()`  | Converts a string to lowercase letters.                                                           | `const str = "HELLO"; console.log(str.toLowerCase());`        |
| `toUpperCase()`  | Converts a string to uppercase letters.                                                           | `const str = "hello"; console.log(str.toUpperCase());`        |
| `trim()`         | Removes whitespace from both ends of a string.                                                    | `const str = "  Hello  "; console.log(str.trim());`           |
| `replace()`      | Replaces a specified value or regular expression in a string with another value.                   | `const str = "Hello World"; console.log(str.replace("World", "Universe"));` |
| `split()`        | Splits a string into an array of substrings based on a specified separator and returns the array.  | `const str = "Hello,World"; console.log(str.split(","));`     |
| `substring()`    | Returns the part of a string between two specified indices.                                       | `const str = "Hello World"; console.log(str.substring(6, 11));` |
| `length`         | Returns the length of a string.                                                                   | `const str = "Hello"; console.log(str.length);`               |



**Understanding Objects in JS**

```js

/* 
  Object in JavaScript is collection of properties
  Properties are defined as Key-Value pair, key is always a String while Value could be of any dataType
*/

// Creating Object with different dataTypes

let person = {
    name: 'Rohit',
    age:25,
    isPlayer:true,
    intrests:['cricket','footbal'],
    address:{
        city:'Mumbai',
        state:'Maharashtra'
    }
}

//Retrieving the values of each key of an Object

console.log(person.name) // Rohit
console.log(person.intrests[1]) // footbal

console.log(person.address.state) // Maharashtra

//Retrieving the values of each key of an Object in Array Style

console.log(person["name"]) // Rohit
console.log(person["intrests"][1]) // footbal

console.log(person["address"].state) // Maharashtra

// Adding a key to Object person and check the key is added

person.gender = "male"

console.log(person)

/* {
    name: 'Rohit',
    age: 25,
    isPlayer: true,
    intrests: [ 'cricket', 'footbal' ],
    address: { city: 'Mumbai', state: 'Maharashtra' },
    gender: 'male'
  } */

  console.log('gender' in person) //true

  // Deleting a key from Object and check the key does not exist

  delete person.gender

  console.log('gender' in person) //false


/* Getting all the keys of Object using Object.keys() method */

let personKeys = Object.keys(person)
console.log(personKeys)  // [ 'name', 'age', 'isPlayer', 'intrests', 'address' ]

/* Getting all the values of Object using Object.values() method */

let personValues = Object.values(person)
console.log(personValues) 

/* [
    'Rohit',
    25,
    true,
    [ 'cricket', 'footbal' ],
    { city: 'Mumbai', state: 'Maharashtra' }
  ] */


 /* Getting all the key and values of Object in a nested array using Object.entries() method */ 

 let entries = Object.entries(person)
 console.log(entries)

 /* 
 
 [
  [ 'name', 'Rohit' ],
  [ 'age', 25 ],
  [ 'isPlayer', true ],
  [ 'intrests', [ 'cricket', 'footbal' ] ],
  [ 'address', { city: 'Mumbai', state: 'Maharashtra' } ]
]
 
 */



/* 
   Iterate Objects in Javascript.
   There are several ways to iterate Objects in Javascript.

   1.Using for..in loop
   2.Using Object.keys
   3.Using Object.entries

*/


// Using for..in

const person1 = {
    name: "John",
    age: 30,
    city: "New York"
  };
  
  for (let key in person1) {
    console.log(key + ": " + person1[key]);
  }
  
/* 
name: John
age: 30
city: New York

*/


// Using Object.keys

const person2 = {
    name: "John",
    age: 30,
    city: "New York"
  };

 let keys=Object.keys(person2)
 
 for (let i = 0; i < keys.length; i++) {
    const key = keys[i];
    console.log(key + ": " + person2[key]);
  }
  
  /* 
name: John
age: 30
city: New York

*/

// Using Object.entries

const person3 = {
    name: "John",
    age: 30,
    city: "New York"
  };
  
  const entries1 = Object.entries(person3);
  
  for (let i = 0; i < entries1.length; i++) {
    const [key, value] = entries1[i];
    console.log(key + ": " + value);
  }
 
    /* 
name: John
age: 30
city: New York

*/

```




