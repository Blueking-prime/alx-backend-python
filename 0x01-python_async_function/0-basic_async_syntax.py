#!/usr/bin/env python3
'''Basic async function'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''waits for a random amount of time and returns a value'''
    delay: float = random.uniform(0, float(max_delay))
    await asyncio.sleep(delay)
    return delay
