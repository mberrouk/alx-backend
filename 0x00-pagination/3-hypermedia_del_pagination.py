#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


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
        """
        """
        self.indexed_dataset()
        if self.__indexed_dataset is None:
            return {}           # TODO

        assert index is not None and index >= 0 and index < len(self.__indexed_dataset)

        data_list = []
        page_size = 0
        keys = list(self.__indexed_dataset.keys())
        if index in keys:
            print("IF")
            s = keys.index(index)
            print(s)
            # print(keys)
            data_list = [self.__indexed_dataset[k] for k in keys[s:s + page_size]]

        print(data_list)
        return {
            "index": index,
            "next_index": 10,
            "page_size": 210,
            "data": 10 
        }

server = Server()

try:
    server.get_hyper_index(1);
except AssertionError:
    print("ERROR")
