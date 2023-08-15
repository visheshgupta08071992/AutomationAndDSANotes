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

 **For Printing** 
 
 ```js
 console.log("Hello World") 
 ```

 **Declaring variables in Javascript**
 
 In Javascript variables are very loosely type. It means variables can hold data of any type </br></br> eg. **var a =4, var b="Hello",var c =5.678,let z=67,let m="Test"** </br> </br> Uptill Javascript 5 we could declare variable only using var keyword but from ES6 i.e JavaScript 6 we could also declare varaibles using let and const keywords.</br></br> **Difference between var and let keyword** </br> 1. we cannot redeclare variable using let but we can do it using var keyword. </br> ![image](https://github.com/visheshgupta08071992/AutomationAndDSANotes/assets/52998083/71e277a9-fd4f-4750-8448-1802eb80a28c) </br>![image](https://github.com/visheshgupta08071992/AutomationAndDSANotes/assets/52998083/80fbeaf8-004c-4564-aa7b-e2b6f4a44fa7) </br> Reassigning is allowed by let but redeclaring is not allowed. </br></br> **Difference between let and const keyword** </br> Const keyword is used to define constant variables, We cannot changes the value of Const variable but we can change the value of variable declare with let
 
 
 **How to know dataType of variable in Javascript**
 
 typeOf() method is used to determine the dataType of variable in JavaScript.</br></br> ![image](https://github.com/visheshgupta08071992/AutomationAndDSANotes/assets/52998083/5c51b1b1-513d-4dd2-882f-fa3202b2b45d)

 ```js
let a=4
let b=78.98
let c="Hello"
let e=true
let g

if(typeof a === 'number'){
    console.log(a + ' is number')
}

if(typeof b === 'number'){
    console.log(b + ' is number')
}

if(typeof c === 'string'){
    console.log(c + ' is string')
}

if(typeof e === 'boolean'){
    console.log(e + ' is boolean')
}

if(typeof g === 'undefined'){
    console.log(g + ' is undefined')
}

```
 
 ## Understanding Arrays
 
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

/*

The Array.from() method in JavaScript is used to create a new array instance 
from an iterable object or an array-like object. 
It allows you to convert objects that are iterable, such as arrays or strings, into a new array.

*/

//Convert a String to Array

const str = 'Hello';
const arr = Array.from(str);

console.log(arr); // Output: ['H', 'e', 'l', 'l', 'o']

//Remove Duplicates from an Array

let a = [2,2,4,4,5,5,6,7,3,3,9,1,8]

let b = Array.from(new Set(a))
console.log(b) 

/* [
  2, 4, 5, 6, 7,
  3, 9, 1, 8
] */

//Mapping array elements
const nums = [1, 2, 3, 4];
const multiplied = Array.from(nums, (num) => num * 2);

console.log(multiplied); // Output: [2, 4, 6, 8]

//Check if Array contains specific value

const language =['java','javascript','python']

console.log(language.includes('ruby')) // false
console.log(language.includes('python')) // true

//Converting an Array into String

let message =['Hi','Hello','Sumeet']
let mssg = message.join('')
console.log(mssg) // HiHelloSumeet

let messageWithSpace =  message.join(' ')
console.log(messageWithSpace) // Hi Hello Sumeet

//Check if an array is Empty

let emptyArr=[]
if(emptyArr.length===0){
    console.log('Array is Empty')
}

 
 ```
 
 ## Understanding Functions in JS
 
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

## Understanding Strings in JS

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



## Understanding Objects in JS

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

// Checking if the Object has a given property

console.log(person.hasOwnProperty('name')) //true
console.log(person.hasOwnProperty('hobby')) //false

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

## Understanding Spread Operator in Javascript

The spread operator in JavaScript is a powerful tool that allows you to easily manipulate arrays and objects. It's represented by three dots `...` and has a couple of different use cases.

**1. Creating Clones:**

You can create a clone of an array or an object using the spread operator. This is particularly useful to avoid modifying the original data:

```javascript
const originalArray = [1, 2, 3];
const cloneArray = [...originalArray];

const originalObject = { a: 1, b: 2 };
const cloneObject = { ...originalObject };
```

**2. Combining Arrays,Oject:**


```javascript
const array1 = [1, 2, 3];
const array2 = [4, 5, 6];

const combinedArray = [...array1, ...array2];
console.log(combinedArray); // Output: [1, 2, 3, 4, 5, 6]

const obj1= {a:1,b:2}
const obj2={c:[1,2,3],d:{e:1}}
const objCombine = {...obj1,...obj2} 


console.log(objCombine); // { a: 1, b: 2, c: [ 1, 2, 3 ], d: { e: 1 } }

```

In this example, the spread operator takes each element from `array1` and `array2` and combines them into a new array called `combinedArray`.

**3. Spreading Objects:**

You can also use the spread operator with objects. When you spread an object, it creates a shallow copy of the object, and you can add or override properties easily:

```javascript
const person = { name: 'John', age: 25 };
const updatedPerson = { ...person, age: 26, city: 'New York' };

console.log(updatedPerson);
// Output: { name: 'John', age: 26, city: 'New York' }
```

In this case, the spread operator copies the properties of the `person` object into the `updatedPerson` object. The `age` property is overridden, and a new property `city` is added.

**4. Spreading Function Arguments:**

The spread operator is also useful for working with function arguments. It allows you to pass an array or iterable of values as separate arguments to a function:

```javascript
function addNumbers(a, b, c) {
  return a + b + c;
}

const numbers = [2, 3, 4];
const sum = addNumbers(...numbers);
console.log(sum); // Output: 9
```

Here, the spread operator helps pass the values from the `numbers` array as individual arguments to the `addNumbers` function.

In summary, the spread operator in JavaScript allows you to unpack elements from arrays, copy properties from objects, pass iterable values as function arguments, and create shallow clones of arrays and objects. It's a versatile tool that simplifies working with data in various scenarios.



## Understanding difference between == and === operators in Javascript

In JavaScript, the double equals operator (`==`) and the triple equals operator (`===`) are used for comparison between values. However, they differ in terms of their behavior and how they handle data types.

The double equals operator (`==`) performs a loose comparison, where type coercion is allowed. It checks if the values on both sides are equal after converting them to a common type. This means that JavaScript will try to convert the values to the same type before making the comparison. Here's an example:

```javascript
console.log(5 == "5"); // true
console.log(true == 1); // true
console.log(null == undefined); // true
```

In the first example, the number `5` is converted to a string `"5"` before the comparison, resulting in equality. In the second example, the boolean `true` is converted to the number `1`, which is then compared to `1`. In the third example, `null` and `undefined` are considered equal in loose comparison.

On the other hand, the triple equals operator (`===`) performs a strict comparison, where no type coercion takes place. It checks if the values on both sides are not only equal in value but also have the same type. Here's an example:

```javascript
console.log(5 === "5"); // false
console.log(true === 1); // false
console.log(null === undefined); // false
```

In this case, all the comparisons evaluate to `false` because the types of the values on both sides are different.

In general, it is recommended to use the triple equals operator (`===`) for comparisons in JavaScript because it avoids unexpected type coercion. It provides a more precise and predictable way of comparing values.


## Understanding classes in Javascript

**People.js**

```javascript

/* 
  Classes in Javascript are introduced in ES6 Engine 

  Classes is preferred over objects as with help of one prototype of class 
  we could create n different object

*/

// module.exports is used for exporting class so that it could be used in another files

module.exports=class People
{
    //First way of defining property
    age = 25

    /*Defining property using getter method, if we add get infront of method 
    then that is treated as property */
    get location(){
        return 'Canada'
    }

    //constructor
    constructor(firstname,lastname){
       this.firstname = firstname
       this.lastname = lastname
    }

    //Class Method
    fullname(){
        return this.firstname + this.lastname
    }
}


```

**Student.js which inherits People.js**

```javascript

const People=require('./People')

module.exports=class Student extends People{

    /* 
       If parent class has any constructor then your child class 
       should also implement similar constructor
    */ 
    constructor(firstname,lastname){
        
        /* Another rule is you have to call your parent class constructor
           as first step in child class constructor
        */
        super(firstname,lastname)
    }

    get location(){
        return 'America'
    }

}

```

**UsingPeopleAndStudent.js**

```js

//Catching Class People and Student in People and Student variable respectively
const People=require('./People')
const Student=require('./Student')

let people = new People('Rohit','Sharma')

console.log(people.age)
console.log(people.location)
console.log(people.fullname())


let student = new Student('Ishan','Sharma')

console.log(student.age)
console.log(student.location)
console.log(student.fullname())


```

## QuickTips

```js
//1.Creating Clones

const originalArray = [1, 2, 3];
const cloneArray = [...originalArray];

const originalObject = { a: 1, b: 2 };
const cloneObject = { ...originalObject };

console.log(cloneArray) // [ 1, 2, 3 ]
console.log(cloneObject) // { a: 1, b: 2 }

//2. Combining Arrays

const array1 = [1, 2, 3];
const array2 = [4, 5, 6];

const combinedArray = [...array1, ...array2];
console.log(combinedArray); // Output: [1, 2, 3, 4, 5, 6]

//3. Combining Objects

const obj1= {a:1,b:2}
const obj2={c:[1,2,3],d:{e:1}}
const objCombine = {...obj1,...obj2} 


console.log(objCombine); // { a: 1, b: 2, c: [ 1, 2, 3 ], d: { e: 1 } }



//4.Find Unique values from Array

const array=[1,2,2,3,4,5,3,6,6]

//Using,Array.from
let uniqueArr= Array.from(new Set(array))

console.log(uniqueArr) // [ 1, 2, 3, 4, 5, 6 ]

//Using Spread Operator

let uniqueArray= [...new Set(array)]

console.log(uniqueArray) // [ 1, 2, 3, 4, 5, 6 ]

//5. Int to String
const num =32

//using toString Method
const numString1 = num.toString()
console.log(numString1 + " is " + typeof(numString1)) // 32 is string

//using ''
const numString2 = num + ''
console.log(numString2 + " is " + typeof(numString2)) // 32 is string
//using String() constructor
const numString3 = String(num)
console.log(numString3 + " is " + typeof(numString3)) // 32 is string

//6. String to int

const s1="53"
const s2= parseInt(s1)
console.log(s2 + " is " + typeof(s2)) // 53 is number

//7. float to int

const s10=54.567
const s20= parseInt(s10)
console.log(s20) // 54

//8. Swap variables

/*

let a=10
let c=20
[a,c] = [c,a]
console.log(a) //20
console.log(c) //10

*/

//9. Verify if an object has a given property

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
//using hasOwnProperty
console.log(person.hasOwnProperty('name')) //true
console.log(person.hasOwnProperty('hobby')) //false

//using in
console.log('name' in person) //true
console.log('hobby' in person) //false

//10. Check if Array contains specific value

const language =['java','javascript','python']

console.log(language.includes('ruby')) // false
console.log(language.includes('python')) // true


//11. Converting an Array into String

let message =['Hi','Hello','Sumeet']
let mssg = message.join('')
console.log(mssg) // HiHelloSumeet

let messageWithSpace =  message.join(' ')
console.log(messageWithSpace) // Hi Hello Sumeet

//12. Truncate An Array

let numbers= [0,1,2,3,4,5,6,7]
numbers.length=3
console.log(numbers) // [ 0, 1, 2 ]

//13. Check if an array is Empty

let emptyArr=[]
if(emptyArr.length===0){
    console.log('Array is Empty')
}

//14. Checking variable if of particular type

let a=4
let b=78.98
let c="Hello"
let e=true
let g

if(typeof a === 'number'){
    console.log(a + ' is number')
}

if(typeof b === 'number'){
    console.log(b + ' is number')
}

if(typeof c === 'string'){
    console.log(c + ' is string')
}

if(typeof e === 'boolean'){
    console.log(e + ' is boolean')
}

if(typeof g === 'undefined'){
    console.log(g + ' is undefined')
}


```

## Understanding Callbacks,Promises and Asysc Await in Javascript


**Blog** - https://www.freecodecamp.org/news/javascript-async-await-tutorial-learn-callbacks-promises-async-await-by-making-icecream/ </br>
**Corresponding Video** - https://www.youtube.com/watch?v=n5ZtTO1ArWg </br>

**Nice read for Promises after going through either the above video/blog** - https://kkirtigoel01.medium.com/promises-in-javascript-js-27baf0e506b5


# async/await

async/await is a syntax introduced in JavaScript to make working with asynchronous code even easier. It allows you to write asynchronous code in a more sequential and readable way, similar to synchronous code.

### How it works

To use async/await, you need to mark a function with the `async` keyword. This tells JavaScript that the function contains asynchronous code and will use the `await` keyword to pause its execution until a promise is resolved.

Here's an example:

```javascript
async function fetchData() {
    return new Promise((resolve, reject) => {
        // Simulating an asynchronous operation
        setTimeout(() => {
            const data = 'This is the fetched data';
            resolve(data);
            // If an error occurs: reject(new Error('Something went wrong'));
        }, 2000);
    });
}

async function processData() {
    try {
        const data = await fetchData();
        console.log('Fetched data:', data);
    } catch (error) {
        console.error('Error:', error);
    }
}

processData();
```

In the example above, we have an `async` function called `fetchData` that returns a promise. It simulates an asynchronous operation that takes 2 seconds and resolves with some data. The `processData` function is also marked as `async`.

Inside `processData`, we use the `await` keyword to pause the execution until the promise returned by `fetchData` is resolved. This allows us to assign the fetched data to the `data` variable.

### Handling errors

async/await provides an easy way to handle errors using the `try/catch` block. Any errors thrown inside the `async` function or when awaiting a promise will be caught by the `catch` block.

In the example above, if an error occurs during the asynchronous operation, such as a network failure, the `reject` function can be called inside the `fetchData` function. This will trigger the `catch` block in `processData`, allowing us to handle the error gracefully.

### Benefits of async/await

- **Readability**: async/await makes asynchronous code look and feel more like synchronous code, making it easier to understand and maintain.
- **Error handling**: With try/catch blocks, error handling becomes more straightforward and intuitive.
- **Sequencing**: async/await allows you to write asynchronous code in a sequential manner, avoiding the need for deeply nested callbacks or complex Promise chaining.

Remember, when using async/await, you should always handle errors using try/catch to ensure your code handles failures gracefully.

That's it! You now have a basic understanding of async/await in JavaScript. Feel free to experiment with these concepts and explore further to become more comfortable with asynchronous programming.




