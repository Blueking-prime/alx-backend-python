#!/usr/bin/env python3
'''a typed tuple creation function'''
from typing import Iterable, List, Tuple


def element_length(lst: Iterable) -> List:
    return [(i, len(i)) for i in lst]
