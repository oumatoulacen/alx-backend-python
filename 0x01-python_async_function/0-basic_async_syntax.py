#!/usr/bin/env python3
'''The basics of async'''
import asyncio
import random


async def wait_random(max_delay=10):
    '''Wait for a random number of seconds'''
    time = random.uniform(0, max_delay)
    return time
