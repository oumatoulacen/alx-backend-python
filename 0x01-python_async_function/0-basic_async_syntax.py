#!/usr/bin/env python3
'''The basics of async'''
import asyncio
import random, time


async def wait_random(max_delay=10):
    '''Wait for a random number of seconds'''
    num = random.uniform(0, max_delay)
    time.sleep(num)
    return num
