#!/usr/bin/env python3
"""LFU Caching"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """Class LFUCache inheriting from BaseCaching"""
    def __init__(self):
        """The initialization method"""
        super().__init__()
        self.lfu_keys = []

    def put(self, key, item):
        """Assign the item value for the key"""
        if item is not None and key is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.lfu_keys.remove(key)
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    lfu_key = self.lfu_keys.pop(0)
                    del self.cache_data[lfu_key]
                    print(f"DISCARD: {lfu_key}\n")
                self.cache_data[key] = item
            self.lfu_keys.append(key)

    def get(self, key):
        """Return the value linked to the key"""
        if key is not None and key in self.cache_data:
            self.lfu_keys.remove(key)
            self.lfu_keys.append(key)
            return self.cache_data[key]
        return None


