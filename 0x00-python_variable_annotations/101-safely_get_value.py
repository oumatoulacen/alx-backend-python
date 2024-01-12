#!/usr/bin/env python3
''' Let's duck type an iterable object '''
from typing import Union, Mapping, Any, TypeVar


T = TypeVar('T')
ret = Union[Any, T]
df = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: df = None) -> ret:
    ''' Get the value of the given key'''
    if key in dct:
        return dct[key]
    else:
        return default
