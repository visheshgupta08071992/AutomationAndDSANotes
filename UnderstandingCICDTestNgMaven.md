# Understanding Continuous Integration, Continuous Deployment, TestNG and Maven

## Continuous Integration
Continuous Integration (CI) is a practice of continuously integrating code from multiple developers into a shared centralized repository. With CI, every code check-in or pull request is verified by an automated build process, which includes running Sonar Code Analysis,unit and integration tests. 

- **If the tests pass**, the build succeeds.
- **If the tests fail**, the build fails, providing continuous feedback to developers on their code changes.

### Example in Our Company
In our company, whenever a developer pushes their changes to our centralized repository (Azure), an automated build is triggered. This process includes:
- Running **unit tests**
- Running **integration tests**
- Performing **Sonar checks**

If all these checks pass, the build is marked as successful.

---

## Continuous Deployment
Continuous Deployment (CD) is a practice of continuously deploying any code change that passes the CI process to higher environments and ultimately to the production environment.

### Current Workflow in Our Company
In our company, we do not have a fully automated continuous deployment process. Instead, we follow these steps:

1. **Code Push or Pull Request Raised**  
   - When a developer pushes code or raises a pull request, a CI setup is triggered.  
   - This automated build process includes:
     - Running **unit tests**
     - Running **integration tests**
     - Performing **Sonar checks**
   - If all checks pass, the build is successful.

2. **Pull Request Review**  
   - Once the build is successful, the pull request undergoes a **PR review process**.  
   - After approval, the changes are merged into the `master` branch.

3. **Deployment to Dev Environment**  
   - Once changes are merged into the `master` branch, an **automated pipeline** is triggered to deploy the code to the **Dev environment**.  
   - After deployment, an **Automated Regression Pipeline** is triggered. This is configured to automatically run whenever the **release pipeline for DEV** is completed.

4. **Manual Testing and Higher Environment Deployment**  
   - After manual feature testing in the Dev environment, the code is **manually deployed** to higher environments such as **UAT** or **Prod**.  
   - On UAT, a **Sanity Regression Pipeline** is auto-triggered once the build is deployed. This is achieved by configuring a trigger to run the regression pipeline whenever the **release pipeline for UAT** is completed.

---

## TestNG

The `testng.xml` file is configuration file used for managing and customizing the execution of our TestNG tests.

### TestNG Execution Hierarchy
- **Suite** → **Test** → **Class** → **Method**

### Hierarchical Components
#### Suite
A **suite** is defined by the `<suite>` tag and can contain one or more tests. Each suite has its own XML configuration file, such as `RegressionSuite.xml`, `SanitySuite.xml`, or `QuickTestSuite.xml`.

#### Test
A **test** is defined by the `<test>` tag and can contain one or more classes.

#### Class
A **class** represents a Java class containing TestNG annotations. It is defined using the `<class>` tag and can include one or more test methods.

#### Method
A **test method** is a method annotated with `@Test` within a class.

---

## Sample `testng.xml` Files

### 1. Include Specific Test Methods from a Class

