## Understanding NodeJs

1.NodeJs is runtime environment for Javacript on Server.</br>
2.In NodeJs single thread can manage multiple connections, This is possible because of Non-blocking IO model which makes use of callbacks to do tasks asynchronously.

## What is NPM

NPM is node package manager which is used to manage packages(dependencies) for Node project. It is similar to Maven/Gradle in Java.

**Some of the useful npm command**

**npm -v** - Used to check Node Version</br>

**npm --help** - Used to get all npm commands</br>

**npm init** - Used to initialize Node Project and create Package.json file which consist of all the external dependencies of Project.</br>

**npm install {packageName} --save** - Used to install specific node package, Once the package is installed then the dependency gets added in package.json file. --save is required if your NPM version is less then 5 then -- save would be required.</br>

**npm i {packageName}** - Can also be used to install specific node package. Once we install the package the dependency gets addedg within **package.json** and **node_modules** folder gets created which consist of dependency packages. We don't push node_modules folder to github as it is very heavy and anyone can install node_modules using npm</br>

**npm i -g {packageName}** - Used to install package globally in system and use in any project.</br>

**npm uninstall {packageName}** - Used to uninstall a package.</br>

**npm install --save-dev nodemon** - Used to install a package as dev dependency. Dev dependency package is used ony during development.</br>

## Undestanding package.json and package-lock.json

**package.json** - It consist of all the dependencies required by your project. It is similar to POM file in maven.</br>

**package-lock.json** - It is a dependency tree. It specifies all the dependencies along with their version which the  dependencies in package.json file are using.</br>


## Understanding modules in NodeJs

There are mainly three types of module in nodejs -</br>

1.**FileBased**  - FileBased Modules means module/code which we need to export from one file to another file.

**File1**

```js

/*  FileBased Modules means module/code which we neeed to export from one file to another file. */


let person = {
    "name":"Ramesh",
    "age":26,
    "Hobby":["cricket","badminton"],
    "message": (name) =>{console.log("Hey I am : ",name)}
}

let lunch = "poha"

/*
module.exports=person
module.exports=lunch

We cannot export each object separately,  Only the last assignment to 'module.exports' will be effective. 
So the 'person' object will not be exported.

*/

/* To fix this we  need to create a new object that contains both the 'person' object and the 'lunch' variable, and then export that object */

let exportObj = {
    person: person,
    lunch: lunch
}

module.exports = exportObj

```

**File2**

```js

//Used for Importing
let File1 = require("./File1")


console.log(File1.lunch)
console.log(File1.person.Hobby[1])
File1.person.message("Rahul")


```


2.**InBuilt** - BuiltIn modules are the modules which are bydefault provided by node.js. We can check all the built in modules provided by node.js here - https://nodejs.org/api/ . Majorly used BuiltIn Modules are FS,Path,OS,Http,Url  https://betterprogramming.pub/4-very-useful-built-in-node-js-modules-b734e140174c</br> 

```js
/* 
BuiltIn modules are the modules which are by default provided by node.js.

We can check all the built in modules provided by node.js here - https://nodejs.org/api/

Majorly used BuiltIn Modules are FS,Path,OS,Http,Url
*/

const fs=require("fs")

fs.readFile('./Test', 'utf8', (err,data) =>{
    if (err) throw err;
    console.log(data);
});

console.log("I am out of ReadFile Function")

/* 

I am out of ReadFile Function
Hello, This is Rakesh

Note - ReadFile is Async FUnction,hence I am out of ReadFile Function is 
executed before and then when the data is read then File Data is printed in Console

We need to use readfileSync function so that operation executes sequentially

*/

fs.writeFile('./Test2', 'Hello Node.js', 'utf8',() =>{
    console.log("Data has been written")
})



```



3.**ThirdParty** - Thirdparty Modules are the Modules which are developed by someone else, We need to explicitly download them. Some of the popular third-party modules are Mongoose, express, angular,loadash,underscore </br>


### CommonJs and ECMAScript Modules

In Node.js, there are two ways to handle modules: CommonJS and EcmaScript modules (ES modules). 

1. CommonJS Modules:
CommonJS is the default module system in Node.js. It uses `require()` to import modules and `module.exports` or `exports` to export variables, functions, or objects.

Example:
Consider a file named `math.js` that has some math-related functions:

```javascript
// math.js
const sum = (a, b) => a + b;
const multiply = (a, b) => a * b;

module.exports = { sum, multiply };
```

To use the `math.js` module in another file, use `require()`:

```javascript
// index.js
const math = require('./math');

console.log(math.sum(2, 4)); // Output: 6
console.log(math.multiply(3, 5)); // Output: 15
```

In the `index.js` file, we import the `math.js` module using `require('./math')` and store it in the `math` variable. We can then access the exported functions using the `math` object.

2. EcmaScript Modules (ES Modules):
ES modules were introduced as an experimental feature in Node.js version 12 and became stable in version 14. They are imported using the `import` statement and exported using the `export` keyword.

Example:
Consider the same `math.js` module using ES modules:

```javascript
// math.js
const sum = (a, b) => a + b;
const multiply = (a, b) => a * b;

export { sum, multiply };
```

To use the ES module in another file, use the `import` statement:

```javascript
// index.js
import { sum, multiply } from './math';

console.log(sum(2, 4)); // Output: 6
console.log(multiply(3, 5)); // Output: 15
```

In the `index.js` file, we use the `import { sum, multiply } from './math'` statement to import the specific functions directly. Then, we can use these functions without any need for an object or namespace.

Note: To use ES modules in Node.js, ensure that the file extension is `.mjs` and the `"type"` field in `package.json` is set to `"module"`. Alternatively, you can use the `.cjs` file extension for CommonJS modules.


## Reference

**Why was Nodejs developed** - https://www.youtube.com/watch?v=WjzLVU-aFXI


**Explain how Nodejs is Single Threaded Non-Blocking EventDriven** - https://www.youtube.com/watch?v=mR1SQn5nDIA

**Learn NodeJs** - 

https://www.youtube.com/watch?v=BSO9C8Z-YV8

https://www.youtube.com/watch?v=BLl32FvcdVM

















