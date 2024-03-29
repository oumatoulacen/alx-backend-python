#!/usr/bin/env python3
'''Let's execute multiple coroutines at the same time with async'''
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''spawn wait_random n times with the specified max_delay'''
    tasks = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    # u might want to use as_complited from asyncio to sort the results
    return sorted(results)
