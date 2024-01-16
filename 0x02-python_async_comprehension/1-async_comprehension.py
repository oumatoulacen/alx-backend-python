#!/usr/bin/env python3
''''async  comprehension'''
from typing import Generator, List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[Generator[float, None, None]]:
    '''async_comprehension function'''
    return [i async for i in async_generator()]
