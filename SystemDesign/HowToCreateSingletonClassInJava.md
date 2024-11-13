## Singleton class

A Singleton class is a design pattern that restricts the instantiation of a class to one single instance. 

## Steps to Create a Singleton Class 

1. **Private Constructor**: Make the constructor of the class private so that no other class can instantiate it.
2. **Static Variable`**: Create a static variable which would the single instance of the class.
3. **Public Static Method**: Create a public static method which would return the instance of the class. This method will create the instance if it does not already exist.
