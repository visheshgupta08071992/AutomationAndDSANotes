Cache is InMemory Database used to store frequently accessed data temporarily thus reducing frequent Database Operation and improving overall performance .

Consider an example where the user is frequentlys retreive the same details, It does not make sense for the application to perform same Database operation again and again for retrieving the same data. Instead we can bring cache which can store these frequently accessed data and thus reduce database operation and improve overall performance of the system.

### Caching:

1. **How it Works:**
   - When a system receives a request for data, it first checks whether the requested data is available in the cache.
   - If the data is found in the cache (cache hit), it is returned to the requester without accessing the original data source, which is typically more time-consuming.
   - If the data is not found in the cache (cache miss), the system retrieves it from the original source, stores it in the cache, and then serves it to the requester.

### Cache Invalidation:

Cache invalidation is the process of updating or deleting cache data when cache becomes outdated or invalid.

1. **Time-Based Invalidation(ttl: Time to leave):**
   - Cached data is considered valid for a specific time period, after which it is automatically invalidated, and the next request triggers a refresh.
   - This approach is simple but may result in serving stale data if the expiration time is too long.

2. **Event-Based Invalidation:**
   - The cache is invalidated based on specific events or changes in the underlying data. Cache should be automatically invalidated when data is updated at source. 
   - This approach requires a mechanism to detect and propagate changes to the cache.
  
2. **Manual Invalidation:**
   - we can Explicitly remove or update the cache when data is updated with the help of API endpoint.
   .

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
  
 # Different Caching Patterns

There are several common caching patterns:

## 1. Cache Aside

With the cache aside pattern, the application first checks the cache for the data. If it's not found, it retrieves the data from the primary data source and then stores it in the cache for future requests.

```
if (data not found in cache) {
  data = fetch from database;
  cache.set(data);
}
return data;  
```

Advantages:

- Simple to implement
- Only caches data that is actually used

Disadvantages:

- Initial request has a cache miss, causing a performance hit 
- Cache invalidation can be difficult

Use when:

- Data is read-heavy and infrequently updated

## 2. Read Through

The read through pattern is similar to cache aside. The difference is that when there is a cache miss, the cache itself retrieves the data from the database and stores it.

```
data = cache.get(key);
if (data not found) {
   data = cache.get_from_db(key);
   cache.set(data); 
}
return data;
```

Advantages:

- Same as cache aside

Disadvantages:

- Same as cache aside

Use when:

- Same as cache aside

## 3. Write Through

With write through caching, data is written both to the cache and the database simultaneously.

```
db.update(data);
cache.set(data);
```

Advantages:

- Consistent data between cache and database
- Cache invalidation is not needed

Disadvantages:

- Higher latency for writes
- More complex to implement

Use when:

- Data is write-heavy

## 4. Write Back/Write Behind

Data is written to the cache only, and then asynchronously written to the database.

```
cache.set(data);
// Asynchronous write to DB 
db.update_async(data);
```

Advantages: 

- Faster initial write latency

Disadvantages:

- Potential for data loss if cache fails before write to DB completes
- More complex

Use when:

- Writes can tolerate some data loss

Hope this explanation of the most common caching patterns helps! Let me know if you have any other questions.

**Referance**
https://www.youtube.com/watch?v=Ez1GK2imrsY
