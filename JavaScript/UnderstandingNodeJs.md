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


## Reference

**Why was Nodejs developed** - https://www.youtube.com/watch?v=WjzLVU-aFXI


**Explain how Nodejs is Single Threaded Non-Blocking EventDriven** - https://www.youtube.com/watch?v=mR1SQn5nDIA















