# Understanding Builder Design Pattern

**What is a design pattern?**

Design pattern is the predefined solution/template to an already existing desing problem. Problems can be creational,structural and behavioral. Example of Structural
Pattern is the Page Object Model which is widely used in Automation Frameworks and where Page Object are structured separate to test files.

**Builder Design Pattern** is the pattern which solves Creational Problem. Now what exact problem does Builder Pattern Solves? 

**Problem Statement -** </br> 
Without breaking the immuatability we need to ensure that complex objects  having large no of mandatory and optional properties can be
easily created.</br>

Different approaches which we could think of to solve the given problem - </br>

1. **Using Setter method** - Using Setter method we can set only the mandatory fields and ignore the optional field as per our needs. But if we use setter method then
we cannot ensure the object to be immuatable and anyone can update the different field of object using setter methods. So Using Setter method would'nt solve the problem as it would break the immutability condition.

2.  **Using Constructors** - With the help of constructors and not providing setter methods we can ensure that the immutability condition of Object is maintained. But consider a scenario where a class object has around 50 fields and all the 50 fields are optional and the object should be created based on the user requirment. In this case we need to create many constructors so that the user requirement is met based on his different requirements. This can be really time consuming,And it would Also  make the code too clumsy.


So to solve the above problem, we would be using **Builder Pattern**.


# How to Create a Builder Class

### Explanation (Step-by-Step with Points)

1. **Define the Outer Class with Fields:**
   - Identify fields as **mandatory** or **optional**.
   - Make the constructor private to restrict direct instantiation.

2. **Create a Static Nested Builder Class:**
   - Include Fields identical to the Outer class.
   - Include a constructor for **mandatory attributes**.

3. **Set Mandatory Attributes in Builder Constructor:**
   - Validate them (e.g., null checks) inside the builder.

4. **Add Setter Methods for Optional Attributes in Builder class:**
   - Each setter method should return the builder itself for chaining.
   - Use the same field names but assign them within the builder class.

5. **Add a `build()` Method:**
   - This method creates an instance of the outer class and passes the builder object to the private constructor.

6. **Use Builder Class to Create Objects:**
   - Pass mandatory attributes via the builder constructor.
   - Use chained methods to set optional attributes.


---

### Complete Code:
```java
public class Car {
    // Fields of the Car class
    private final String make;  // Mandatory
    private final String model; // Mandatory
    private final int year;     // Optional
    private final String color; // Optional

    // Private constructor to enforce object creation through the builder
    private Car(CarBuilder builder) {
        this.make = builder.make;
        this.model = builder.model;
        this.year = builder.year;
        this.color = builder.color;
    }

    // Static nested Builder class
    public static class CarBuilder {
        // Fields of the builder (same as outer class)
        private final String make;  // Mandatory
        private final String model; // Mandatory
        private int year;           // Optional
        private String color;       // Optional

        // Constructor to initialize mandatory attributes
        public CarBuilder(String make, String model) {
            if (make == null || model == null) {
                throw new IllegalArgumentException("Make and Model are mandatory");
            }
            this.make = make;
            this.model = model;
        }

        // Setter methods for optional attributes
        public CarBuilder setYear(int year) {
            this.year = year;
            return this;
        }

        public CarBuilder setColor(String color) {
            this.color = color;
            return this;
        }

        // Build method to create the final object
        public Car build() {
            return new Car(this);
        }
    }

    @Override
    public String toString() {
        return "Car{" +
                "make='" + make + '\'' +
                ", model='" + model + '\'' +
                ", year=" + year +
                ", color='" + color + '\'' +
                '}';
    }
}

// Example usage
public class Main {
    public static void main(String[] args) {
        // Create a car with mandatory attributes only
        Car car1 = new Car.CarBuilder("Toyota", "Camry")
                .build();

        // Create a car with both mandatory and optional attributes
        Car car2 = new Car.CarBuilder("Tesla", "Model 3")
                .setYear(2023)
                .setColor("Blue")
                .build();

        System.out.println(car1);
        System.out.println(car2);
    }
}
```


# Using Lombok to Create a Builder Class

Using Lombok, you can significantly simplify the implementation of the Builder Pattern by leveraging its annotations. Here's how to implement the same example with **Lombok**:


### Complete Code with Lombok:
```java
import lombok.Builder;
import lombok.Getter;
import lombok.ToString;

@Getter
@Builder
@ToString
public class Car {
    // Define fields with mandatory and optional attributes
    private final String make;  // Mandatory
    private final String model; // Mandatory
    private final int year;     // Optional
    private final String color; // Optional
}

// Example usage
public class Main {
    public static void main(String[] args) {
        // Create a car with mandatory attributes only
        Car car1 = Car.builder()
                .make("Toyota")
                .model("Camry")
                .build();

        // Create a car with both mandatory and optional attributes
        Car car2 = Car.builder()
                .make("Tesla")
                .model("Model 3")
                .year(2023)
                .color("Blue")
                .build();

        System.out.println(car1);
        System.out.println(car2);
    }
}
```

---

**Referance** - https://www.youtube.com/watch?v=ILvWj9ZLkqY&list=PL9ok7C7Yn9A-JaUtcMwevO_FfbFNRYLfU&index=15



