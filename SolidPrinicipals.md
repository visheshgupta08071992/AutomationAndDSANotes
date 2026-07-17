Solid Prinicipals are design rules that helps software engineer to write code that is -
* ✅ Easy to understand
* ✅ Easy to maintain
* ✅ Easy to test
* ✅ Easy to extend without breaking existing code

Think of SOLID as **5 rules for writing good object-oriented code**.

---

# Imagine You're Building a Car 🚗

Suppose you're building a car.

A well-designed car has:

* Engine does only engine work.
* Steering does only steering.
* Tires can be replaced without changing the engine.
* If you upgrade the music system, the engine shouldn't stop working.

Software should also be designed this way.

That's exactly what SOLID teaches.

---
| **SOLID Principle**                           | **Meaning**                                                                      | **Simple Explanation**                                                          | **Java Example**                                                                                                                                                                                    | **Real-Life Example**                                                                                                         | **Memory Trick**                              |
| --------------------------------------------- | -------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| **S – Single Responsibility Principle (SRP)** | A class should have **only one responsibility** (one reason to change).          | Don't put multiple jobs in one class. Keep each class focused on one task.      | `Employee` stores employee data.<br>`SalaryCalculator` calculates salary.<br>`EmployeeRepository` saves employee.<br>`EmailService` sends emails.                                                   | In a hospital, the **Doctor** treats patients, the **Receptionist** books appointments, and the **Cashier** handles payments. | **One Class = One Job**                       |
| **O – Open/Closed Principle (OCP)**           | Software should be **open for extension but closed for modification**.           | Add new features by creating new classes instead of changing existing code.     | `Discount` interface with implementations like `RegularDiscount`, `PremiumDiscount`, `VIPDiscount`, `GoldDiscount`. Adding a new discount means creating a new class instead of modifying old code. | You can plug a new USB device into your computer without changing the motherboard.                                            | **Add New, Don't Modify Old**                 |
| **L – Liskov Substitution Principle (LSP)**   | A child class should be able to replace its parent without breaking the program. | If a subclass can't behave like its parent, the inheritance hierarchy is wrong. | `Sparrow extends FlyingBird` works because sparrows can fly. `Penguin` should extend `Bird`, not `FlyingBird`, because penguins can't fly.                                                          | If you rent a car, every vehicle provided should actually be drivable. Giving a bicycle would violate expectations.           | **Child Must Behave Like Parent**             |
| **I – Interface Segregation Principle (ISP)** | Don't force a class to implement methods it doesn't need.                        | Create small, focused interfaces instead of one large interface.                | `Workable`, `Eatable`, and `Sleepable` interfaces. `Human` implements all three, while `Robot` implements only `Workable`.                                                                          | A TV remote shouldn't have buttons for a washing machine or refrigerator.                                                     | **Small Interfaces Are Better**               |
| **D – Dependency Inversion Principle (DIP)**  | Depend on **interfaces (abstractions)** instead of concrete classes.             | High-level classes shouldn't depend directly on specific implementations.       | `Computer` depends on the `Keyboard` interface. You can pass a `WiredKeyboard`, `WirelessKeyboard`, or `BluetoothKeyboard` without changing `Computer`.                                             | A wall power socket works with many devices because they all follow the same plug standard.                                   | **Depend on Interfaces, Not Implementations** |



---

# S — Single Responsibility Principle (SRP)

> **A class should have only ONE reason to change.**

Meaning:

A class should do **only one job**.

## ❌ Bad Example

Imagine an `Employee` class.

```java
class Employee {

    void calculateSalary() {
        // salary logic
    }

    void saveToDatabase() {
        // database logic
    }

    void sendEmail() {
        // email logic
    }
}
```

This class has **3 responsibilities**.

* Salary calculation
* Database saving
* Email sending

If email logic changes, this class changes.

If database changes, this class changes.

If salary rules change, this class changes.

Too many reasons to modify one class.

---

## ✅ Good Example

Separate responsibilities.

```java
class Employee {
    // employee data
}
```

```java
class SalaryCalculator {

    void calculate(Employee employee) {
    }
}
```

```java
class EmployeeRepository {

    void save(Employee employee) {
    }
}
```

```java
class EmailService {

    void send(Employee employee) {
    }
}
```

Now each class has **only one responsibility**.

---

### Real Life Example

Hospital

* Doctor → Treats patients
* Receptionist → Books appointments
* Cashier → Handles payments

Imagine if one person did all three jobs.

Chaos.

---

# O — Open/Closed Principle (OCP)

> **Open for Extension, Closed for Modification**

Meaning:

You should be able to **add new features without changing existing code.**

---

## Example

Suppose we calculate discounts.

### ❌ Bad

```java
class DiscountCalculator {

    double calculate(String customerType) {

        if(customerType.equals("Regular"))
            return 5;

        if(customerType.equals("Premium"))
            return 10;

        if(customerType.equals("VIP"))
            return 20;

        return 0;
    }
}
```

Tomorrow you add

```
Gold Customer
```

You must edit this class again.

Next month

```
Silver Customer
```

Again modify.

Eventually this becomes huge.

---

## ✅ Good

Create an interface.

```java
interface Discount {

    double calculate();
}
```

Regular customer

```java
class RegularDiscount implements Discount {

    public double calculate() {
        return 5;
    }
}
```

Premium

```java
class PremiumDiscount implements Discount {

    public double calculate() {
        return 10;
    }
}
```

VIP

```java
class VIPDiscount implements Discount {

    public double calculate() {
        return 20;
    }
}
```

Now if tomorrow Gold customer comes

Just create

