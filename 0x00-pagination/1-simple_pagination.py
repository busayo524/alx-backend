#!/usr/bin/env python3
"""
This is a simple helper function
"""
import csv
import math
from typing import List, Tuple


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

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
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

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """get page and return list of 10 rows
        """
        assert isinstance(page, int) and page > 0, f"Page index {page} is greater than zero"  # noqa
        assert isinstance(page_size, int) and page_size > 0, f"Page_size index{page_size} is greater than 0"  # noqa
        start_index, end_index = self.index_range(page, page_size)
        dataset = self.dataset()
        if start_index >= len(dataset):
            return []
        else:
            return dataset[start_index:end_index]
