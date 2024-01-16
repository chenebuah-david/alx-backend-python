#!/usr/bin/env python3
"""This is a coroutine called async_generator that takes no arguments"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    It will create a list of 10 numbers from a 10-number generator
    """
    rslt = [s async for s in async_generator()]
    return rslt
