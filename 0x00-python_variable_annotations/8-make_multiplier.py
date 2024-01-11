#!/usr/bin/env python3
'''functions'''
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''multiplier'''
    def fun (x) -> float:
        return x * multiplier
    return fun
