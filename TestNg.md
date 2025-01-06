Let's jump right in understanding all important annotations & configurations of TestNG

1) @Test: Marks a method as a test method
2) @BeforeSuite: Marks a method to run before any test suite
3) @AfterSuite: Marks a method to run after all tests in a suite have run
4) BeforeTest: Marks a method to run before any test method belonging to the classes inside the <test> tag in XML
5) @AfterTest: Marks a method to run after all test methods belonging to the classes inside the <test> tag in XML
6) @BeforeClass: Marks a method to run before the first test method in the current class is invoked
7) @AfterClass: Marks a method to run after all the test methods in the current class have been run
8) @BeforeMethod: Marks a method to run before each test method
9) @AfterMethod: Marks a method to run after each test method
10) @DataProvider: Marks a method as a data provider supplying data for test methods
Ex:
 @DataProvider(name = "testData")
 public Object[][] testData() {
 return new Object[][] {
 { "data1" },
 { "data2" }
 };
11) @Parameters: Marks a method or a class as a parameter provider for test methods
Ex: 
 @Parameters({ "browser", "platform" })
 @BeforeMethod
 public void setUp(String browser, String platform) {
 // Setup logic using parameters
 }
12) @Listeners: Marks a listener class to listen to events during test execution, Mostly used for WebDriverEvent Listeners, TestNG Listeners
13) @Factory: Marks a method to generate instances of test class dynamically
14) TestNG XML for Parameters:

<suite name="ParameterizedSuite"> <test name="ParameterizedTest"> <parameter name="browser" value="chrome"/> <classes>
<class name="TestNGExample"/> </classes> </test> </suite>

15) Parallel Test Execution:

<suite name="ParallelSuite" parallel="tests" thread-count="2">
 <test name="Test1"> <classes> <class name="TestClass1"/> </classes> </test> 
<test name="Test2"> <classes> <class name="TestClass2"/> </classes> </test> </suite>

16) invocationCount specifies the number of times a test method should be invoked
17) threadPoolSize controls how many threads TestNG will use to execute the invocations of a test method
Ex: @Test(threadPoolSize = 3, invocationCount = 6)
 public void testMethod() {
 // Test logic
 }
18) Dependency Testing: Define dependencies between test methods
Ex: 
 @Test(dependsOnMethods = "firstMethod")
 public void secondMethod() {
 // Test logic
 }
19) Grouping: Group tests to execute specific sets of tests
Ex:
 @Test(groups = "smoke")
 public void smokeTest() {
 // Smoke test logic
 }
20) Test Priority: Set priority for test methods, works in alphabetical order or smallest number.



##CICD

Continuous Integration is the practise of Automatically integrating code from multiple developers into shared repository several times a day.

As part of Continuous integration every code commit or pull request is verifyied by Automated build which inludes running of your unit and integration tests, If the unit and intergation tests passes then the build passes else if the unit and integration tests fails then the build fails, Thus continuous integration gives continuous feedback to developers.

Continuous Deployment is the practice of automatically deploying every code change that passes the CI process to a production environment. In our project Regression Test pipeline is triggered when the build is deployed on QA environment and Sanity TestPipeline is triggered when the build is deployed on UAT environment.
