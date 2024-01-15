#!/usr/bin/env python3
""" This is the asynchronous basics """

from asyncio import Task, create_task

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """This takes max_delay as an argument and return asyncio.Task"""
    task = create_task(wait_random(max_delay))
    return task
