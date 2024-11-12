## Percentile Response Time

Percentile response time indicates that the response time for a given percentage of users (N percentile) would be the given time or even less.

For example:
- **99th Percentile Response Time**: If the 99th percentile response time of an API is 5 seconds, we can say that for 99% of users, the response time would be 5 seconds or even less. Only for the remaining 1% of users, the response time would be more than 5 seconds.
- **95th Percentile Response Time**: If the 95th percentile response time of an API is 3 seconds, we can say that for 95% of users, the response time would be 3 seconds or even less. Only for the remaining 5% of users, the response time would be more than 3 seconds.

### How to Calculate Percentile Response Time

To calculate the percentile response time:
1. **Collect Response Times**: Obtain the response times for a set of identical requests (e.g., 1000 requests).
2. **Sort Response Times**: Arrange the response times in ascending order.
3. **Identify the Position**:
   - For the 99th percentile, find the response time at the 99th percentile position out of the total records.
   - Example: For 1000 records, 99% of 1000 is 990, so the 99th percentile response time would be the response time at the 990th position in the sorted list.

