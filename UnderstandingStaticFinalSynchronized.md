# Java Keywords: final, static, synchronized, volatile

These four keywords are particularly important for Java interviews, especially for SDET roles where interviewers expect a strong understanding of OOP, memory management, multithreading, and thread safety.

Let's understand each keyword with practical examples, use cases, and common interview questions.

# 1. `final` keyword

The `final` keyword is used to restrict modification.

It can be applied to:

1. Variables
2. Methods
3. Classes

### A. final variable

Once initialized, a final variable cannot be reassigned.

```
class Employee {

    final int salary = 50000;

    void display() {
        // Compilation error
        // salary = 60000;
    }
}
```

Important: A final variable must be initialized exactly once, either at declaration, in an instance initializer, or in a constructor (for instance variables).

Example:

```
class Employee {

    final int salary;

    Employee(int salary) {
        this.salary = salary;
    }
}
```

### B. final method

A final method cannot be overridden by a child class.

```
class Parent {

    final void display() {
        System.out.println("Parent display");
    }
}

class Child extends Parent {

    // Compilation error
    // void display() {}
}
```

Why use it?

When you want to prevent subclasses from changing a particular implementation.

### C. final class

A final class cannot be extended.

```
final class Vehicle {

    void start() {
        System.out.println("Vehicle started");
    }
}

// Compilation error
// class Car extends Vehicle {}
```

Example from Java: `String` is a final class.

### Important interview concept: final reference vs object

This is a very common trick question.

```
final StringBuilder sb = new StringBuilder("Hello");

sb.append(" World");  // Valid

// Compilation error
// sb = new StringBuilder("Java");
```

Why?

- You cannot change the reference to point to another object.
- You can still modify the object itself if it is mutable.



Remember

`final` does not automatically make an object immutable.



# 2. `static` keyword

The `static` keyword means a member belongs to the class rather than an individual object.

It can be applied to:

1. Variables
2. Methods
3. Initialization blocks
4. Nested classes

### A. static variable

A static variable is shared across all objects of a class.

```
class Employee {

    static String company = "MSCI";

    String employeeName;

    Employee(String name) {
        this.employeeName = name;
    }
}
```

Usage:

```
public class Main {

    public static void main(String[] args) {

        Employee e1 = new Employee("Amit");
        Employee e2 = new Employee("Rahul");

        System.out.println(Employee.company);
    }
}
```

Both objects share the same `company` variable.

