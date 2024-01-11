#!/usr/bin/env python3
'''functions'''
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''multiplier'''
    def fun (multiplier: float) -> float:
        return multiplier * multiplier
    return fun
