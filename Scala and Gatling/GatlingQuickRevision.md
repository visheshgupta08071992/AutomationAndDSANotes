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

```
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




