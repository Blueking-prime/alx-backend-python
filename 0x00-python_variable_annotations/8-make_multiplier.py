#!/usr/bin/env python3
'''a typed tuple creation function'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float, float], float]:
    '''creates a multiplier function'''
    def func(x: float, n: float = multiplier) -> float:
        '''multiplies stuff'''
        return x * n
    return func
