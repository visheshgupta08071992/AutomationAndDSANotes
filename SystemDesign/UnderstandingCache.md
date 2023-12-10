Cache is an inmemory database which could be used to store all the commonly used data.

### Caching:

1. **How it Works:**
   - When a system receives a request for data, it first checks whether the requested data is available in the cache.
   - If the data is found in the cache (cache hit), it is returned to the requester without accessing the original data source, which is typically more time-consuming.
   - If the data is not found in the cache (cache miss), the system retrieves it from the original source, stores it in the cache, and then serves it to the requester.

2. **Benefits:**
   - Improved performance: Frequently accessed data is readily available, reducing the need to repeatedly fetch it from slower sources.
   - Reduced latency: Caching helps minimize the time it takes to retrieve data, leading to faster response times.

### Cache Invalidation:

Cache invalidation is the process of removing or updating cached data to ensure that the cached information remains accurate and up-to-date. There are different strategies for cache invalidation:

1. **Time-Based Invalidation(ttl: Time to leave):**
   - Cached data is considered valid for a specific time period, after which it is automatically invalidated, and the next request triggers a refresh.
   - This approach is simple but may result in serving stale data if the expiration time is too long.

2. **Event-Based Invalidation:**
   - The cache is invalidated based on specific events or changes in the underlying data. When the data changes, the corresponding cache entries are marked as invalid.
   - This approach requires a mechanism to detect and propagate changes to the cache.

### Cache Eviction:

Cache eviction is the process of removing items from the cache to make room for new items. When a cache reaches its capacity, and there is a need to store new data, the system must decide which existing items to evict. Common cache eviction policies include:

1. **Least Recently Used (LRU):**
   - Evicts the least recently accessed items first.
   - Keeps track of the order in which items are accessed and removes the least recently accessed ones.

2. **Most Recently Used (MRU):**
   - Evicts the most recently accessed items first.
   - Retains the items that have been accessed most recently.

3. **First-In-First-Out (FIFO):**
   - Evicts the oldest items first.
   - Maintains a queue of items and removes the ones that have been in the cache the longest.
  
4. **Least Frequently Used (LFU):**
   - Evicts the least Frequently accessed items first.

### Caching Patterns:

1. **Write-Through Cache:**
   - Data is written to both the cache and the underlying data store simultaneously. Ensures that the cache is always synchronized with the data store.

2. **Write-Behind Cache (Write-Behind Caching):**
   - Data is initially written to the cache and later asynchronously written to the underlying data store. This can improve write performance.

3. **Read-Through Cache:**
   - When a cache miss occurs, the cache automatically retrieves the missing data from the underlying data store and updates the cache.

4. **Lazy Loading (or Lazy Initialization):**
   - Data is only loaded into the cache when it is requested. It helps minimize the initial load on the system.

**Referance**
https://www.youtube.com/watch?v=Ez1GK2imrsY
