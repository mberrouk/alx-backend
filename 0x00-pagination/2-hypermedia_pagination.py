#!/usr/bin/env python3
"""
1-simple_pagination.py
"""


import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Use the page and page_size to return a tuple of size
    two containing a start index and an end index corresponding
    to the range of indexes to return in a list for those
    particular pagination parameters.
    """

    return ((page - 1) * page_size, ((page - 1) * page_size) + page_size)


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
        """
        Use index_range to find the correct indexes to paginate
        the dataset correctly and return the appropriate page of the dataset.
        """
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0
        start_index, end_index = index_range(page, page_size)
        datas = self.dataset()
        if start_index > len(datas):
            return []
        return datas[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        hypermedia pagination
        """
        page_list = self.get_page(page, page_size)
        datalen = len(self.__dataset)
        total_pages = math.ceil(datalen / page_size)
        s, e = index_range(page, page_size)
        sdict = {
                'page_size': len(page_list),
                'page': page,
                'data': page_list,
                'next_page': page + 1 if datalen > e else None,
                'prev_page': page - 1 if s > 0 else None,
                'total_pages': total_pages
                }
        return sdict
