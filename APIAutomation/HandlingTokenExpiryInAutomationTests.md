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

2. **Refresh the token when it expires.** In your test, catch token expiry errors and refresh the token. Then retry the request.

   ```java
   try {
     api.get("/resource")  
   } catch (TokenExpiredException e) {
     AccessTokenResponse tokenResponse = api.refreshToken();  
     accessToken = tokenResponse.getAccessToken();
     api.get("/resource") 
   }
   ```

3. **Generate a new token for each test.** In the setup of each test, call the authorization API to generate a new token. This ensures each test has a fresh token.

4. **Increase the token expiry time.** If possible, extend the token expiry time to be longer than your test suites. This reduces the need to refresh tokens during testing.

5. **Mock the authorization.** In your test base class, mock the authorization request to return a test token. This token can then be used for all test requests.

If a test fails due to token expiry, you can refresh the token and retry the request to see if the test passes. If it still fails after refreshing the token, then the failure was likely due to something else. Handling token expiry in a robust way helps make your API tests more stable and reliable.
