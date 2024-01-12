#!/usr/bin/env python3
''' Let's duck type an iterable object '''
from typing import Union, Mapping, Any, TypeVar


T = TypeVar('T')
def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    ''' Get the value of the given key'''
    if key in dct:
        return dct[key]
    else:
        return default
