In Java, the `Set` interface is a part of the Java Collections Framework and represents a collection that cannot contain duplicate elements. Here are some common methods provided by the `Set` interface, along with examples:

### 1. **`add(E e)`**
   Adds the specified element to the set if it is not already present.

   **Example:**
   ```java
   Set<String> set = new HashSet<>();
   set.add("Apple");
   set.add("Banana");
   set.add("Apple"); // Duplicate element, will not be added

   System.out.println(set); // Output: [Apple, Banana]
   ```

### 2. **`remove(Object o)`**
   Removes the specified element from the set if it is present.

   **Example:**
   ```java
   Set<String> set = new HashSet<>();
   set.add("Apple");
   set.add("Banana");
   
   set.remove("Apple"); // Removes "Apple" from the set

   System.out.println(set); // Output: [Banana]
   ```

### 3. **`contains(Object o)`**
   Returns `true` if the set contains the specified element.

   **Example:**
   ```java
   Set<String> set = new HashSet<>();
   set.add("Apple");
   set.add("Banana");

   boolean hasApple = set.contains("Apple"); // true
   boolean hasGrape = set.contains("Grape"); // false

   System.out.println("Contains Apple? " + hasApple); // Output: Contains Apple? true
   System.out.println("Contains Grape? " + hasGrape); // Output: Contains Grape? false
   ```

### 4. **`size()`**
   Returns the number of elements in the set.

   **Example:**
   ```java
   Set<String> set = new HashSet<>();
   set.add("Apple");
   set.add("Banana");

   int size = set.size();

   System.out.println("Set size: " + size); // Output: Set size: 2
   ```

### 5. **`isEmpty()`**
   Returns `true` if the set contains no elements.

   **Example:**
   ```java
   Set<String> set = new HashSet<>();

   boolean empty = set.isEmpty(); // true

   set.add("Apple");
   empty = set.isEmpty(); // false

   System.out.println("Is set empty? " + empty); // Output: Is set empty? false
   ```

### 6. **`clear()`**
   Removes all elements from the set.

   **Example:**
   ```java
   Set<String> set = new HashSet<>();
   set.add("Apple");
   set.add("Banana");

   set.clear(); // All elements removed

   System.out.println(set); // Output: []
   ```

### 7. **`iterator()`**
   Returns an iterator over the elements in the set.

   **Example:**
   ```java
   Set<String> set = new HashSet<>();
   set.add("Apple");
   set.add("Banana");

   Iterator<String> iterator = set.iterator();
   while (iterator.hasNext()) {
       System.out.println(iterator.next());
   }
   // Output: Apple Banana (Order may vary depending on the implementation)
   ```

### 8. **`addAll(Collection<? extends E> c)`**
   Adds all the elements in the specified collection to the set.

   **Example:**
   ```java
   Set<String> set = new HashSet<>();
   set.add("Apple");

   List<String> list = Arrays.asList("Banana", "Grape", "Apple"); // "Apple" is a duplicate

   set.addAll(list);

   System.out.println(set); // Output: [Apple, Banana, Grape]
   ```

### 9. **`retainAll(Collection<?> c)`**
   Retains only the elements in the set that are contained in the specified collection.

   **Example:**
   ```java
   Set<String> set = new HashSet<>();
   set.add("Apple");
   set.add("Banana");
   set.add("Grape");

   List<String> list = Arrays.asList("Banana", "Apple");

   set.retainAll(list);

   System.out.println(set); // Output: [Apple, Banana]
   ```

### 10. **`removeAll(Collection<?> c)`**
    Removes from the set all of its elements that are contained in the specified collection.

    **Example:**
    ```java
    Set<String> set = new HashSet<>();
    set.add("Apple");
    set.add("Banana");
    set.add("Grape");

    List<String> list = Arrays.asList("Banana", "Apple");

    set.removeAll(list);

    System.out.println(set); // Output: [Grape]
    ```
