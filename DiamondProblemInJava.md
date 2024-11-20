## Diamond Problem in Java

Diamond problem refers to an Ambiguity that arises due to Multiple inheritance when a class inherits two or more classes  having method with same name and Signature.

### Example
Consider the following example to illustrate the Diamond Problem:


```java
class D {
    void display() {
        System.out.println("Display from D");
    }
}

class A extends D {
    void display() {
        System.out.println("Display from A");
    }
}

class B extends D {
    void display() {
        System.out.println("Display from B");
    }
}

class C extends A, B { // This line would cause a compile-time error in Java
}
```

In this scenario, if Class C attempts to call `display()`, the compiler will not know whether to use the implementation from Class A or Class B, resulting in an ambiguity error.



## Java's Approach to the Diamond Problem

Java does not allow multiple inheritance of classes to avoid this ambiguity. You can only extend one class at a time. However, Java does allow multiple inheritance of interfaces, which can lead to a similar situation.

### 1. Using Interfaces
Java interfaces can declare methods without providing an implementation. When a class implements multiple interfaces that contain methods with the same name, it must provide its own implementation of those methods. Here’s how you can implement it:

```java
interface A {
    void display();
}

interface B {
    void display();
}

class C implements A, B {
    public void display() {
        System.out.println("Display from C");
    }
}
```

In this case, Class C must implement the `display()` method, thus resolving any ambiguity.

### 2. Default Methods in Interfaces (Java 8 and later)
With Java 8, interfaces can have default methods that provide a body. If two interfaces provide default implementations of the same method, the implementing class must explicitly override the method and specify which interface's implementation to use:

```java
interface A {
    default void display() {
        System.out.println("Display from A");
    }
}

interface B {
    default void display() {
        System.out.println("Display from B");
    }
}

class C implements A, B {
    public void display() {
        // To resolve ambiguity:
        A.super.display(); // Calls display from interface A
        // or
        B.super.display(); // Calls display from interface B
    }
}
```

