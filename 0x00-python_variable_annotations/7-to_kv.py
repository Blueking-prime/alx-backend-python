#!/usr/bin/env python3
'''a typed tuple creation function'''
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''creates a tuple'''
    return (k, v ** 2)
