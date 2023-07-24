#!/usr/bin/env python3
'''chapter 1 getting to know the layput'''

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """ The function """
    end_index: int = page * page_size
    start_index: int = end_index - page_size
    return start_index, end_index
