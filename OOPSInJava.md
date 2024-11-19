# OOPS in Java

### Summary of OOP Features in Java

| Concept       | Description                                                                 |
|---------------|-----------------------------------------------------------------------------|
| Abstraction   | Hiding implementation details and showing only the essential features of an object                |
| Encapsulation | Wrapping data (variables) and methods (functions) together in a single unit (class) and restricting direct access to some of the object's components.       |
| Inheritance   | Mechanism for creating new classes based on existing ones                  |
| Polymorphism  | Ability to process objects differently based on their data type            |


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
Encapsulation is the process of wrapping data (variables) and methods (functions) together in a single unit (class) and restricting direct access to some of the object's components.

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
Here, the `name` attribute is private, meaning it cannot be accessed directly from outside the `Person` class. Instead, public methods are provided to get and set its value. When we try to operate on public variables, one can set any values to them. For example, firstName can be set with null, a string with special characters or numbers.
Instead, if we have them as private variables, then in the setter method we can do initial business checks before setting the values to the variables.

The same gets applied for getter methods. You have the control to return a default value if some variable is null or not in the desired state.

---

