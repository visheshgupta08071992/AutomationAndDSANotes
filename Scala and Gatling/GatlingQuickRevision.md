## Gatling in Detailed Github MD links

**Scala** - https://github.com/visheshgupta08071992/AutomationAndDSANotes/blob/master/Scala%20and%20Gatling/Scala.md

**Gatling** - https://github.com/visheshgupta08071992/Gatling/blob/master/Understanding%20Gatling.md

**Gatling Framework** - https://github.com/visheshgupta08071992/GatlingTestPerformanceFramework-Advance/tree/master/src/test/scala/com/GatlingPerformanceFramework


## Gatling quick revison along with framework structure

Creating a Gatling Test involves three major things -

1. Creating All Http requests.
2. Creating Scenarios while are nothing but one or more then one linked executable https requests.
3. Creating Simulations - Simulations are nothing but running different scenarios against different load/concurrency.


## Understanding brief Gatling Framework Structure -


![image](https://github.com/user-attachments/assets/f79448d0-7ae6-486b-bc45-acb3f76e4200)


## Understanding Config Object which contains all config details

```scala
package com.GatlingPerformanceFramework.config

object Config {

  val DEV_URL = "https://QAurl.com"
  val QA_URL = "https://Devurl.com"
  val UAT_URL = "https://UATurl.com"
  val TOKEN = "Bearer tokenID"
  val postHeader = Map("SECURITY-TENANT-ID" -> "clientId",
    "SECURITY-PRINCIPAL-ID" -> "userID",
    "Authorization" -> TOKEN,
    "Content-Type" -> "application/json")

  val postHeaderForACL = Map("SECURITY-TENANT-ID" -> "clientId",
    "MS-PROFILE-ID" -> "userProfileID",
    "Authorization" -> TOKEN,
    "Content-Type" -> "application/json")

  val getHeader = Map("SECURITY-TENANT-ID" -> "clientID",
    "SECURITY-PRINCIPAL-ID" -> "userID",
    "Authorization" -> TOKEN)

  val asOfDate="2021-01-01"

  val Port50KQA="Gatling-Load-100K-1"
  
  val app_url = "https://reqres.in/"

  val users = Integer.getInteger("users", 10).toInt
  val rampUp = Integer.getInteger("rampup", 100).toInt
  val throughput = Integer.getInteger("throughput", 100).toInt
  val rateStartRange = Integer.getInteger("rateStartRange", 1).toInt
  val rateEndRange = Integer.getInteger("rateEndRange", 5).toInt
}

```

### Understanding how to create HTTP requests and various checks while creating http Request

As a best practise we should create all the requests within Requests objects present within request folder

```scala
  def addListOfPortfolios(portfolioId: String,positionId: String,instrumentId: String) = http("Add List of Portfolios Request")
    .post(DEV_URL + "/portfolios")
    .headers(postHeader)
    .header("Content-Type","application/json")
 //   .body(ElFileBody("./src/test/resources/bodies/AddListOfPortfolios.json"))
    .body(ElFileBody("C://Users/guptvis/OneDrive/OneDrive - MSCI Office 365/Desktop/PositionJson/portfolio.json"))
    .asJson
    .check(status is 200)
    .check(jsonPath("$[0].success").ofType[Boolean].is(true))
    .requestTimeout(60000)

```

As seen above the function `addListOfPortfoliosthat` accepts three parameters: `portfolioId`, `positionId`, and `instrumentId`, all of which are strings.
It creates an HTTP request for adding list of portfolios.

### Why `addListOfPortfolios` Has No Return Type Defined

In Scala, if the return type can be inferred, specifying it explicitly is optional. Since the entire method body is a Gatling HTTP request (which is an `HttpRequestBuilder` type in Gatling), Scala automatically assigns `HttpRequestBuilder` as the return type.

### Absence of Curly Braces `{}`

In Scala, if a method body contains only a single expression, curly braces `{}` are optional. Here, the method body consists of a single HTTP request expression, so braces are not required.

### Would It Be OK to Add Braces?

Yes, you could add curly braces for readability, especially if the method grows in complexity. Adding them doesn’t affect the functionality:

```scala
def addListOfPortfolios(portfolioId: String, positionId: String, instrumentId: String) = {
  http("Add List of Portfolios Request")
    .post(DEV_URL + "/portfolios")
    .headers(postHeader)
    .header("Content-Type", "application/json")
    .body(ElFileBody("C://Users/guptvis/OneDrive/OneDrive - MSCI Office 365/Desktop/PositionJson/portfolio.json"))
    .asJson
    .check(status is 200)
    .check(jsonPath("$[0].success").ofType[Boolean].is(true))
    .requestTimeout(60000)
}
```

### Now lets understand different parts of request

1.**ElFileBody** -  EL allows you to inject variables and dynamic content into your file, making it ideal for scenarios where the request data needs to be customized per request.

2.**gzipBody** - gzipBody is used to gzip-compress the request body content, typically for performance optimization or when the server expects compressed data.

  **Syntax:** `gzipBody(StringBody("<body_content>"))`


3.**RawFileBody** - RawFileBody reads the request body from a file without processing any placeholders or expressions. It is suitable for binary files or static content that doesn’t require variable substitution.

  **Syntax:** `RawFileBody("<path_to_file>")`


4.**StringBody** -  StringBody allows you to define the request body directly as a string. It’s useful for small requests or scenarios where you want to define the request data inline. Like ElFileBody, StringBody also supports Gatling’s Expression Language (EL) for variable substitution.

```scala
.exec(http("Add Portfolio with Inline JSON")
  .post("/portfolios")
  .body(StringBody("""{"portfolioId": "${portfolioId}", "positionId": "${positionId}"}"""))
  .asJson
  .check(status.is(200))
)
```

### Summary Table

| Method         | Use Case                                           | Dynamic Content Support | Example                          |
|----------------|----------------------------------------------------|--------------------------|----------------------------------|
| **ElFileBody** | File-based with dynamic content (e.g., JSON files) | Yes                      | `.body(ElFileBody("path.json"))` |
| **gzipBody**   | Compress the request body                          | Yes (nested body)        | `.body(gzipBody(StringBody(...)))` |
| **RawFileBody**| Static file-based content (e.g., images, binary)   | No                       | `.body(RawFileBody("image.png"))` |
| **StringBody** | Inline body with dynamic content                   | Yes                      | `.body(StringBody("{...}"))`     |









