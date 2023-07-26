#!/usr/bin/env python3
'''Task 1's module'''
from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    '''FIFO caching system'''

    def __init__(self):
        '''Initialize the cache'''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        ''''Adds item to cache'''
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_item, _ = self.cache_data.popitem(last=False)
            print(f'DISCARD: {first_item}')

    def get(self, key):
        '''Gets item from cache'''
        return self.cache_data.get(key, None)
