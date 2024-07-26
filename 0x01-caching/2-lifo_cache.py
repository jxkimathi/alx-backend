#!/usr/bin/python3
"""LIFO Caching"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """Class LIFOCache inheriting from BaseCaching"""
    def __init__(self):
        """The initialization method"""
        super().__init__()

    def put(self, key, item):
        """Assign to the dict the item value for the key"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                last_item = list(self.cache_data.keys())[-1]
                del self.cache_data[last_item]
                print(f"DISCARD: {last_item}\n")

    def get(self, key):
        """Return the value linked to key"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
