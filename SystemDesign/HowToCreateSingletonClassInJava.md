## Singleton class

A Singleton class is a design pattern that restricts the instantiation of a class to one single instance. 

## Steps to Create a Singleton Class 

1. **Private Constructor**: Make the constructor of the class private so that no other class can directly instantiate it.
2. **Static Variable`**: Create a static variable which would store the single instance of the class.
3. **Public Static Method**: Create a public static method which would return the instance of the class. This method will create the instance if it does not already exist.

## Example of Singleton Class

```java
public class Singleton {
    

    // Step 1: Private constructor to prevent instantiation
    private Singleton() {
        // Initialization code here
    }
	
	// Step 2: Create a private static variable to hold the single instance
    private static Singleton instance;

    // Step 3: Public static method to provide access to the instance
    public static synchronized Singleton getInstance() {
        if (instance == null) { // Check if instance is null
            instance = new Singleton(); // Create instance if it doesn't exist
        }
        return instance; // Return the single instance
    }

    public void showMessage() {
        System.out.println("Hello from Singleton!");
    }
}
```

### Using the Singleton Class


```java
public class Main {
    public static void main(String[] args) {
        // Get the only object available
        Singleton singleton = Singleton.getInstance();
        
        // Show message
        singleton.showMessage();
    }
}
```

