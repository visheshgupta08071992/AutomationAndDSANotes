# OOPS in Java

### Summary of OOP Features in Java

| Concept       | Description                                                                 |
|---------------|-----------------------------------------------------------------------------|
| Abstraction   | Hiding implementation details and showing only the essential features of an object                |
| Encapsulation | Wrapping data (variables) and methods (functions) together in a single unit (class) and restricting direct access to some of the object's components.       |
| Inheritance   | Inheritance is a mechanism in Java where one class(subclass) can inherit the properties and methods of another class(superclass)               |
| Polymorphism  | Same name different implementation. This can be achieved through method overloading (compile-time polymorphism) and method overriding (runtime polymorphism).</br> </br> **Method Overloading:** Same method name with different parameters.</br>**Method Overriding:** A subclass provides a specific implementation of a method that is already defined in its superclass.   |


---

### **1. Abstraction**
Abstraction is the process of hiding implementation details and showing only the essential features of an object. Abstraction can be achieved using abstract classes and interfaces.

**Example:**

```java
abstract class Animal {
    abstract void makeSound(); // Abstract method

    void eat() { // Concrete method
        System.out.println("This animal eats food.");
    }
}

class Dog extends Animal {
    @Override
    void makeSound() {
        System.out.println("Dog barks");
    }
}

public class Main {
    public static void main(String[] args) {
        Animal dog = new Dog();
        dog.makeSound();
        dog.eat();
    }
}
```
---

### **2. Encapsulation**
Encapsulation is the process of wrapping data (variables) and methods (functions) together in a single unit (class) and restricting direct access to some of the object's components. As part of Encapsulation we make all the Data Variable as Private and all the Methods as Public which would perform operations on Private Variables. If anyone wants to access the Private variable, They can access through public methods.

**Example:**
```java
class Person {
    private String firstName; // Private variable

    public String getName() { // Getter method
        return firstName;
    }

    public void setName(String firstName) { // Setter method
        this.firstName = firstName;
    }
}
```
Here, the `firstName` attribute is private, meaning it cannot be accessed directly from outside the `Person` class. Instead, public methods are provided to get and set its value. When we try to operate on public variables, one can set any values to them. For example, firstName can be set with null, a string with special characters or numbers.
Instead, if we have them as private variables, then in the setter method we can do initial business checks before setting the values to the variables.

The same gets applied for getter methods. You have the control to return a default value if some variable is null or not in the desired state.

---

### **3. Inheritance**
Inheritance is a mechanism in Java where one class(subclass) can inherit the properties and methods of another class(superclass).

- **Why?** To promote code reuse.
- **How?** By using the `extends` keyword.

**Example:**

```java
class Vehicle {
    void start() {
        System.out.println("Vehicle is starting...");
    }
}

class Car extends Vehicle {
    void drive() {
        System.out.println("Car is driving...");
    }
}

public class Main {
    public static void main(String[] args) {
        Car car = new Car();
        car.start(); // Inherited from Vehicle
        car.drive();
    }
}
```

---

### **4. Polymorphism** (https://www.javatpoint.com/runtime-polymorphism-in-java)
Same name different implementation. This can be achieved through method overloading (compile-time polymorphism) and method overriding (runtime polymorphism).</br> </br> **Method Overloading:** Same method name with different parameters.Metho Overloading represents Compile Time Polymorphism. A class can have multiple methods with same name but differnt no or Type of Paramters, A Compiler knows which method would be called based on the passed paramter . This choice is made during compilation, which is why it's called "compile-time polymorphism."</br> </br> **Method Overriding:** A subclass provides a specific implementation of a method that is already defined in its superclass.

**Example of Method Overloading (Compile-time Polymorphism):**

```java
class Calculator {
    int add(int a, int b) {
        return a + b;
    }

    int add(int a, int b, int c) {
        return a + b + c;
    }
    double add(double a, double b) {
           return a + b; // Adds two doubles
       }
}

public class Main {
    public static void main(String[] args) {
        Calculator calc = new Calculator();
        // Compile-time polymorphism: selecting the appropriate add method based on parameter types  

        System.out.println("Sum of 2 numbers: " + calc.add(5, 10));
        System.out.println("Sum of 3 numbers: " + calc.add(5, 10, 15));
        System.out.println("Sum of doubles: " + calc.add(2.5, 3.7));  
    }
}
```

**Example of Method Overriding (Run-time Polymorphism):**

```java
class Animal {
    void makeSound() {
        System.out.println("Some generic animal sound");
    }
}

class Cat extends Animal {
    @Override
    void makeSound() {
        System.out.println("Cat meows");
    }
}

public class Main {
    public static void main(String[] args) {
        Animal animal = new Cat();
        animal.makeSound(); // Calls the overridden method in Cat
    }
}
```

**Overloading Rules**:
   - Methods can be overloaded by changing:
     - The number of parameters.
     - The types of parameters.
     - The order of parameters.
   - Methods cannot be overloaded by changing only the return type.

**Example**:
   Here’s an example to illustrate that you cannot overload methods based solely on different return types:

   ```java
   class Example {
       public int calculate(int a, int b) {
           return a + b; // Returns an integer
       }

       // This would cause a compile-time error
       // public double calculate(int a, int b) {
       //     return (double)(a + b);
       // }
   }
   ```

   In this code, attempting to define a second `calculate` method with the same parameter types but a different return type will result in a compile-time error because both methods have the same signature.

 **Valid Overloading Example**:
   Here’s how you can correctly overload methods:

   ```java
   class Calculator {
       public int add(int a, int b) {
           return a + b; // Adds two integers
       }

       public double add(double a, double b) {
           return a + b; // Adds two doubles
       }

       public int add(int a, int b, int c) {
           return a + b + c; // Adds three integers
       } 
    }  
   }


   ```

In this valid example, the `add` method is overloaded with different parameter types and numbers, which is permissible in Java.




---


