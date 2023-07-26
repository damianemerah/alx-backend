#!/usr/bin/env python3
'''Task 2's module'''


from typing import List
import math
import csv


def index_range(page: int, page_size: int) -> tuple[int, int]:
    '''Return a tuple for start and end index'''
    if page and page_size > 1:
        start = page * page_size - page_size
        end = page * page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''Return paginated list'''
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        if start > len(self.dataset()):
            return []
        return self.dataset()[start: end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''Return paginated list'''
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        data = self.dataset()

        if start > data:
            return {}

        total_pages = len(len(self.dataset()))
        prev_page = page - 1 if page > 1 else None,
        next_page = page + 1 if page < total_pages else None

        dict_ = {
            "page_size": page_size,
            "page": page,
            'data': data[start: end],
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }

        return dict_
