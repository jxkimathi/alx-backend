#!/usr/bin/env python3
"""Uses index_range to find the correct indexes to paginate"""
import csv
import math
from typing import List
from typing import Dict
from typing import Union


def index_range(page, page_size) -> tuple:
    """Returns the particular pagination parameters"""
    start = (page - 1) * page_size
    end = start + page_size
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
        """Gets the page presented"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        if page <= 0 and page_size <= 0:
            return []
        start, end = index_range(page, page_size)
        return self.dataset()[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str,
                                                                    Union[int, List[List], None]]:
        """Returns a dictionary with hypermedia pagination information"""
        dataset_page = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            'page_size': len(dataset_page),
            'page': page,
            'data': dataset_page,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
