#!/usr/bin/env python3
'''complex types mixed list'''
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''return sum of mixed items'''
    return sum(mxd_lst)
