#!/usr/bin/python3
"""MRU Caching"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """Class MRUCache inheriting from BaseCaching"""
    def __init__(self):
        """The initialization method"""
        super().__init__()

    def put(self, key, item):
        """Assign the item value for the key"""
        if item is not None and key is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                mru_key = max(self.cache_data, key=self.cache_data.get)
                del self.cache_data[mru_key]
                print(f"DISCARD: {mru_key}\n")

    def get(self, key):
        """Return the value linked to the key"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
