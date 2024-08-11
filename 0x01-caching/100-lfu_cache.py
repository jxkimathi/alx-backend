
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


my_cache = LFUCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
print(my_cache.get("B"))
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
print(my_cache.get("A"))
print(my_cache.get("B"))
print(my_cache.get("C"))
my_cache.put("F", "Mission")
my_cache.print_cache()
my_cache.put("G", "San Francisco")
my_cache.print_cache()
my_cache.put("H", "H")
my_cache.print_cache()
my_cache.put("I", "I")
my_cache.print_cache()
print(my_cache.get("I"))
print(my_cache.get("H"))
print(my_cache.get("I"))
print(my_cache.get("H"))
print(my_cache.get("I"))
print(my_cache.get("H"))
my_cache.put("J", "J")
my_cache.print_cache()
my_cache.put("K", "K")
my_cache.print_cache()
my_cache.put("L", "L")
my_cache.print_cache()
my_cache.put("M", "M")
my_cache.print_cache()