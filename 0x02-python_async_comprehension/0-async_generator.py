#!/usr/bin/env python3
'''Creates an async genrator'''
import asyncio
from random import uniform
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator:
    '''Yields a random number from 0 - 10 ten times'''
    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
