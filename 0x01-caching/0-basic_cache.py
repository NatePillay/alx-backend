#!/usr/bin/python3
'''0-main task'''
BaseCaching = __import__('base_caching').BaseCaching

class BasicCache(BaseCaching):
    '''function basic cache inherits from base'''
    def __init__(self):
        """ Initiliaze
        """
        super().__init__()

    def put(self, key, item):
        '''assign item value for given key in cache'''
        if key is not None or item is not None:
            self.cache_data[key] = item

    def get(self, key):
        if not key or not self.cache_data.get(key):
            return None
        return self.cache_data.get(key)
