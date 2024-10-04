from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        """
        Initialize the LRU cache with a given capacity.
        :param capacity: The maximum number of items the cache can hold.
        """
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        """
        Retrieve the value for the given key if it exists in the cache.
        :param key: The key to search for.
        :return: The value if the key is found, else -1.
        """
        if key in self.cache:
            # Move the key to the end to mark it as recently used
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        """
        Insert a new key-value pair into the cache.
        :param key: The key to insert.
        :param value: The value to associate with the key.
        """
        if key in self.cache:
            # Move the key to the end to mark it as recently used
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            # Remove the least recently used item (the first one in the OrderedDict)
            self.cache.popitem(last=False)

# Test Cases
lru_cache = LRUCache(2)
lru_cache.put(1, 1)
lru_cache.put(2, 2)
print(lru_cache.get(1))  # Output: 1 (Key 1 is accessed, so it becomes most recently used)
lru_cache.put(3, 3)      # Evicts key 2 (Key 2 was least recently used)
print(lru_cache.get(2))  # Output: -1 (Key 2 is not in the cache anymore)
lru_cache.put(4, 4)      # Evicts key 1 (Key 1 was least recently used)
print(lru_cache.get(1))  # Output: -1 (Key 1 is not in the cache anymore)
print(lru_cache.get(3))  # Output: 3 (Key 3 is in the cache)
print(lru_cache.get(4))  # Output: 4 (Key 4 is in the cache)