![image](https://github.com/user-attachments/assets/71a02772-f76f-456a-8cf6-ac1f756389d9)



```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE suite SYSTEM "http://testng.org/testng-1.0.dtd">
<suite name="All Test Suite">
    <listeners>
        <listener class-name="com.listners.TestListner"/>
    </listeners>
    <test parallel="methods" thread-count="1" name="C:/VisheshProjects/APIAutomationFramework">
        <classes>
            <class name="com.tests.GetTests">
                <methods>
                    <include name="verifyAllEmployeeDetails"/>
                    <include name="verifySpecificEmployeeDetails"/>
                </methods>
            </class>
            <class name="com.tests.PostTests">
                <methods>
                    <include name="verifyEmployeeRecordIsAdded"/>
                    <include name="verifyEmployeeRecordIsAddedUsingExternalFile"/>
                </methods>
            </class>
        </classes>
    </test>
</suite>
```



### 2. Include All Classes in a Test

![image](https://github.com/user-attachments/assets/adf23ac9-24c3-4940-ac35-e03bde83b50d)


```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE suite SYSTEM "http://testng.org/testng-1.0.dtd">
<suite name="Suite">
    <listeners>
        <listener class-name="com.automation.listeners.Listeners"/>
    </listeners>
    <test thread-count="5" name="Test">
        <classes>
            <class name="com.automation.practice.jsonserver.GetRequestTest"/>
            <!-- Uncomment to include other classes -->
            <!-- <class name="com.automation.tests.GetJobDetailsTest"/> -->
        </classes>
    </test>
</suite>
```

### 3. Run a Complete Package


![image](https://github.com/user-attachments/assets/a9178e8e-e379-42db-ac1e-376270b5eb32)



```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE suite SYSTEM "https://testng.org/testng-1.0.dtd">
<suite name="Automation Test Suite for Spotify Playlist APIs" data-provider-thread-count="3">
    <listeners>
        <listener class-name="com.spotify.oauth2.listeners.AnnotationTransformer"/>
    </listeners>
    <test name="Regression Tests execution for Spotify Playlist APIs" thread-count="10" parallel="methods">
        <packages>
            <package name="com.spotify.oauth2.tests"/>
        </packages>
    </test>
</suite>
```

### 4. Grouping Tests
```xml
<!DOCTYPE suite SYSTEM "http://testng.org/testng-1.0.dtd">
<suite name="GoRestSuite" parallel="methods" thread-count="1">
    <listeners>
        <listener class-name="com.framework.core.report.TestNGListener"/>
    </listeners>
    <parameter name="envName" value="qa"/>
    <test name="UsersRegressionTest">
        <groups>
            <run>
                <include name="regression"/>
            </run>
        </groups>
        <classes>
            <class name="com.gorest.tests.UsersWithRestClientTest"/>
        </classes>
    </test>
</suite>
```

---

## TestNG Execution Flow

1. **Pre-execution Setup:**
    - `@BeforeSuite` → `@BeforeTest` → `@BeforeClass` → `@BeforeMethod`
2. **Execution:**
    - Execute `@Test` methods (in priority order, if defined).
3. **Post-execution Cleanup:**
    - `@AfterMethod` → `@AfterClass` → `@AfterTest` → `@AfterSuite`

---

## TestNG Annotations

### Common Annotations:
- `@Test`: Marks a method as a test method.
- `@BeforeSuite`: Method annotated with BeforeSuite would be executed before all the Tests within the suite.
- `@AfterSuite`: Method annotated with AfterSuite would be executed after all the Tests within the suite.
- `@BeforeTest`: Method annotated with BeforeTest would be executed before all the Tests belonging to classes defined under **Test** tag of the xml file.
- `@AfterTest`: Method annotated with AfterTest would be executed after all the Tests belonging to classes defined under **Test**  tag of the xml file.
- `@BeforeClass`: Method annotated with BeforeClass would be executed before all the test methods of current invoked class.
- `@AfterClass`: Method annotated with AfterClass would be executed after all the test methods of current invoked class
- `@BeforeMethod`: Executes before each test method.
- `@AfterMethod`: Executes after each test method.
- `@Parameters`:</br>
   The @Parameters tag in TestNG allows us to pass values from the test configuration file (testng.xml) into oour test methods. Generally browser name,Environment name, User credentials which are required during execution are passed as parameters.

 ```xml
    <!DOCTYPE suite SYSTEM "https://testng.org/testng-1.0.dtd">
<suite name="Parameter Suite">
    <test name="Test with Parameters">
        <parameter name="env" value="qa" />
        <parameter name="browser" value="chrome" />   
        <parameter name="username" value="testuser" />
        <parameter name="password" value="testpass" />
        <classes>
            <class name="com.example.ParameterizedTest" />
        </classes>
    </test>
</suite>
  
```

```java

package com.example;

import org.testng.annotations.Parameters;
import org.testng.annotations.Test;

public class ParameterizedTest {

   @BeforeMethod
   @Parameters({"env","browser" })
   public void setUp(String env, String browser)
   {
      // Setup logic using parameters
   }

    @Test
    @Parameters({"username", "password"})
    public void testLogin(String username, String password) {
        System.out.println("Username: " + username);
        System.out.println("Password: " + password);
        // Add login logic or assertions here
    }
}


```

We can also provide parameter values dynamically using command line. In TestNG, when we provide parameters both in the testng.xml file and dynamically via the command line using the -D option, the command line parameters will take precedence over those defined in the testng.xml file.So the easiest way of changing the values of parameters at runtime is to pass them via the JVM argument (https://rationaleemotions.wordpress.com/2017/09/29/dynamic-parameterization-in-testng/).




**Running our TestNg Test with Maven when there is no Surefire Plugin**

```bash

mvn test -DsuiteXmlFile=testng.xml -Denv=uat -Dbrowser=firefox -Dusername=dynamicUser -Dpassword=dynamicPass

```

**Running our TestNg Test with Maven when there is Surefire Plugin**

```bash

mvn test -Denv=uat -Dbrowser=firefox -Dusername=dynamicUser -Dpassword=dynamicPass

```

**Configuration of VM arguments if running through IDE**

![image](https://github.com/user-attachments/assets/6a8de11d-4306-4a41-8885-56225d3f7ec4)


- `@groups`: https://toolsqa.com/testng/groups-in-testng/ </br>  
  groups in TestNg is used for grouping different tests together into a straightforward group and running these tests together by just running the group in a single command. We can group our tests based on smoke and sanity tests.

```java

import org.testng.annotations.Test;

public class GroupingExample {

    @Test(groups = {"Smoke"})
    public void testLogin() {
        System.out.println("Executing Smoke Test: Login");
        // Smoke test logic for login
    }

    @Test(groups = {"Smoke", "Regression"})
    public void testDashboard() {
        System.out.println("Executing Smoke and Regression Test: Dashboard");
        // Test logic for dashboard
    }

    @Test(groups = {"Regression"})
    public void testProfileUpdate() {
        System.out.println("Executing Regression Test: Profile Update");
        // Regression test logic for profile update
    }

    @Test(groups = {"Regression"})
    public void testLogout() {
        System.out.println("Executing Regression Test: Logout");
        // Regression test logic for logout
    }
}
```

**Smoke.xml**

```xml

<!DOCTYPE suite SYSTEM "https://testng.org/testng-1.0.dtd">
<suite name="Test Suite with Groups">
    <!-- Run only Smoke tests -->
    <test name="Smoke Tests">
        <groups>
            <run>
                <include name="Smoke" />
            </run>
        </groups>
        <classes>
            <class name="com.example.GroupingExample" />
        </classes>
    </test>

```

**Regression.xml**

```xml

<!DOCTYPE suite SYSTEM "https://testng.org/testng-1.0.dtd">
<suite name="Test Suite with Groups">

    <!-- Run only Regression tests -->
    <test name="Regression Tests">
        <groups>
            <run>
                <include name="Regression" />
            </run>
        </groups>
        <classes>
            <class name="com.example.GroupingExample" />
        </classes>
    </test>
</suite>

```

- `priority` - priority attribute is used to define the sequence of test methods, works in alphabetical order or smallest number(https://toolsqa.com/testng/testng-test-priority/)

 ```java

   @Test (priority = 1)
	public void CloseBrowser() {
		driver.close();
		System.out.println("Closing Google Chrome browser");
	}

	@Test (priority = 0)
	public void OpenBrowser() {
		driver.get("https://www.demoqa.com");
		System.out.println("Launching Google Chrome browser"); 
	}

	@Test (priority = 1)
	public void AccountTest(){
		System.out.println("Some tests for Customer Account");
	}

  ```

- `dependsOnMethods` - dependsOnMethods attribute is used to specify that a test method should run only after certain other methods have been executed successfully.

  ```java

  @Test(dependsOnMethods = {"method1", "method2"})
  public void dependentMethod() {
    // Test logic here
  }
  ```

- `invocationCount` - specifies the number of times a test method should be invoked
- `threadPoolSize` - controls how many threads TestNG will use to execute the invocations of a test method Ex: @Test(threadPoolSize = 3, invocationCount = 6) public void testMethod() { // Test logic }

  
---

---

## ✅ What is **Maven**?

**Maven** is a **build automation tool** used primarily for **Java** projects. It helps manage:

- **Project dependencies** (external libraries)
- **Build lifecycle** (compile, test, package, deploy)
- **Project structure** and configuration via `pom.xml`
- **Plugins** and reusable tasks

Think of Maven as a smart assistant that builds, tests, and packages your code into a JAR or WAR file, and can even deploy it for you.

---

## 🏗️ Maven Build Lifecycle (Phases)

Maven has a **default build lifecycle** with several **phases**. Each phase represents a stage in the build process. Running a phase will automatically run all previous phases in order.

Here are the most common Maven phases:

| Phase         | Description |
|---------------|-------------|
| `validate`    | Validates the project structure and necessary info |
| `compile`     | Compiles the source code |
| `test`        | Runs unit tests using a framework like JUnit/TestNG |
| `package`     | Packages the code into a JAR/WAR |
| `verify`      | Runs checks on the results of integration tests |
| `install`     | Installs the package into the local repository (`~/.m2`) |
| `deploy`      | Copies the package to a remote repository (for sharing with others) |

---

## 📦 Maven Project Structure

```
my-app/
├── src/
│   ├── main/
│   │   └── java/             # Application source code
│   └── test/
│       └── java/             # Test source code
├── target/                   # Compiled classes and packaged artifacts
└── pom.xml                   # Maven configuration file
```


## 🛠️ Running Maven Commands

You can run different phases like this:

```bash
mvn validate       # Check project structure
mvn compile        # Compile Java files
mvn test           # Run unit tests
mvn package        # Create JAR file in `target/`
mvn install        # Store the JAR in your local Maven repo
```

Running `mvn package` will run all prior phases (`validate`, `compile`, `test`, etc.).

---

## 🔁 Bonus: Maven Lifecycle in Real Use

If you run:

```bash
mvn install
```

Maven will:
1. Validate your `pom.xml`
2. Compile your code
3. Run tests
4. Package it (JAR/WAR)
5. Install the package locally

---

## Understanding Maven Compiler and Surefire Plugin


## 🔧 1. Maven Compiler Plugin

The **Maven Compiler Plugin** is used to **compile your Java source code**.

### 📌 Why it's needed:

By default, Maven uses **Java 1.5** to compile your project, unless you explicitly set the version.

---

### ✅ How to configure:

In your `pom.xml`, add:

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-compiler-plugin</artifactId>
            <version>3.11.0</version> <!-- or latest -->
            <configuration>
                <source>17</source>     <!-- Java source version -->
                <target>17</target>     <!-- Java bytecode version -->
            </configuration>
        </plugin>
    </plugins>
</build>
```

You can change `17` to your Java version (e.g., `11`, `21`, etc.).

---

### ✅ Example:

Let's say you use Java 17 features. Without this plugin, Maven might throw errors saying syntax is invalid. With it configured, Maven knows how to compile using the proper version.

---

## ✅ 2. Maven Surefire Plugin

The **Maven Surefire Plugin** is used to **run unit tests** (those in `src/test/java`). It supports frameworks like **JUnit**, **TestNG**, etc.

---

### 📌 Why it's needed:

When you run `mvn test`, Surefire kicks in to find and run your test classes.

---

### ✅ How to configure:

```xml
<build>
    <plugins>
        <!-- Compiler plugin here if needed -->

        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-surefire-plugin</artifactId>
            <version>3.2.5</version> <!-- or latest -->
            <configuration>
                <includes>
                    <include>**/*Test.java</include>
                    <include>**/*Tests.java</include>
                </includes>
            </configuration>
        </plugin>
    </plugins>
</build>
```

> By default, it runs files that match: `**/Test*.java`, `**/*Test.java`, or `**/*TestCase.java`.

---

### ✅ Example test:

```java
package com.example;

import org.junit.Test;
import static org.junit.Assert.*;

public class AppTest {
    @Test
    public void testSum() {
        assertEquals(5, 2 + 3);
    }
}
```

Running:

```bash
mvn test
```

Will trigger Surefire, find `AppTest.java`, run it, and report results.

---

## ✅ Combined Example `pom.xml`

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.example</groupId>
    <artifactId>maven-demo</artifactId>
    <version>1.0-SNAPSHOT</version>

    <dependencies>
        <!-- JUnit dependency -->
        <dependency>
            <groupId>junit</groupId>
            <artifactId>junit</artifactId>
            <version>4.13.2</version>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <!-- Compiler plugin -->
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.11.0</version>
                <configuration>
                    <source>17</source>
                    <target>17</target>
                </configuration>
            </plugin>

            <!-- Surefire plugin -->
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-surefire-plugin</artifactId>
                <version>3.2.5</version>
            </plugin>
        </plugins>
    </build>
</project>
```

---

### 🧪 Running

```bash
mvn compile         # Uses maven-compiler-plugin
mvn test            # Uses maven-surefire-plugin
mvn package         # Runs all and creates .jar/.war
```

---


