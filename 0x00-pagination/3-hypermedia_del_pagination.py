#!/usr/bin/env python3
"""
1-simple_pagination.py
"""


import csv
import math
from typing import List, Tuple, Dict


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
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Get page data
        """
        data = self.indexed_dataset()
        assert index is not None and index >= 0 and index <= max(data.keys())
        next_in = None
        lsdata = []
        cnt = 0
        for key, value in data.items():
            if cnt == page_size:
                next_in = key
                break
            if key >= index:
                lsdata.append(value)
                cnt += 1
        data_dict = {
                'index': index,
                'data': lsdata,
                'page_size': len(lsdata),
                'next_index': next_in
                }
        return data_dict
