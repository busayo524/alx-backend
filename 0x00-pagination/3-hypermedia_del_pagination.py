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
        """geting hypermedia data with index and page size
        """
        assert isinstance(index, int) and index >= 0, f"index {index} is valid"  # noqa
        assert isinstance(page_size, int) and page_size > 0, f"page_size {page_size} is valid"  # noqa

        data = self.indexed_dataset()
        data_length = len(data)

        assert index < data_length, f"this is valid"

        current_index = index
        line_count = 0
        data_list = []

        while line_count < page_size and current_index < data_length:
            line = data.get(current_index)
            if line is None:
                line_count += 1
            else:
                data_list.append(line)
                line_count += 1
            current_index + 1

        next_index = current_index if current_index < data_length else None

        return {
                "index": index,
                "next_index": next_index,
                "page_size": len(data_list),
                "data": data_list
            }
