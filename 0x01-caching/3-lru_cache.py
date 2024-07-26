#!/usr/bin/python3
"""LRU Caching"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """Class LRUCache inheriting from BaseCaching"""
    def __init__(self):
        """The initialization method"""
        super().__init__()

    def put(self, key, item):
        """Assign the dict the item value for the key"""
        if item is not None and key is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                lru_key = next(iter(self.cache_data))
                del self.cache_data[lru_key]
                print(f"DISCARD: {lru_key}\n")

    def get(self, key):
        """Return the value linked to the key"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
