#!/usr/bin/env python3
"""
function task 3
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Takes an integer max_delay, creates a task wait_random(max_delay)
    """
    return asyncio.create_task(wait_random(max_delay))
