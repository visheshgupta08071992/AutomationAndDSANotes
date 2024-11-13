## Immutable class

Immutable means unmodifiable, An immutable class is a class whose Object state cannot be changed after its created. There are many immutable classes like String, Boolean, Byte, Short, Integer, Long, Float, Double etc. In short, all the wrapper classes and String class is immutable.

## Principles of Immutable Classes

1. **Declare the class as `final`**: This would avid inheritance and ensure that no other classes are extending the given class.
2. **Make all fields as `final`**: This would ensure that fields can only be assigned once and are final and constant.
3. **Make all fields `final`**: This would ensure that fields cannot be accessed directly from outside the class.
4. **No setter methods**: This wound ensure that class fields cannot be modified after object creation.
5. **Initialize all fields in the constructor**
6. **Return copies of mutable objects**: If the class contains fields that reference mutable objects (like arrays/collections/maps),
    return copies in the constructor and getter methods instead of the original objects to maintain immutability.

## Example of an Immutable Class

Here’s an example illustrating how to create an immutable class called `Employee`.

```java
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

public final class Employee {
    private final String pancardNumber;
    private final Map<String, String> attributes;

    public Employee(String pancardNumber, Map<String, String> attributes) {
        this.pancardNumber = pancardNumber;
        // Create a new HashMap to prevent external modification
        this.attributes = new HashMap<>(attributes);
    }

    public String getPancardNumber() {
        return pancardNumber;
    }

    public Map<String, String> getAttributes() {
        return new HashMap<>(attributes); // Return a new HashMap as a copy
    }
}
```

### Testing the Immutable Class

Here’s how you can test this immutable class:

```java
import java.util.HashMap;

public class ImmutableTest {
    public static void main(String[] args) {
        HashMap<String, String> attributes = new HashMap<>();
        attributes.put("Department", "Finance");
        attributes.put("Location", "New York");

        Employee emp = new Employee("ABC123", attributes);

        // Print initial values
        System.out.println("Pancard Number: " + emp.getPancardNumber());
        System.out.println("Attributes: " + emp.getAttributes());

        // Attempting to modify attributes will throw an exception
        // emp.getAttributes().put("Role", "Manager"); // This will not compile

        // Original map remains unchanged
        attributes.put("Department", "HR");
        System.out.println("Updated Original Attributes Map: " + attributes);
        System.out.println("Employee Attributes After Original Map Update: " + emp.getAttributes());

        // Attempting to modify the returned map will not affect the original Employee object
        Map<String, String> empAttributes = emp.getAttributes();
        empAttributes.put("Role", "Manager"); // This modifies only the local copy

        // Check employee attributes again
        System.out.println("Modified Local Copy Attributes: " + empAttributes);
        System.out.println("Employee Attributes After Modification Attempt: " + emp.getAttributes());

    }
}
```

### Output

The output will show that the state of the `Employee` object remains unchanged despite attempts to modify its attributes:

```
Pancard Number: ABC123
Attributes: {Department=Finance, Location=New York}
Updated Original Attributes Map: {Department=HR, Location=New York}
Employee Attributes After Original Map Update: {Department=Finance, Location=New York}
Modified Local Copy Attributes: {Department=Finance, Location=New York, Role=Manager}
Employee Attributes After Modification Attempt: {Department=Finance, Location=New York}

```

### Let's dive deeper into the protection mechanisms for deep copies:

**Constructor Protection:**

```java
this.attributes = new HashMap<>(attributes);
```

1.Creates a new HashMap with all entries from the input map </br>
2.Breaks the reference to the original map </br>
3.Any subsequent changes to the original map won't affect the Employee object </br>

**Getter Protection:**

```java
return new HashMap<>(attributes);
```

1.Returns a completely new HashMap with the same entries </br>
2.Prevents direct modification of the internal map </br>
3.Any changes to the returned map won't affect the original Employee object </br>