[A Guide to the Static Keyword in Java | Baeldung](https://images.openai.com/static-rsc-4/Z8nEUTbF0H99yRNrJ49IYAnfhOgKz6a0GexaYsHQ2f38-AD7WjKD3hyxgb0ohFclLjYqeHVUuksB0tGFFpb2ubTcQY-LlbhjbuVPMFOL94vuvGkdCNRHmG2tOtOMTM9P_lCgZm-hfxzP5pnA1SMiv1Gk88FbBAUqWZ9bXD71l9k?purpose=inline)

[baeldung.com](https://www.baeldung.com/java-static?utm_source=chatgpt.com)

### B. static method

A static method can be called without creating an object.

```
class Calculator {

    static int add(int a, int b) {
        return a + b;
    }
}

public class Main {

    public static void main(String[] args) {

        int result = Calculator.add(10, 20);

        System.out.println(result);
    }
}
```

Important rules:

- Static methods can directly access static members.
- Static methods cannot directly access instance variables or instance methods.
- Static methods cannot use `this` or `super`.
- Static methods are hidden, not overridden, in subclasses.

### C. static block

A static block executes once when the class is initialized.

```
class Employee {

    static {
        System.out.println("Static block executed");
    }

    Employee() {
        System.out.println("Constructor executed");
    }
}
```

### D. static nested class

Java allows nested classes to be static.

```
class Outer {

    static class Inner {

        void display() {
            System.out.println("Static nested class");
        }
    }
}
```

Usage:

```
Outer.Inner obj = new Outer.Inner();
obj.display();
```

### Real-world use cases

- Utility methods such as `Math.max()`.
- Shared constants.
- Common counters.
- Factory methods.
- Helper classes.

# 3. `synchronized` keyword

The `synchronized` keyword is used in Java multithreading to ensure only one thread at a time executes a particular synchronized section for a given lock.

It helps prevent race conditions when multiple threads access shared mutable data.

### A. Understanding the problem without synchronized

Imagine two threads accessing the same bank account.

Initial balance = ₹1,000.

Both threads try to withdraw ₹500 simultaneously.

```
class BankAccount {

    int balance = 1000;

    void withdraw(int amount) {

        if (balance >= amount) {
            balance = balance - amount;
        }
    }
}
```

Without synchronization, both threads might read the balance as ₹1,000 before either updates it.

This can cause incorrect results.

### B. Using synchronized method

```
class BankAccount {

    int balance = 1000;

    synchronized void withdraw(int amount) {

        if (balance >= amount) {

            balance = balance - amount;

            System.out.println(
                Thread.currentThread().getName()
                + " remaining balance: " + balance
            );
        }
    }
}
```

Now, only one thread at a time can execute `withdraw()` on the same account object.

### C. Types of synchronization

1\. Synchronized instance method

```
synchronized void display() {
    System.out.println("Instance method");
}
```

- Acquires the object's monitor lock (`this`).
- Other threads cannot simultaneously execute another synchronized instance method using the same object.

2\. Synchronized static method

```
static synchronized void display() {
    System.out.println("Static method");
}
```

- Acquires the class object's monitor lock.
- Only one thread at a time can hold that class lock.

3\. Synchronized block

```
void display() {

    synchronized (this) {
        System.out.println("Synchronized block");
    }
}
```

You can synchronize only the critical section instead of the entire method.

### D. How synchronized works

Two threads accessing the same synchronized method

Thread 1

Lock acquired

Executing method

Thread 2

Waiting

Waiting for lock

Thread 1 releases lock

After completing the synchronized method

Thread 2 acquires lock

Now executes the synchronized method

### Important interview points

- `synchronized` provides mutual exclusion and memory visibility.
- Java uses intrinsic locks (monitor locks).
- Locks are reentrant: a thread can acquire the same monitor again.
- Synchronization can introduce performance overhead.
- Synchronization can lead to deadlocks if locks are acquired in an unsafe order.
- Two different objects have different instance locks.
- Static synchronized methods use a class-level lock, not an instance lock.

# 4. `volatile` keyword

The `volatile` keyword is also related to multithreading.

It ensures that changes made by one thread to a volatile variable are visible to other threads that subsequently read that variable.

It addresses the visibility problem in multithreading.

### A. Understanding the problem

Consider this example:

```
class SharedData {

    boolean running = true;

    void stop() {
        running = false;
    }

    void execute() {

        while (running) {
            // Keep executing
        }

        System.out.println("Thread stopped");
    }
}
```

Suppose:

- Thread 1 executes `execute()`.
- Thread 2 executes `stop()`.

Thread 2 changes `running` to `false`.

However, without proper synchronization, Thread 1 is not guaranteed to observe this change promptly. It may continue using a previously observed value.

### B. Solution using volatile

```
class SharedData {

    volatile boolean running = true;

    void stop() {
        running = false;
    }

    void execute() {

        while (running) {
            // Keep executing
        }

        System.out.println("Thread stopped");
    }
}
```

No. Static methods cannot be overridden in Java. They are called method hiding.

Let's understand this with an example.

## 1. Example: Static method hiding

```
class Parent {

    static void display() {
        System.out.println("Parent static method");
    }
}

class Child extends Parent {

    static void display() {
        System.out.println("Child static method");
    }
}

public class Main {

    public static void main(String[] args) {

        Parent p = new Parent();
        Child c = new Child();

        Parent obj = new Child();

        p.display();
        c.display();
        obj.display();
    }
}
```

Output:

```
Parent static method
Child static method
Parent static method
```

### Why does `obj.display()` print Parent?

Look at this statement:

```
Parent obj = new Child();
obj.display();
```

- Reference type = `Parent`
- Actual object type = `Child`
- Method type = `static`

Since static methods are resolved at compile time based on the reference type, Java calls `Parent.display()`.

This is called method hiding, not method overriding.

## 2. Static method vs instance method

This is the most important distinction for interviews.

| Feature      | Static method         | Instance method                  |
| ------------ | --------------------- | -------------------------------- |
| Overriding   | No                    | Yes                              |
| Binding      | Compile-time          | Runtime (for overridden methods) |
| Resolution   | Reference type        | Actual object type               |
| Polymorphism | No runtime overriding | Runtime polymorphism             |
