#!/usr/bin/env python3
"""
LIFOCache
"""
BaseCaching = __import__("base_caching").BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache
    """

    def __init__(self):
        """
        Initializer
        """
        super().__init__()
        self.hold = []

    def put(self, key, item):
        """
        put for key items
        Args:
            key(str): key of dictionary
            item(Any): value of dictionary
        """
        if key in self.cache_data:
            self.hold.remove(key)

        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lfu = self.hold.pop()
                del self.cache_data[lfu]
                print(f"DISCARD: {lfu}")
            self.cache_data[key] = item
            self.hold.append(key)

    def get(self, key):
        """
        get key
        """
        if key is None or key not in self.cache_data:
            return None
        self.hold.remove(key)
        self.hold.append(key)
        return self.cache_data[key]
