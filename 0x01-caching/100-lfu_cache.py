#!/usr/bin/env python3
'''Least frequently used caching module'''
from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    '''Least frequently used cache class'''

    def __init__(self):
        '''Initialize cache'''
        super().__init__()
        self.cache_data = OrderedDict()
        self.frequency = OrderedDict()

    def get_lru(self):
        '''Gets least-recently used or least-frequently used'''
        lru = min(self.frequency.values())
        key = [key for key, freq in self.frequency.items() if freq == lru]
        return key

    def discard_lru(self):
        '''Discard lfu and lru'''
        keys = self.get_lru()
        self.frequency.pop(keys[0])
        self.cache_data.pop(keys[0])
        return keys[0]

    def put(self, key, item):
        '''Insert item to cache_data'''

        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS and key not in self.cache_data:
            deleted_key = self.discard_lru()
            print(f'DISCARD: {deleted_key}')

        if key in self.frequency:
            new_key = self.frequency[key]
            self.frequency.pop(key)
            self.frequency[key] = new_key + 1
        else:
            self.frequency[key] = 1
        self.cache_data[key] = item

    def get(self, key):
        '''Returns item matching key in cache'''
        if key in self.cache_data:
            self.frequency[key] += 1
        return self.cache_data.get(key, None)
