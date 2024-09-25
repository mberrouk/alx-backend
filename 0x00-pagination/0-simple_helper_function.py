#!/usr/bin/env python3
"""
Implementing Simple Pagination.
"""


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """
    Found a start index and end index.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
