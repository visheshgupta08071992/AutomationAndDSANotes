# Handling Authorization Token Expiry in API Automation Tests

There are a few ways you can handle authorization token expiry in your API automation tests written in RestAssured:

1. **Refresh the token before each test.** In your test base class, call the API to refresh the access token before each test method runs. This ensures you have a valid token for that test.

   ```java
   @BeforeMethod
   public void refreshToken() {
     // Call API to refresh access token
     AccessTokenResponse tokenResponse = api.refreshToken();  
     // Set new access token 
     accessToken = tokenResponse.getAccessToken();
   }
   ```

**Advantages:**
- Every test starts with a fresh access token.
- Easy to implement.
- Reduces failures caused by token expiry during test execution.

**Disadvantages:**
- Generates unnecessary authentication API calls.
- Increases execution time.
- Does not scale efficiently when you have hundreds or thousands of test cases.
- Can create unnecessary load on the authentication server.

2. **Refresh the token when it expires using Try/Catch.** In your test, catch token expiry errors and refresh the token. Then retry the request.

   ```java
   try {
     api.get("/resource")  
   } catch (UnauthorizedException  e) {
     AccessTokenResponse tokenResponse = api.refreshToken();  
     accessToken = tokenResponse.getAccessToken();
     api.get("/resource") 
   }
   ```

In Rest Assured, receiving HTTP 401 does not automatically throw an UnauthorizedException.

For example:
```java
Response response = given()
        .when()
        .get("/resource");
```


Even if the server returns HTTP 401, Rest Assured generally returns a Response object.

You need to explicitly check the status code or configure an exception mechanism yourself.

My suggestion: Prefer checking the HTTP status code rather than relying on Try-Catch for normal HTTP responses.</br></br>

3. **Refresh the token when it expires using If condition.** In your test, Within if condition check if you are retrievng 401 UnAuthorized statuscode,If yes refresh the Token

```java
 @Test
    public void yourApiTestMethod() {
        Response response = RestAssured.given()
                .header("Authorization", "Bearer " + accessToken)
                .when()
                .get("your_api_endpoint");

        // Check if the response is 401 Unauthorized
        if (response.getStatusCode() == 401) {
            // Refresh the token
            accessToken = refreshAccessToken();

            // Retry the API request with the new token
            response = RestAssured.given()
                    .header("Authorization", "Bearer " + accessToken)
                    .when()
                    .get("your_api_endpoint");
        }

        // Perform your assertions and other test logic based on the response
    }
```


This is better than Approach 2 because you are explicitly checking the HTTP response.

However, I would make two improvements:

```
1. Move this Token Refresh logic into Thread Safe reusable reusable method. AlsoImagine 10 test threads are running simultaneously and all receive 401.

Without proper synchronization, all 10 threads might attempt to refresh the token simultaneously.

You should implement thread-safe token refresh logic, such as synchronized refresh with a token-version check, so that only one thread refreshes a given expired token and other threads reuse the new token.
2. Retry only once to avoid infinite retry loops.
```




4. **Increase the token expiry time.** If possible, extend the token expiry time to be longer than your test suites. This reduces the need to refresh tokens during testing.


If a test fails due to token expiry, you can refresh the token and retry the request to see if the test passes. If it still fails after refreshing the token, then the failure was likely due to something else. Handling token expiry in a robust way helps make your API tests more stable and reliable.
