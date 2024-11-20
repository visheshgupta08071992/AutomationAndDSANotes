In Java, both **abstract classes** and **interfaces** are used to achieve abstraction. However, they are designed for different purposes and have distinct characteristics. Below is a detailed comparison along with examples.

---



### **Differences Between Abstract Class and Interface**


| **Abstract Class**                                                                                 | **Interface**                                                                                   |
|----------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| Abstract class can have abstract and non-abstract methods.                                         | Interface can have only abstract methods. Since Java 8, it can have default and static methods also. |
| Abstract class doesn't support multiple inheritance.                                               | Interface supports multiple inheritance.                                                       |
| Abstract class can have final, non-final, static, and non-static variables.                        | Interface has only static and final variables.                                                 |
| Abstract class can provide the implementation of an interface.                                     | Interface can't provide the implementation of an abstract class.                               |
| The `abstract` keyword is used to declare an abstract class.                                       | The `interface` keyword is used to declare an interface.                                       |
| An abstract class can extend another Java class and implement multiple Java interfaces.            | An interface can extend another Java interface only.                                           |
| An abstract class can be extended using the keyword `extends`.                                     | An interface can be implemented using the keyword `implements`.                                |
| A Java abstract class can have class members like `private`, `protected`, etc.                    | Members of a Java interface are `public` by default.                                           |
| An abstract class should be used when SuperClass and SubClass shares some relationship, For Car is a supr class and we can have multiple subclasses like BMW,Audi,Maruti each have all functionalities of Car while their specififc functionalities          | An interface should be used to share a common behavior between unrelated classes. For example, Good Speaking quality which a Lecturer,A Politician,An Actor all might have but they are completely unrelated, We can create an Interface GoodSpeaking and share these common quality in all the unrelated classes                                         |
| **Example:**                                                                                      | **Example:**                                                                                  |
| `public abstract class Shape { public abstract void draw(); }`                                     | `public interface Drawable { void draw(); }`                                                  |



Simply, abstract class achieves partial abstraction (0 to 100%) whereas interface achieves fully abstraction (100%).

---

### **Examples**

#### **1. Abstract Class Example**

```java
abstract class Animal {
    String name; // Instance variable

    // Abstract method
    abstract void makeSound();

    // Concrete method
    void eat() {
        System.out.println(name + " is eating.");
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
        Dog dog = new Dog();
        dog.name = "Buddy";
        dog.makeSound();
        dog.eat();
    }
}
```

---

#### **2. Interface Example**

```java
interface Vehicle {
    // Abstract method
    void start();

    // Default method (introduced in Java 8)
    default void fuel() {
        System.out.println("Vehicle is being fueled.");
    }
}

class Car implements Vehicle {
    @Override
    public void start() {
        System.out.println("Car is starting.");
    }
}

public class Main {
    public static void main(String[] args) {
        Car car = new Car();
        car.start();
        car.fuel();
    }
}
```

---

#### **3. Multiple Inheritance with Interface**

One of the key advantages of interfaces is the ability to implement multiple interfaces, which is not possible with abstract classes.

```java
interface Flyable {
    void fly();
}

interface Swimmable {
    void swim();
}

class Bird implements Flyable, Swimmable {
    @Override
    public void fly() {
        System.out.println("Bird is flying.");
    }

    @Override
    public void swim() {
        System.out.println("Bird is swimming.");
    }
}

public class Main {
    public static void main(String[] args) {
        Bird bird = new Bird();
        bird.fly();
        bird.swim();
    }
}
```

---

