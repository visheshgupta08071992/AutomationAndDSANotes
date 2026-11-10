# Access Modifiers in Java

Access modifiers in Java are keywords that define where a class, method, constructor, or variable can be accessed from.

Java has four levels of access control:

1. `private`
2. `default` (also called package-private)
3. `protected`
4. `public`


This is the most important table to remember for interviews.

<img width="604" height="172" alt="image" src="https://github.com/user-attachments/assets/1fd49c28-1668-433f-8c50-57601d597885" />



Easy way to remember:

- `private` → Same class only.
- `default` → Same package only.
- `protected` → Same package + subclasses outside the package.
- `public` → Everywhere.

## 3. Important interview concepts

### Q1. Can we declare a class as private or protected?

It depends on whether it is a top-level class or nested class.

Top-level class:

Only two access levels are allowed:

```
public class Employee {
}

// Valid
class Department {
}

// Invalid
// private class Employee {}

// Invalid
// protected class Employee {}
```

Nested class:

All four access modifiers are allowed.

```
class Outer {

    private class A {}
    protected class B {}
    public class C {}
    class D {}
}
```

### Q2. Can a constructor have an access modifier?

Yes! Constructors support all four access modifiers.

```
class Employee {

    private Employee() {
        System.out.println("Private constructor");
    }
}
```

A private constructor prevents other classes from directly creating objects using `new Employee()`.

This is commonly used in the Singleton design pattern and utility classes.

### Q3. Can we override a method with a more restrictive access modifier?

No. Java does not allow reducing the visibility of an overridden method.

Example:

```
class Parent {

    public void display() {
        System.out.println("Parent");
    }
}

class Child extends Parent {

    // Compilation error
    // protected void display() {}

    // Valid
    public void display() {
        System.out.println("Child");
    }
}
```

You can maintain or increase visibility, but cannot reduce it.

For example:

| Parent method | Child override | Valid? |
| ------------- | -------------- | ------ |
| protected     | protected      | Yes    |
| protected     | public         | Yes    |
| public        | protected      | No     |
| public        | private        | No     |
| default       | protected      | Yes    |
| default       | public         | Yes    |

### Q4. Can local variables have access modifiers?

No.

```
public class Employee {

    public void display() {

        // Invalid
        // private int salary = 50000;

        int salary = 50000; // Valid
    }
}
```

Access modifiers apply to class members, constructors, and nested types, but not local variables or method parameters.

