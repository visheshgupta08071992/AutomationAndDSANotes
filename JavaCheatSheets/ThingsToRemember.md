# Useful Things to remember while Coding


##  Different ways of getting a corresponding numeric value of a character in Java

In Java, there are several ways to obtain the corresponding numeric value of a character:

1. **Character.getNumericValue(char ch)**:
   You can use the `Character.getNumericValue(char ch)` method to get the numeric value of a character. This method returns the numeric value of the character if it represents a digit, or -1 if it's not a digit.

   ```java
   char charDigit = '5';
   int numericValue = Character.getNumericValue(charDigit);
   System.out.println(numericValue); // Output: 5
   ```

2. **Subtracting '0'**:
   You can subtract the character '0' from the character representing a digit to get the corresponding numeric value. This works because the ASCII values of the characters '0' to '9' are consecutive, and subtracting '0' effectively converts the character to its integer value.

   ```js
   char charDigit = '5';
   int numericValue = charDigit - '0';
   System.out.println(numericValue); // Output: 5
   ```

3. **Parsing as an Integer**:
   You can also parse the character as an integer using the `Integer.parseInt()` method. This method will treat the character as a string containing a digit and convert it to an integer.

   ```js
   char charDigit = '5';
   int numericValue = Integer.parseInt(String.valueOf(charDigit));
   System.out.println(numericValue); // Output: 5
   ```

All of these methods will give you the corresponding numeric integer value for a character that represents a digit, such as '5'.

  **Note**

  Directly converting a Character into Integer using Integer.value(character) results in ASCII value of character

   ```js
   char c='4';
   System.out.println(Integer.valueOf('0')); //48
   System.out.println(Integer.valueOf(c));  //52
   ```


## How to Sort two Dimensional Array

Certainly! Sorting a two-dimensional array in Java involves specifying the criteria by which you want to sort the elements (e.g., by the values in a specific column) and then using a sorting algorithm like `Arrays.sort()` or `Collections.sort()` for 2D arrays of objects.

Here's an example of how to sort a two-dimensional array of integers in Java:

```java
import java.util.Arrays;

public class TwoDArraySorting {
    public static void main(String[] args) {
        int[][] twoDArray = {
            {5, 2, 9},
            {8, 3, 1},
            {4, 7, 6}
        };
        
        // Before sorting
        System.out.println("Before sorting:");
        printArray(twoDArray);

        // Sort the 2D array by the first column (ascending order)
        Arrays.sort(twoDArray, (a, b) -> Integer.compare(a[0], b[0]));
               // or

        Arrays.sort(twoDArray, (a, b) -> {
            return a[0] - b[0]
        }); 
        // After sorting
        System.out.println("\nAfter sorting by the first column (ascending order):");
        printArray(twoDArray);
    }

    // Helper method to print the 2D array
    public static void printArray(int[][] arr) {
        for (int[] row : arr) {
            for (int num : row) {
                System.out.print(num + " ");
            }
            System.out.println();
        }
    }
}
```

In this example, we have a 2D array `twoDArray`, and we want to sort it by the values in the first column in ascending order. We use `Arrays.sort()` and provide a custom comparator to specify the sorting criteria.

Here's the output:

```
Before sorting:
5 2 9 
8 3 1 
4 7 6 

After sorting by the first column (ascending order):
4 7 6 
5 2 9 
8 3 1 
```

You can modify the comparator to sort by different columns or in descending order by changing the comparison logic inside the lambda expression. The same approach can be used for two-dimensional arrays of other data types or custom objects; you just need to adjust the comparator accordingly.

## Commonly Used Regex

Here are the commonly used regex patterns in Java along with examples of replacing characters in strings:

- **`\s`** - Matches any whitespace character. Eg: space, tab, newline.
  ```java
  String str = "Hello world!";
  str = str.replaceAll("\\s", "");
  // str is now "Helloworld!"
  ```

- **`\S`** - Matches any non-whitespace character.
  ```java
  String str = "Hello   world!";
  str = str.replaceAll("\\S", "");
  // str is now "      "
  ```

- **`\w`** - Matches any word character (letter, number or underscore).
  ```java
  String str = "Hello123_world!";
  str = str.replaceAll("\\w", "x");
  // str is now "xxxxxxxxx!"
  ```

- **`\W`** - Matches any non-word character.
  ```java
  String str = "Hello123_world!";
  str = str.replaceAll("\\W", "");
  // str is now "Hello123_world"
  ```

- **`\d`** - Matches any digit (number from 0-9).
  ```java
  String str = "Hello123world!";
  str = str.replaceAll("\\d", "0");
  // str is now "Hello000world!"
  ```

- **`\D`** - Matches any non-digit character.
  ```java
  String str = "Hello123world!";
  str = str.replaceAll("\\D", "");
  // str is now "123"
  ```

- **`[^a-zA-Z0-9]`** - Matches any character that is not a letter or number.
  ```java
  String str = "Hello world!";
  str = str.replaceAll("[^a-zA-Z0-9]", "");
  // str is now "Helloworld"
  ```

