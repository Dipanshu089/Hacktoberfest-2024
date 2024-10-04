Problem Statement:
Design a data structure that represents an LRU (Least Recently Used) cache. The cache should have two primary operations:
1. get(key): This operation retrieves the value associated with the given key if it exists in the cache. If the key does not exist, return -1.
2. put(key, value): This operation inserts a new key-value pair into the cache. If the cache has reached its maximum capacity, it should remove the least recently used key-value pair to make space for the new one.

Your cache should maintain the order of access, meaning that if a key is accessed (either through a get or put operation), it should be considered the most recently used key. The cache should discard the least recently used key-value pair when it exceeds its capacity.

Requirements:
1. Use an appropriate data structure that supports fast access and removal.
2. The capacity of the cache should be provided during initialization.

Constraints:
1. The cache capacity is a positive integer.
2. Keys and values are integers.

Solution Explanation:
We can implement the LRU Cache using Python's OrderedDict, which maintains the insertion order of keys. The idea is to:
1. Get Operation: If the key exists, we move it to the end of the dictionary to mark it as recently used and return its value. If the key doesn't exist, return -1.
2. Put Operation: If the key already exists, we move it to the end to mark it as recently used. Then, we insert/update the key-value pair. If the cache exceeds its capacity, we remove the least recently used item (the first item in the dictionary).

Time Complexity:
1. get: O(1) because accessing elements in a dictionary and moving them to the end are O(1) operations.
2. put: O(1) for both inserting a new key and evicting the least recently used key.

Test Case Explanation:
1. Put(1,1): Inserts key 1 with value 1.
2. Put(2,2): Inserts key 2 with value 2. The cache now has two entries: {1:1, 2:2}.
3. Get(1): Key 1 is accessed, so it becomes the most recently used. The cache is still {1:1, 2:2}, but key 1 is now marked as more recent.
4. Put(3,3): Key 2 is evicted because it's the least recently used. Key 3 is inserted, so the cache is {1:1, 3:3}.
5. Get(2): Key 2 was evicted, so the result is -1.
6. Put(4,4): Key 1 is evicted (least recently used), and key 4 is inserted. The cache becomes {3:3, 4:4}.
7. Get(1): Key 1 was evicted, so the result is -1.
8. Get(3): Key 3 is in the cache, so the result is 3.
9. Get(4): Key 4 is in the cache, so the result is 4.