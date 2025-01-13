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
- `@BeforeTest`: Method annotated with BeforeTest would be executed before all the Tests belonging to classes defined in the <test> tag of the xml file.
- `@AfterTest`: Method annotated with AfterTest would be executed after all the Tests belonging to classes defined in the <test> tag of the xml file.
- `@BeforeClass`: Method annotated with BeforeClass would be executed before all the test methods of current invoked class.
- `@AfterClass`: Method annotated with AfterClass would be executed after all the test methods of current invoked class
- `@BeforeMethod`: Executes before each test method.
- `@AfterMethod`: Executes after each test method.

---

