#!/usr/bin/env python3
''' Let's duck type an iterable object '''
from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''length with elements in a tuple'''
    return [(i, len(i)) for i in lst]
