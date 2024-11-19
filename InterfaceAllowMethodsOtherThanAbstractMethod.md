Prior to Java 8, interfaces in Java were completely abstract, meaning they could only declare methods without providing any implementation. This caused certain challenges:

1. **Backward Compatibility**: When a new method was added to an interface, all implementing classes needed to implement it, breaking existing code.
2. **Reusable Utility Methods**: Developers often wanted to provide reusable methods common to all implementers of an interface but couldn't do so directly in the interface.
3. **Modern Functional Programming Needs**: Functional programming and concepts like lambda expressions, introduced in Java 8, required more flexibility in interface design.

To address these issues, **default methods** and **static methods** were introduced in interfaces in Java 8.

---

### **Key Benefits of Default and Static Methods**

#### **1. Default Methods**
- Allow interfaces to provide a default implementation for methods.
- Existing classes implementing the interface don’t need to override the default method unless they want a custom behavior.

#### **2. Static Methods**
- Allow interfaces to define utility methods that are specific to the interface.
- These methods belong to the interface itself and cannot be overridden by implementing classes.

---

### **Example: Default Methods**

```java
interface Vehicle {
    void start();

    // Default method with implementation
    default void fuel() {
        System.out.println("Fueling the vehicle...");
    }
}

class Car implements Vehicle {
    @Override
    public void start() {
        System.out.println("Car is starting...");
    }
}

class Bike implements Vehicle {
    @Override
    public void start() {
        System.out.println("Bike is starting...");
    }

    // Overriding the default method
    @Override
    public void fuel() {
        System.out.println("Fueling the bike differently...");
    }
}

public class Main {
    public static void main(String[] args) {
        Vehicle car = new Car();
        car.start();
        car.fuel();

        Vehicle bike = new Bike();
        bike.start();
        bike.fuel();
    }
}
```

**Output:**
```
Car is starting...
Fueling the vehicle...
Bike is starting...
Fueling the bike differently...
```

---

### **Example: Static Methods**

```java
interface MathUtils {
    // Static method
    static int add(int a, int b) {
        return a + b;
    }

    static int multiply(int a, int b) {
        return a * b;
    }
}

public class Main {
    public static void main(String[] args) {
        // Calling static methods of the interface
        int sum = MathUtils.add(5, 10);
        int product = MathUtils.multiply(5, 10);

        System.out.println("Sum: " + sum);
        System.out.println("Product: " + product);
    }
}
```

**Output:**
```
Sum: 15
Product: 50
```

---

### **Why Introduced in Java 8?**

1. **Backward Compatibility**: Default methods allowed the addition of new methods to existing interfaces (e.g., `java.util.Collection`) without breaking their implementations.
   - Example: `Collection` in Java 8 added methods like `stream()` and `forEach()` as default methods.
2. **Avoid Utility Classes**: Static methods in interfaces eliminated the need for separate utility classes like `Collections` or `Math` for common functionality.
3. **Functional Interfaces**: Functional interfaces (e.g., `Comparator`) benefited from default methods, enabling them to include commonly used behavior.
   - Example: `Comparator` added a default method `reversed()`.

---

### **Real-World Example**

Consider a real-world scenario where a **Payment** interface defines a default method for transaction logs:

```java
interface Payment {
    void processPayment(double amount);

    // Default method to log payment
    default void logTransaction(double amount) {
        System.out.println("Transaction logged for amount: $" + amount);
    }

    // Static method for utility
    static boolean validateAmount(double amount) {
        return amount > 0;
    }
}

class CreditCardPayment implements Payment {
    @Override
    public void processPayment(double amount) {
        if (Payment.validateAmount(amount)) {
            System.out.println("Processing credit card payment for $" + amount);
            logTransaction(amount);
        } else {
            System.out.println("Invalid payment amount.");
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Payment payment = new CreditCardPayment();
        payment.processPayment(150.0);
    }
}
```

**Output:**
```
Processing credit card payment for $150.0
Transaction logged for amount: $150.0
```

---

### **Summary**

- **Default Methods**: Allow providing a default implementation in interfaces, making them more flexible and backward-compatible.
- **Static Methods**: Enable defining utility methods directly in interfaces without requiring external utility classes.
- **Java 8 Motivation**: Enhanced functional programming support and maintaining backward compatibility while improving flexibility.

Let me know if you'd like further clarification or deeper examples!
