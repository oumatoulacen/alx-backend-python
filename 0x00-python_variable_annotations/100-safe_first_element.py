#!/usr/bin/env python3
'''  Duck typing - first element of a sequence '''
from typing import Sequence, Union, Any


# The types of the elements of the input are not known
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''safe_first_element'''
    if lst:
        return lst[0]
    else:
        return None
