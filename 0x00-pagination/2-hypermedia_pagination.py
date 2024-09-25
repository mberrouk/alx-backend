#!/usr/bin/env python3
"""
Implementing Simple Pagination.
"""

import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Found a start index and end index.
    """
    start_index = (page - 1) * page_size
    end_index = ((page - 1) * page_size) + page_size
    return (start_index, end_index)


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
        """ Retrive data
        """
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0
        beg, end = index_range(page, page_size)
        data = self.dataset()
        if beg > len(data) or end > len(data):
            return []
        return data[beg:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict[str, str]:
        """ Hypermedia pagination
        """
        data = self.get_page(page, page_size)
        beg, end = index_range(page, page_size)

        dictData = {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if end < len(self.__dataset) else None,
            "prev_page": page - 1 if beg > 0 else None,
            "total_pages": math.ceil(len(self.__dataset) / page_size)
        }
        return dictData
