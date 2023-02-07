#!/usr/bin/env python3
'''Measures an async comprehendor'''
import asyncio
from time import perf_counter
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''Measures execution time for an async function'''
    s = perf_counter()
    task_list = [asyncio.create_task(async_comprehension()) for _ in range(4)]
    await asyncio.gather(*task_list)
    return perf_counter() - s
