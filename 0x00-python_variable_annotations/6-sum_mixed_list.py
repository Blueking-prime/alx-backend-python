#!/usr/bin/env python3
'''a typed list summing function'''
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    '''sums a list of floats'''
    sum: float = 0
    for i in mxd_list:
        sum += i

    return sum
