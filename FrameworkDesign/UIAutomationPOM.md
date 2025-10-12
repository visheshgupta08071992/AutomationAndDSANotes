## Understanding PageObject Model Framework Structure


**Reference Framework**  - https://github.com/visheshgupta08071992/WeatherReportingComparator

Please ensure to check **FeedbackReceivedOnFramework** file, The file contains the mistakes in the framework.

## Understanding Framework Structure

With regards to UI Automation we have used Page Object Model Framework design pattern which is widely used in industry for Framework design. We have used maven for building our application and managing dependencies, We have used TestNg for Asseertion and managing execution of our Tests. The version control tool was GIT and the remote repository was Github.

Lets look at the structure of the framework:

<img width="838" height="855" alt="image" src="https://github.com/user-attachments/assets/8b88ddba-e818-4179-9dae-3f5151b407c8" />


**Base** - base Folder consist of Base class which is inherited by all the Page Classes and the Test Classes. The main function of Base Class is to load config properties file, Define Webdriver driver,Launch the desired browser based on the parameter provided by test method, Set implicit wait times. We can also define whether we want to run in headless or non headless baded before launching the browser within the base test.

```java

  ChromeOptions co = new ChromeOptions();
  co.setHeadless(prop.getProperty("headless"));
  driver = new ChromeDriver(co);

```



As per feedback received on framework, The base class needs to be improved and test classses should send the browser on which they want to execute their test, So initialization method should have parameter browserName and test methods should call initialization method by passing browserName on which they want to run their test.

```java
package base;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Properties;
import java.util.concurrent.TimeUnit;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.support.ui.WebDriverWait;

import io.github.bonigarcia.wdm.WebDriverManager;
import io.restassured.builder.RequestSpecBuilder;
import io.restassured.builder.ResponseSpecBuilder;
import io.restassured.http.ContentType;
import io.restassured.specification.RequestSpecification;
import io.restassured.specification.ResponseSpecification;
import util.TestConstants;

public class TestBase {

	protected static WebDriver driver;
	protected static Properties prop;
	protected static WebDriverWait wait;
	public static RequestSpecification requestSpec;
	public static ResponseSpecification responseSpec;


	public TestBase(){
		try {
			prop = new Properties();
			FileInputStream ip = new FileInputStream(System.getProperty("user.dir")+ "/src/main/java/config/WeatherReporting.properties");
			prop.load(ip);
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	public static void initialization(){
		String browserName = prop.getProperty("browser");

		if(browserName.equals("chrome")){
			WebDriverManager.chromedriver().setup();
			driver = new ChromeDriver();
		}
		else if(browserName.equals("FF")){
			WebDriverManager.firefoxdriver().setup();
			driver = new FirefoxDriver();
		}
		driver.manage().window().maximize();
		driver.manage().deleteAllCookies();
		driver.manage().timeouts().pageLoadTimeout(TestConstants.PAGE_LOAD_TIMEOUT, TimeUnit.SECONDS);
		driver.manage().timeouts().implicitlyWait(TestConstants.IMPLICIT_WAIT, TimeUnit.SECONDS);

		driver.get(prop.getProperty("url"));
	}

	public static RequestSpecification buildRequestSpec(String City,String APIKey){
		return requestSpec=new RequestSpecBuilder()
				.setBaseUri(prop.getProperty("baseURI"))
				.addQueryParam("q",City)
				.addQueryParam("appid",APIKey)
				.setContentType(ContentType.JSON)
				.build();
	}

	public static ResponseSpecification buildResponseSpec(){
		return responseSpec= new ResponseSpecBuilder()
				.expectStatusCode(TestConstants.STATUS_200)
				.expectContentType(ContentType.JSON)
				.build();
	}
}

```

**config** - config folder contains properties file which contains all configuration details like url,browser,baseUTL,JDBC Connection url. Note as perfeedback received the configuration prperties file shouls be in resource folder as per Industry standards.

```
url=https://www.ndtv.com/weather
browser=chrome
baseURI=http://api.openweathermap.org/data/2.5/weather
headless=true

```

**pages** - page folder consist of all the page classes corresponding to pages within the application. Page classes are used to define WebElements(PageObjects) and perform operations on them. We have achieved encpasulation here by wrapping Private DataVariable(WebElements) and Public Methods performing operations on those Data Variables. Single Responsibility principal is maintained as Pages only defines Page Objects and performs operations on them.Page Linkage: Methods that navigate/submit should return the next Page object (e.g., HomePage login(...)), enabling readable flows.

