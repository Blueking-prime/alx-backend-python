#!/usr/bin/env python3
'''a typed list summing function'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    '''sums a list of floats'''
    sum: float = 0
    for i in input_list:
        sum += i

    return sum
