#!/usr/bin/python3
"""LFU Caching"""
BaseCaching = __import__('base_caching').BaseCaching
from collections import OrderedDict, defaultdict

class LFUCache(BaseCaching):
    """Class LFUCache inheriting from BaseCaching"""
    def __init__(self):
        """The initialization method"""
        super().__init__()
        self.cache_data = OrderedDict()
        self.frequency = defaultdict(int)
        self.usage_order = OrderedDict()

    def put(self, key, item):
        """Assign to the dict the item value for the key"""
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.frequency[key] += 1
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    # Find the least frequently used key
                    min_freq = min(self.frequency.values())
                    lfu_keys = [k for k, v in self.frequency.items() if v == min_freq]
                    # If multiple keys have the same min frequency, use LRU policy
                    if len(lfu_keys) > 1:
                        lru_key = None
                        for k in self.usage_order:
                            if k in lfu_keys:
                                lru_key = k
                                break
                    else:
                        lru_key = lfu_keys[0]
                    del self.cache_data[lru_key]
                    del self.frequency[lru_key]
                    del self.usage_order[lru_key]
                    print(f"DISCARD: {lru_key}")
                
                self.cache_data[key] = item
                self.frequency[key] = 1
            # Update usage order
            if key in self.usage_order:
                del self.usage_order[key]
            self.usage_order[key] = None

    def get(self, key):
        """Return the value linked to key"""
        if key is not None and key in self.cache_data:
            self.frequency[key] += 1
            # Update usage order
            del self.usage_order[key]
            self.usage_order[key] = None
            return self.cache_data[key]
        return None