```java

package pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;

import base.TestBase;

public class WeatherPage extends TestBase {

	@FindBy(xpath="//input[@id='indiceslist-search']")
	private WebElement searchCityTextBox;

	@FindBy(xpath="//li[@class='searched']//td[3][contains(.,'Bengaluru')]/b/text()")
	private WebElement searchedCity;

	@FindBy(xpath="//div[@class='noti_wrap']")
	private WebElement notificationPopup;

	@FindBy(xpath="//div[@class='noti_wrap']//a[@class='notnow']")
	private WebElement notificationPopupNotNowButton;

	public WeatherPage() {
		PageFactory.initElements(driver,this);
	}

	public void searchCity(String city){
		searchCityTextBox.click();
		searchCityTextBox.sendKeys(city);
	}

	public boolean searchedCityIsDisplayed(String city) {
		return driver.findElement(By.xpath("//b[text()='"+city+"']")).isDisplayed();
	}

	public String searchedCityTemprature(String city) {
		return driver.findElement(By.xpath("//li[@class='searched']//td[3]")).getText();
	}

	public boolean isNotificationPopUpDisplayed(){
		return notificationPopup.isDisplayed();
	}

	public void closeNotificationPopupButton(){
		notificationPopupNotNowButton.click();
	}
}


```


The above page class is using PageFactory to achieve Page Object Model. PageFactory is one of the way to achieve PageObjectModel.With PageFactory we define the WebElements using @FindBy Annotation. PageFactory is used for Lazy Initialization that is it looks for Weblement every time a method is called on it. It does not stores the Webelement within cache. To avoid PageFactory to look for webelement everytime we can use @CacheLookUp.

<img width="784" height="754" alt="image" src="https://github.com/user-attachments/assets/b7e22c22-b0d7-47d4-9585-0a1d36cc7d81" />

<img width="930" height="580" alt="image" src="https://github.com/user-attachments/assets/0ee34d5e-1a78-43f0-bbd0-4e74b9413d75" />

<img width="958" height="521" alt="image" src="https://github.com/user-attachments/assets/826792ba-2c55-4cd8-96ef-6303d8f2b0e1" />

PageFactory has not been decommissioned in Selenium 4, but its use is now discouraged by the Selenium team. The class is still available and functional, but Selenium contributors recommend alternatives that are more efficient and less prone to issues like the StaleElementReferenceException

## Why PageFactory is no longer the recommended approach

The reasons for moving away from `PageFactory` are related to performance and reliability issues.

- **Lazy initialization can cause issues:** `PageFactory` uses "lazy initialization," where it only locates elements when they are first used. This can cause problems with dynamic web pages (AJAX-heavy pages) if the DOM changes after the page object is initialized but before the element is accessed.

- **Performance overhead:** With `PageFactory`, the driver will locate the element every single time a method is called on it, which can cause performance degradation. While `@CacheLookup` was designed to solve this by caching a reference to the element, it is prone to the `StaleElementReferenceException` if the page's DOM changes.

- **Less flexibility:** `PageFactory` does not provide an easy way to handle dynamic locators, which are common in modern web applications.

|                             | **PageFactory Approach (Discouraged)**                                                                                                       | **Recommended POM Approach**                                                                                                 |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| **Element declaration**     | Uses annotations like `@FindBy` for fields.<br>`@FindBy(id = "user-name") private WebElement usernameField;`                                    | Uses the `By` class to define locators.<br>`static final By usernameField = By.id("user-name");`                              |
| **Element access**          | Accesses the element directly as a `WebElement`.<br>`usernameField.sendKeys("testuser");`                                                      | Locates the element at the time of action.<br>`driver.findElement(usernameField).sendKeys("testuser");`                       |
| **Element initialization**  | The `PageFactory.initElements(driver, this);` method initializes the page object.                                                             | Locators are declared, but elements are fetched on demand using `driver.findElement()`.                                       |
| **Best suited for**         | Small, simple projects with mostly static pages.                                                                                              | All projects, particularly complex ones.                                                                                      |


----

**utility** : Utility folder contains all the utility files like Listners for Extent Report,TestConstant File, Utlity code to retrieve Test Dta from Excel. Code for Taking Screenshot.

----

**test** : test folder consist of all the Test classes. Single Responsibility Principal is maintained as Tests only  contain assertions & flows.


