#!/usr/bin/env python3
"""Creates a simple helper function"""


def index_range(page, page_size) -> tuple:
    """Returns the particular pagination parameters"""
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
