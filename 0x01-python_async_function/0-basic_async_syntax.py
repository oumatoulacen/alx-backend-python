#!/usr/bin/env python3
'''The basics of async'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''Wait for a random number of seconds'''
    num = random.uniform(0, max_delay)
    await asyncio.sleep(num)
    return num
