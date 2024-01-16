#!/usr/bin/env python3

"""This is a coroutine that will execute async_comprehension four times"""

import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    This returns the total runtime for 4 asynchronous
    comprehension running in parallel
    """
    t_start = time.perf_counter()
    task = [async_comprehension() for s in range(4)]
    await asyncio.gather(*task)
    t_end = time.perf_counter()
    return (t_end - t_start)
