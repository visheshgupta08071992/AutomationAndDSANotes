# Java Program to Implement `equals()` and `hashCode()`

This is a very important Java interview question, especially for SDET roles because it is commonly used with `HashMap`, `HashSet`, and collections.

Let's understand it with a simple real-world example.

Suppose we have two `Employee` objects:

- Employee 1: ID = 101, Name = Vishesh
- Employee 2: ID = 101, Name = Vishesh

Although these are two different objects in memory, logically they represent the same employee.

We want Java to consider these objects equal.

## 1. Complete Java program

```

import java.util.Objects;

class Employee {

    int id;
    String name;

    Employee(int id, String name) {
        this.id = id;
        this.name = name;
    }

    // Overriding equals()
    @Override
    public boolean equals(Object obj) {

        if (this == obj) {
            return true;
        }

        if (obj == null || getClass() != obj.getClass()) {
            return false;
        }

        Employee employee = (Employee) obj;

        return id == employee.id &&
               Objects.equals(name, employee.name);
    }

    // Overriding hashCode()
    @Override
    public int hashCode() {
        return Objects.hash(id, name);
    }
}

public class Main {

    public static void main(String[] args) {

        Employee emp1 = new Employee(101, "Vishesh");
        Employee emp2 = new Employee(101, "Vishesh");
        Employee emp3 = new Employee(102, "Akshay");

        System.out.println(emp1.equals(emp2));
        System.out.println(emp1.equals(emp3));

        System.out.println(emp1.hashCode());
        System.out.println(emp2.hashCode());
        System.out.println(emp3.hashCode());
    }
}

```

## 2. Expected output

```
true
false
Same hash code for emp1 and emp2
A potentially different hash code for emp3
```

The exact integer hash codes depend on the implementation and should not be memorized.

## 3. Understand equals() step by step

Let's understand each condition in the `equals()` method.

Step 1:

```
if (this == obj) {
    return true;
}
```

Checks whether both references point to the exact same object in memory.

If yes, they are obviously equal.

Step 2:

```
if (obj == null || getClass() != obj.getClass()) {
    return false;
}
```

Two checks happen here:

- If the object passed is null, return false.
- If both objects belong to different classes, return false.

Step 3:

```
Employee employee = (Employee) obj;
```

We convert the generic `Object` into an `Employee` object using typecasting.

Why?

Because we need to access Employee-specific properties such as `id` and `name`.

Step 4:

```
return id == employee.id &&
       Objects.equals(name, employee.name);
```

Now we compare the actual data.

- Are both employee IDs equal?
- Are both employee names equal?

If both conditions are true, `equals()` returns true.

Otherwise, it returns false.

## 4. Understand hashCode()

Our implementation:

```
@Override
public int hashCode() {
    return Objects.hash(id, name);
}
```

In simple words, `hashCode()` generates an integer based on the object's fields.

For example:

| Object | ID  | Name    | Hash code |
| ------ | --- | ------- | --------- |
| emp1   | 101 | Vishesh | H1        |
| emp2   | 101 | Vishesh | H1        |
| emp3   | 102 | Akshay  | H2        |

Because emp1 and emp2 have the same data, they generate the same hash code.

Important: Different objects can also generate the same hash code. This is called a hash collision.

## 5. Why do we need both equals() and hashCode()?

This is the most important part for interviews.

Consider a `HashSet`:

```
Set<Employee> employees = new HashSet<>();

employees.add(emp1);
employees.add(emp2);
employees.add(emp3);

System.out.println(employees.size());
```

Output:

```
2
```

Why?

1. `emp1` is added to the HashSet.
2. `emp2` has the same hash code as emp1, so Java checks `equals()` to determine whether they are equal.
3. Since `equals()` returns true, emp2 is treated as a duplicate.
4. `emp3` is different, so it gets added.

Therefore, the size is 2.


## 6. Important contract between equals() and hashCode()

Remember these three rules for your interview:

| Rule   | Explanation                                                                  |
| ------ | ---------------------------------------------------------------------------- |
| Rule 1 | If two objects are equal using `equals()`, they MUST have the same hashCode. |
| Rule 2 | If two objects have the same hashCode, they are NOT necessarily equal.       |
| Rule 3 | If an object's fields used in hashCode change, its hashCode may also change. |

Very important interview question:

What happens if we override `equals()` but don't override `hashCode()`?

Answer: Two logically equal objects may have different hash codes because the inherited `Object.hashCode()` does not use our custom equality fields. Consequently, HashSet or HashMap may fail to recognize them as duplicates or matching keys.

## 7. Frequently asked interview questions

Q1. Can two different objects have the same hashCode?

Yes. This is called a hash collision.

Q2. Can two equal objects have different hashCodes?

No. If `equals()` returns true, both objects must have the same hashCode.

Q3. Can we override hashCode() without overriding equals()?

Yes, technically. But it is generally not recommended because it can violate the expected equality contract.

Q4. Where are equals() and hashCode() defined?

Both methods are defined in Java's `Object` class.

Q5. Which collections use equals() and hashCode()?

- HashMap
- HashSet
- Hashtable
- LinkedHashMap
- LinkedHashSet

## 8. Quick revision – Remember this for interviews

# hashCode() + equals()

- `hashCode()` → Identifies the bucket where an object should be stored.
- `equals()` → Checks whether two objects are logically equal.
- Same equals result (`true`) → Same hashCode is mandatory.
- Same hashCode → Does not guarantee equality.
- Always override both methods together when defining custom logical equality.
