#!/usr/bin/env python3
'''regular function that returns an asyncio.Task '''
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''return an asyncio Task that will wait for the given delay'''
    return asyncio.Task(wait_random(max_delay))
