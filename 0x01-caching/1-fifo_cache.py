#!/usr/bin/env python3
"""
First In First Out Cache
"""
baseCaching = __import__("base_caching").BaseCaching


class FIFOCache(baseCaching):
    """
    FIFO Cache
    """

    def __init__(self):
        """initialize inherited class attrribute"""
        super().__init__()
        self.hold = []

    def put(self, key, item):
        """
        put method to the dictionary
        Args:
            key(str): the dictionary key
            item(Any): the dictionary items
        """

        if key is not None and item is not None:
            if len(self.cache_data) >= baseCaching.MAX_ITEMS:
                first_key = self.hold.pop(0)
                del self.cache_data[first_key]
                print(f"DISCARD: {first_key}")

            self.cache_data[key] = item
            self.hold.append(key)

    def get(self, key):
        """
        get value
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
