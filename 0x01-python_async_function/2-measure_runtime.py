#!/usr/bin/env python3
'''Measure the runtime'''
import asyncio
import time
from importlib import import_module


wait_n = import_module('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''Measure the runtime'''
    start = time.perf_counter()
    # the asychronous function should be called by the asyncio.run
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    total_time = end - start
    return total_time / n
