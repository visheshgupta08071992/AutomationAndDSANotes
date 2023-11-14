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

3. **Refresh the token when it expires using If condition.** In your test, Within if condition check if you are retrievng 401 UnAuthorized statuscode,If yes refresh the Token

```
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

5. **Increase the token expiry time.** If possible, extend the token expiry time to be longer than your test suites. This reduces the need to refresh tokens during testing.


If a test fails due to token expiry, you can refresh the token and retry the request to see if the test passes. If it still fails after refreshing the token, then the failure was likely due to something else. Handling token expiry in a robust way helps make your API tests more stable and reliable.
