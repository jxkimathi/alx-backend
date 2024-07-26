#!/usr/bin/python3
"""FIFO Caching"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """Class FIFOCache that inherits from BaseCaching"""
    def __init__(self):
        """The initialization method"""
        super().__init__()

    def put(self, key, item):
        """Assign to the dict the item value for the key"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_item = next(iter(self.cache_data))
                del self.cache_data[first_item]
                print("DISCARD:", first_item)

    def get(self, key):
        """Return the value linked to key"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
