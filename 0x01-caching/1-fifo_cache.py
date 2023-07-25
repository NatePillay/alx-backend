#!/usr/bin/python3
""" FIFOCache module inherits from BaseCaching and is a caching system
"""


BaseCaching = __import__('base_caching').BaseCaching
from collections import OrderedDict

class FIFOCache(BaseCaching):
    """ FIFO defines:
      - inherits from BaseCaching and is a caching system
      - where your data are stored (in a dictionary)
    """
    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """assign to the {} self.cache_data the item value for the key
        """
        if item and key:
            if len(self.cache_data) < BaseCaching.MAX_ITEMS:
                self.cache_data[key] = item
            else:
                self.cache_data[key] = item
                keys = list(self.cache_data.keys())
                print("DISCARD: {}".format(keys[0]))
                del self.cache_data[keys[0]]


    def get(self, key):
        """return value in self.cache_data linked to key
        """
        if not key or not self.cache_data.get(key):
            return None
        return self.cache_data.get(key)
