# JavaExceptionHandling

Exception is abnormal condition that distrupts the normal execution of Program. Order of catch block should be from most relevant to most generic. try-with-resources is a special  try block which is used to autoclose resources used within try block without using finally block.

```java
try (BufferedReader reader = new BufferedReader(new FileReader("data.txt"))) {
    String line = reader.readLine();
    System.out.println(line);
} catch (IOException e) {
    e.printStackTrace();
}

```

```java
try (
    FileInputStream fis = new FileInputStream("input.txt");
    FileOutputStream fos = new FileOutputStream("output.txt")
) {
    // use fis and fos
}


```


![image](https://user-images.githubusercontent.com/52998083/206474520-5ce1e745-ce1f-4b02-9fcc-3b25e5519d8d.png)



<img width="646" height="257" alt="image" src="https://github.com/user-attachments/assets/78ef5125-d0df-47dc-b78c-4ef3d0c061a5" />

<img width="582" height="273" alt="image" src="https://github.com/user-attachments/assets/1bd18ece-2cfa-429e-bd43-25e6d3ffce89" />


# How to Create Custom Exceptions in Java

A Custom Exception is a user-defined exception that we create to handle application-specific error scenarios that standard Java exceptions may not clearly represent.

For example:

- Invalid employee ID.
- Insufficient bank balance.
- Invalid age during registration.
- Invalid test execution status.
- API response validation failure.

Java allows us to create two types of custom exceptions:

1. Custom Checked Exception – Extends `Exception`.
2. Custom Unchecked Exception – Extends `RuntimeException`.

Let's understand both with practical examples.

## 1. Custom Checked Exception

To create a checked exception, extend the `Exception` class.

### Scenario: Bank account age validation

Suppose a banking application requires customers to be at least 18 years old.

If the age is below 18, we want to throw our own exception called `InvalidAgeException`.

Step 1: Create a custom exception class

```
class InvalidAgeException extends Exception {

    public InvalidAgeException(String message) {
        super(message);
    }
}
```

Explanation:

- `InvalidAgeException` is our custom exception.
- It extends Java's `Exception` class.
- The constructor accepts an error message.
- `super(message)` passes that message to the parent `Exception` class.

Step 2: Throw the custom exception

```
class BankAccount {

    public static void validateAge(int age)
            throws InvalidAgeException {

        if (age < 18) {
            throw new InvalidAgeException(
                "Customer age must be 18 or above"
            );
        }

        System.out.println("Age validation successful");
    }
}
```

Explanation:

- `throws InvalidAgeException` declares that the method may throw this checked exception.
- `throw new InvalidAgeException()` actually creates and throws the exception.

Step 3: Handle the exception

```
public class Main {

    public static void main(String[] args) {

        try {

            BankAccount.validateAge(15);

        } catch (InvalidAgeException e) {

            System.out.println(
                "Exception occurred: " + e.getMessage()
            );
        }
    }
}
```

Output:

```
Exception occurred: Customer age must be 18 or above
```


## 2. Custom Unchecked Exception

To create an unchecked exception, extend the `RuntimeException` class.

Let's use the same banking example.

Step 1: Create a custom exception class

```
class InsufficientBalanceException extends RuntimeException {

    public InsufficientBalanceException(String message) {
        super(message);
    }
}
```

Step 2: Throw the custom exception

```
class BankAccount {

    int balance = 5000;

    public void withdraw(int amount) {

        if (amount > balance) {
            throw new InsufficientBalanceException(
                "Insufficient account balance"
            );
        }

        balance = balance - amount;

        System.out.println("Remaining balance: " + balance);
    }
}
```

Step 3: Call the method

```
public class Main {

    public static void main(String[] args) {

        BankAccount account = new BankAccount();

        account.withdraw(7000);
    }
}
```

Output:

```
Exception in thread "main"
InsufficientBalanceException: Insufficient account balance
```

Notice something important:

We did not use `try-catch` or `throws`.

The program compiled successfully because `InsufficientBalanceException` extends `RuntimeException`.

You can still catch an unchecked exception if you want to handle it.

## 3. Checked vs Unchecked custom exceptions

| Feature              | Checked                                   | Unchecked                            |
| -------------------- | ----------------------------------------- | ------------------------------------ |
| Parent class         | `Exception`                               | `RuntimeException`                   |
| Mandatory handling   | Yes                                       | No                                   |
| `try-catch` required | Yes, or declare `throws`                  | No                                   |
| `throws` declaration | Required if not caught                    | Optional                             |
| Typical use          | Expected conditions callers should handle | Programming errors or invalid states |
| Example              | `InvalidAgeException`                     | `InsufficientBalanceException`       |

## 4. Important: Difference between `throw` and `throws`

This is frequently asked in Java interviews.

| `throw`                                | `throws`                               |
| -------------------------------------- | -------------------------------------- |
| Used to explicitly throw an exception  | Used to declare possible exceptions    |
| Used inside method or constructor body | Used in method/constructor declaration |
| Followed by an exception object        | Followed by exception class names      |
| Throws one exception object at a time  | Can declare multiple exception types   |

Example:

```
public void validateAge(int age)
        throws InvalidAgeException {

    if (age < 18) {
        throw new InvalidAgeException("Invalid age");
    }
}
```

Here:

- `throws InvalidAgeException` → Declares the exception.
- `throw new InvalidAgeException()` → Actually throws the exception.

## 5. How to decide which custom exception to create?

A simple guideline:

Your application encounters an exceptional condition.

Should the caller be forced to handle or acknowledge it?

Create a checked exception by extending `Exception`.

Is it an invalid argument, programming error, or invalid application state?

Consider an unchecked exception by extending `RuntimeException`.

## 6. Interview questions to remember

1. Can we create custom checked exceptions? Yes, by extending `Exception`.
2. Can we create custom unchecked exceptions? Yes, by extending `RuntimeException`.
3. Can we throw an unchecked exception without declaring it using `throws`? Yes.
4. Can we catch unchecked exceptions? Yes.
5. Can a custom exception have multiple constructors? Yes.
6. Why do we use `super(message)`? To pass the exception message to the parent class.
7. Can we use `throw` and `throws` together? Yes.

One practical SDET example: You could create a custom `APIResponseValidationException` extending `RuntimeException` when an API response doesn't meet an expected business condition. This makes failures in your automation framework more meaningful and easier to debug.

Suggested next step: Practice writing three custom exceptions yourself: `InvalidTestDataException`, `APIResponseValidationException`, and `DatabaseConnectionException`. This will help reinforce both checked and unchecked exception handling.

I can also give you a short Java exception coding exercise tomorrow to test your understanding.

☕Daily Java exception practiceTap to set up

