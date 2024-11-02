#!/usr/bin/env python3
"""
Least Frequently Used (LFU) Cache
"""
BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    """
    LFU Cache
    """

    def __init__(self):
        """Initialize the cache"""
        super().__init__()
        self.usage_frequency = {}  # Dictionary to track the frequency of usage of each key  # noqa
        self.usage_order = []      # List to track the order of usage of keys  # noqa

    def put(self, key, item):
        """
        Add an item to the cache using LFU algorithm
        Args:
            key (str): the dictionary key
            item (Any): the dictionary item
        """

        if key is None or item is None:
            return

        # If the key is already in the cache, update its value and frequency  # noqa
        if key in self.cache_data:
            self.cache_data[key] = item
            self.usage_frequency[key] += 1
            self.usage_order.remove(key)
            self.usage_order.append(key)
        else:
            # If the cache is full, remove the least frequently used item noqa
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find the minimum frequency
                min_freq = min(self.usage_frequency.values())

                # Find keys with the minimum frequency
                min_freq_keys = [k for k, v in self.usage_frequency.items() if v == min_freq]  # noqa

                # If there's more than one key with the minimum frequency, use LRU to decide  # noqa
                if len(min_freq_keys) > 1:
                    lfu_key = min_freq_keys[0]
                    for k in min_freq_keys:
                        if self.usage_order.index(k) < self.usage_order.index(lfu_key):  # noqa
                            lfu_key = k
                else:
                    lfu_key = min_freq_keys[0]

                # Remove the LFU (or LRU among LFU) key
                del self.cache_data[lfu_key]
                del self.usage_frequency[lfu_key]
                self.usage_order.remove(lfu_key)
                print(f"DISCARD: {lfu_key}")

            # Add the new key-value pair to the cache and initialize its frequency  # noqa
            self.cache_data[key] = item
            self.usage_frequency[key] = 1
            self.usage_order.append(key)

    def get(self, key):
        """
        Retrieve the value associated with the key from cache_data
        """
        if key is None or key not in self.cache_data:
            return None

        # Increment the frequency of access and update usage order
        self.usage_frequency[key] += 1
        self.usage_order.remove(key)
        self.usage_order.append(key)
        return self.cache_data[key]
