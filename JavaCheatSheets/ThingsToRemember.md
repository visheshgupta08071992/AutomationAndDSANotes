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
