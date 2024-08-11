#!/usr/bin/python3
"""LRU Caching"""
BaseCaching = __import__('base_caching').BaseCaching
from collections import OrderedDict

class LRUCache(BaseCaching):
    """Class LRUCache inheriting from BaseCaching"""
    def __init__(self):
        """The initialization method"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Assign to the dict the item value for the key"""
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data.move_to_end(key)
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_key = next(iter(self.cache_data))
                print(f"DISCARD: {first_key}")
                self.cache_data.pop(first_key)

    def get(self, key):
        """Return the value linked to key"""
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
        return None
