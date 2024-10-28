#!/usr/bin/env python3
"""
This is a simple helper function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    helper function

    Args:
        page(int): first index as 1
        page_size: this is the size of each page
    Return:
        Tuple[int, int]: this returns tuple with start and end index
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
