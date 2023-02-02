#!/usr/bin/env python3
'''a typed tuple creation function'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''creates a multiplier function'''
    def func(x: float) -> float:
        '''multiplies stuff'''
        return x * multiplier
    return func
