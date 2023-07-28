#!/usr/binenv python3
'''Task 0's module'''
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''Return a tuple for start and end index'''
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
