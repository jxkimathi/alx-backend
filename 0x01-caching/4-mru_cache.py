#!/usr/bin/python3
"""MRU Caching"""
BaseCaching = __import__('base_caching').BaseCaching
from collections import OrderedDict

class MRUCache(BaseCaching):
    """Class MRUCache inheriting from BaseCaching"""
    def __init__(self):
        """The initialization method"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Assign to the dict the item value for the key"""
        if key is not None and item is not None:
            if key in self.cache_data:
                del self.cache_data[key]
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Pop the most recently used item
                last_key, _ = self.cache_data.popitem(last=True)
                print(f"DISCARD: {last_key}")
            self.cache_data[key] = item

    def get(self, key):
        """Return the value linked to key"""
        if key is not None and key in self.cache_data:
            # Move the key to the end to mark it as recently used
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
        return None
