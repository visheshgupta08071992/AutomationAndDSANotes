In Java, both **abstract classes** and **interfaces** are used to achieve abstraction. However, they are designed for different purposes and have distinct characteristics. Below is a detailed comparison along with examples.

---



### **Differences Between Abstract Class and Interface**

| **Abstract Class**                                                                                 | **Interface**                                                                                   |
|----------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| A class that can have abstract methods (methods without a body) and non-abstract methods (methods with a body). | Interface can have only abstract methods. Since Java 8, it can have default and static methods also. |
| Used when you want to define a base class that can have partial implementation.                    | Used to define a contract that a class must follow (complete abstraction).                     |
| Defined using the `abstract` keyword.                                                             | Defined using the `interface` keyword.                                                        |
| A class can inherit only one abstract class.                                                      | A class can implement multiple interfaces.                                                    |
| Can have instance variables (state) with any access modifier.                                      | Can only have `public static final` (constant) fields.                                         |
| Can have abstract, non-abstract (concrete), static, or final methods.                              | Can have abstract methods (default in Java 7) and default/static methods (from Java 8 onward). |
| Can have constructors.                                                                             | Cannot have constructors.                                                                     |
| Abstract methods can be `protected` or `public`.                                                  | All methods are `public` by default.                                                          |
| Suitable when classes share behavior or state.                                                    | Suitable when unrelated classes share a contract or behavior.                                 |
