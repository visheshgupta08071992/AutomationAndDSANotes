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

