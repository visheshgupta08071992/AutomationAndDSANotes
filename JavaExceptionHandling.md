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

