#!/usr/bin/env python3
'''Complex types - string and int/float to tuple'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''takes a k:int and v:int/float as arguments and returns a tuple'''
    return k, v ** 2
