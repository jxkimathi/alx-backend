#!/usr/bin/python3
"""Basic dictionary caching"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Class BasicCache that inherits from BaseCahing"""
    def put(self, key, item):
        """Assign to the dict self.cache_data the item value for the key"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Return the value in self.cache_data"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