```java
import java.io.IOException;

import org.testng.Assert;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.DataProvider;
import org.testng.annotations.Test;

import base.TestBase;
import io.restassured.RestAssured;
import io.restassured.response.Response;
import pages.WeatherPage;
import util.TestConstants;
import util.Utility;

public class WeatherPageTest extends TestBase {

	public WeatherPage weatherPage;
	public double temperatureInKelvinFromUI;
	public double temperatureInKelvinfromAPI;
	public double variance;

	public WeatherPageTest() {
		super();
	}

	@BeforeClass
    @Parameters({"browser","headless"})
	public void setUp(){
		initialization();
		weatherPage=new WeatherPage();
		if(weatherPage.isNotificationPopUpDisplayed()){
			weatherPage.closeNotificationPopupButton();
		}
	}

	@Test(dataProvider = "cityData")
	public void verifyVarianceInTemperatureFromUIAndAPI(String City){
		weatherPage.searchCity(City);
		Assert.assertTrue(weatherPage.searchedCityIsDisplayed(City));
		String completeTempurature=weatherPage.searchedCityTemprature(City);
		double temperatureInCelcius=Utility.getTemperatureInCelcius(completeTempurature);
		temperatureInKelvinFromUI=Utility.getTemperatureInKelvin(temperatureInCelcius);
		Response response=RestAssured.given().log().all()
				.spec(TestBase.buildRequestSpec(City,TestConstants.API_KEY))
				.when().post()
				.then().log().all()
				.spec(TestBase.buildResponseSpec())
				.extract().response();
		String temperature=response.jsonPath().getString("main.temp");
		temperatureInKelvinfromAPI= Utility.convertStringtoNumeric(temperature);
		variance=Math.abs(temperatureInKelvinfromAPI-temperatureInKelvinFromUI);
		Assert.assertTrue(variance<=TestConstants.variance,
				"\nTemperature Variance is more than 2 for city : " + City + "\nTemparture Through UI is : " +
				temperatureInKelvinFromUI +
						"  " +
						"\nTemperature through API is : " + temperatureInKelvinfromAPI + "\nVariance is : " + variance);
	}

	@DataProvider(name="cityData")
	Object[][] getCities() throws IOException {
		String [][] cities={{"Pune"},{"Bengaluru"},{"Chennai"},{"Chandigarh"},{"Nagpur"},{"Indore"}};
		return (cities);
	}


	@AfterClass
	public void shutDown(){
		driver.quit();
	}
}


```

**Understanding Soft and HardAsserts**

| Type            | Behavior                                           | Use When                            |
| --------------- | -------------------------------------------------- | ----------------------------------- |
| **Hard Assert** | Stops execution immediately on failure             | Critical path / preconditions.Useful for **critical validations**, where there’s no point continuing if the check fails.       |
| **Soft Assert** | Continues execution and reports all failures later | Multiple non-blocking verifications |



```java
@Test
public void verifyCheckoutSummary() {
    SoftAssert softAssert = new SoftAssert();

    // Hard assert - critical login check
    Assert.assertTrue(loginPage.isLoggedIn(), "Login failed!");

    // Soft asserts for visual/UI validations
    softAssert.assertEquals(cartPage.getItemCount(), 3, "Item count mismatch");
    softAssert.assertEquals(cartPage.getTotalPrice(), "$250.00", "Total price incorrect");
    softAssert.assertTrue(cartPage.isCheckoutButtonVisible(), "Checkout button missing");

    // Collate and report all soft failures
    softAssert.assertAll();
}
```


**PR Review Points**

PR review Strategy -

1. Whether the code is functioning as per the Jira requirement.
2. Check Asertion are validating correct outcome
3. Ensure that the given code is not dupicated.
4. Check if the code is generic and can be converted into utility method so that the same can be used by other classes.
6. Check that the data is not harcoded and is externalized via configuation files,csv,json,database.
6. Does the code follow project convention(naming,identation,spacing)
7. Commenting and Documentation - Is the code selfexplanatory? Where the logic is complex,Are there inline comment or javadoc
8. Do we have proper waits before performing operations on a Weblement.
9. Verify locator strategy, Ensure absolute locater is not used.
10. Do not write Assertions in Page classes, Assertion should only be written in Test classes.Test Classes should never use/call driver APIs(findelement,click,sendkeys)

https://www.linkedin.com/pulse/interview-241-automation-what-your-checklist-zyjsc/





