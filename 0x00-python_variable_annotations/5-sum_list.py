#!/usr/bin/env python3
"""This contains a function that sums a list of floats"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """This returns list sum as a float
    """
    if input_list is None:
        return 0
    else:
        return sum(input_list)
