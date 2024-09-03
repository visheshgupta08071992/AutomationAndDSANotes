A `HashMap` in Java is a widely used data structure that stores key-value pairs. Internally, it uses a hash table to store the map entries, making retrieval operations like `get()` and `put()` very efficient, usually with a time complexity of O(1). Here’s how `HashMap` works internally:

![image](https://github.com/user-attachments/assets/b5d74f03-c9f0-4fc3-928c-4e05e83ca2e8)

![image](https://github.com/user-attachments/assets/7429b7db-d930-4619-93e8-79cc4c5d58f7)



### 1. **Hashing:**
   - When you put a key-value pair in a `HashMap`, the key is first hashed using its `hashCode()` method.
   - This hash code is then converted to an index in the internal array (called a bucket array) where the entry will be stored.

### 2. **Index Calculation:**
   - The index for storing the key-value pair is calculated using the formula:
     \[
     \text{index} = \text{hash} \, \& \, (\text{n-1})
     \]
     where `n` is the size of the internal array (usually a power of 2).

### 3. **Collision Handling:**
   - Since different keys can generate the same hash code, they might end up in the same index (bucket). This is called a collision.
   - To handle collisions, Java uses a linked list or a binary tree (since Java 8) within each bucket. If two keys collide, their entries are stored in the same bucket but as separate nodes in the linked list or binary tree.

### 4. **Resizing:**
   - `HashMap` dynamically resizes when the number of entries exceeds a threshold (called load factor, typically 0.75). The resizing operation doubles the size of the bucket array and rehashes all existing entries to fit into the new bucket array.

### 5. **Retrieval:**
   - To retrieve a value, the key is hashed to find the index in the bucket array.
   - The `HashMap` then traverses the linked list or binary tree in the corresponding bucket to find the entry with the matching key and returns the associated value.

### Example:

Let’s consider an example:

```java
import java.util.HashMap;

public class HashMapExample {
    public static void main(String[] args) {
        // Creating a HashMap
        HashMap<String, Integer> map = new HashMap<>();

        // Adding key-value pairs to the HashMap
        map.put("Apple", 1);
        map.put("Banana", 2);
        map.put("Orange", 3);

        // Retrieving values from the HashMap
        System.out.println("Value for key 'Apple': " + map.get("Apple"));
        System.out.println("Value for key 'Banana': " + map.get("Banana"));
        System.out.println("Value for key 'Orange': " + map.get("Orange"));
    }
}
```

### How the Example Works Internally:

1. **Inserting "Apple":**
   - The key `"Apple"` is hashed to an index.
   - Suppose it hashes to index 2.
   - The key-value pair (`"Apple" -> 1`) is stored in the bucket at index 2.

2. **Inserting "Banana":**
   - The key `"Banana"` is hashed.
   - Suppose it hashes to index 5.
   - The key-value pair (`"Banana" -> 2`) is stored in the bucket at index 5.

3. **Inserting "Orange":**
   - The key `"Orange"` is hashed.
   - Suppose it hashes to index 2 (collision with `"Apple"`).
   - A linked list or tree is created at index 2 to store both `"Apple" -> 1` and `"Orange" -> 3`.

4. **Retrieving "Apple":**
   - The key `"Apple"` is hashed to index 2.
   - The `HashMap` finds `"Apple"` in the list/tree at index 2 and returns `1`.


