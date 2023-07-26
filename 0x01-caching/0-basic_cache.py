#!/usr/bin/env python3
'''Task 0's module'''
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''A caching system'''

    def put(self, key, item):
        '''Assigns key , item to self.cache_data (dict)'''
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        '''Returns item for key'''
        return self.cache_data.get(key, None)
