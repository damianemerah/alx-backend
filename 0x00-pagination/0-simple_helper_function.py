#!/usr/binenv python3
'''Task 0's module'''


def index_range(page: int, page_size: int) -> tuple[int, int]:
    '''Return a tuple for start and end index'''
    start = page * page_size - page_size
    end = page * page_size
    return (start, end)
