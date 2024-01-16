#!/usr/bin/env python3

"""This is a python module to loop 10 times"""
import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[float, None, None]:
    """
    It will generate a sequence of 10 numbers
    """
    for s in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
