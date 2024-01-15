#!/usr/bin/env python3
'''The basics of async'''
import asyncio
import random


async def wait_random(max_delay=10):
    '''Wait for a random number of seconds'''
    num = random.uniform(0, max_delay + 1)
    await asyncio.sleep(num)
    return num
