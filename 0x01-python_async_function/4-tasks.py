#!/usr/bin/env python3
'''More work with tasks'''
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''spawn wait_random n times'''
    delay_list: List = []
    ret_list: List[float] = []

    # Create new task for every time wait_random needs to be run
    for _ in range(n):
        x = task_wait_random(max_delay)
        delay_list.append(x)

    # Collates tasks as they are completed
    for task in asyncio.as_completed(delay_list):
        ret_list.append(await task)

    return ret_list