```java
class GoldDiscount implements Discount {

    public double calculate() {
        return 15;
    }
}
```

No existing code changes.

---

### Real Life Example

Think about charging your phone.

Your phone already supports charging.

When USB-C came, manufacturers **added a new charger**, not redesigned the phone's internal charging logic every time.

---

# L — Liskov Substitution Principle (LSP)

> **A child class should be able to replace its parent class without breaking the program.**

---

Suppose

```java
class Bird {

    void fly() {
    }
}
```

Now

```java
class Sparrow extends Bird {
}
```

Works perfectly.

But then

```java
class Penguin extends Bird {

    void fly() {
        throw new UnsupportedOperationException();
    }
}
```

Oops!

Penguins cannot fly.

---

Now imagine

```java
Bird bird = new Penguin();

bird.fly();
```

Program crashes.

The child class cannot properly substitute the parent.

LSP is violated.

---

## Better Design

```java
class Bird {
}
```

```java
class FlyingBird extends Bird {

    void fly() {
    }
}
```

```java
class Sparrow extends FlyingBird {
}
```

```java
class Penguin extends Bird {
}
```

Now everything works correctly.

---

### Real Life Example

Imagine renting a car.

If the contract says

> Every vehicle can drive.

Then giving someone a bicycle instead would violate expectations.

The substitute should behave as promised.

---

# I — Interface Segregation Principle (ISP)

> **Don't force a class to implement methods it doesn't need.**

---

Suppose

```java
interface Worker {

    void work();

    void eat();

    void sleep();
}
```

Now Robot

```java
class Robot implements Worker {

    public void work() {}

    public void eat() {
        // ??
    }

    public void sleep() {
        // ??
    }
}
```

Robot doesn't eat.

Robot doesn't sleep.

Why force it?

---

## Better

Split interfaces.

```java
interface Workable {

    void work();
}
```

```java
interface Eatable {

    void eat();
}
```

```java
interface Sleepable {

    void sleep();
}
```

Now

```java
class Human implements Workable, Eatable, Sleepable {
}
```

Robot

```java
class Robot implements Workable {
}
```

Perfect.

---

### Real Life Example

Imagine buying a TV remote.

You only want

* Volume
* Channel

Instead the remote also has

* Air Conditioner controls
* Washing Machine controls
* Refrigerator controls

Most buttons are useless.

Small focused interfaces are better.

---

# D — Dependency Inversion Principle (DIP)

> **Depend on abstractions (interfaces), not concrete classes.**

---

Suppose

```java
class Keyboard {
}
```

Computer

```java
class Computer {

    private Keyboard keyboard = new Keyboard();
}
```

Problem:

Computer only works with one keyboard.

Tomorrow

Wireless keyboard

Bluetooth keyboard

Gaming keyboard

Need code changes.

---

## Better

Create interface.

```java
interface Keyboard {
}
```

Implementations

```java
class WiredKeyboard implements Keyboard {
}
```

```java
class WirelessKeyboard implements Keyboard {
}
```

Computer

```java
class Computer {

    private Keyboard keyboard;

    Computer(Keyboard keyboard) {
        this.keyboard = keyboard;
    }
}
```

Usage

```java
Keyboard keyboard = new WirelessKeyboard();

Computer computer = new Computer(keyboard);
```

Tomorrow

```
BluetoothKeyboard
```

Works immediately.

---

### Real Life Example

Think of a wall power socket.

The socket doesn't care whether you plug in:

* Phone charger
* Laptop charger
* Fan
* TV

It only depends on the **standard plug interface**, not a specific device.

---

# Putting It All Together

Suppose you're developing an **E-Commerce Application**.

Without SOLID:

```
Order Class

✔ Calculate Price
✔ Save Order
✔ Send Email
✔ Generate Invoice
✔ Process Payment
✔ Print Receipt
✔ Apply Discount
✔ Notify Customer
```

One giant class.

After SOLID:

```
Order
        |
        |
------------------------------
|            |               |
Payment    Invoice      Notification
Service    Service        Service
|
Discount Strategy
|
Repository
```

Each class has one job, can be extended easily, depends on interfaces, and is easier to test.

---

# Easy Way to Remember SOLID

| Principle | Meaning               | One-line Memory Trick                      |
| --------- | --------------------- | ------------------------------------------ |
| **S**     | Single Responsibility | One class = One job                        |
| **O**     | Open/Closed           | Add new features without changing old code |
| **L**     | Liskov Substitution   | Child should behave like Parent            |
| **I**     | Interface Segregation | Don't force unnecessary methods            |
| **D**     | Dependency Inversion  | Depend on interfaces, not implementations  |

## A simple mnemonic

Remember the phrase:

**"Single Objects Like Intelligent Design."**

* **S** → **Single** Responsibility
* **O** → **Objects** should be Open for extension, Closed for modification
* **L** → **Like** (child classes should behave like their parents)
* **I** → **Intelligent** interfaces (small and focused)
* **D** → **Design** with abstractions (interfaces), not concrete classes

---

Since you already work with **Java, Spring Boot, and design patterns like Builder**, the next step is to see how SOLID is applied in real projects. For example:

* **SRP** → `UserService`, `UserRepository`, `EmailService`
* **OCP** → Strategy Pattern for payment or discount calculation
* **LSP** → Proper inheritance hierarchies (e.g., `Bird`/`FlyingBird`)
* **ISP** → Small interfaces like `JpaRepository`, `CrudRepository`
* **DIP** → Spring's Dependency Injection using `@Autowired` or constructor injection with interfaces

This connection between SOLID, design patterns, and Spring is what you'll encounter most often in production Java applications.
