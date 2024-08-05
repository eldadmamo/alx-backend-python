#!/usr/bin/env python3
"""
execute multiple coroutines same time async
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    returns list of all in ascending order
    """
    c_routines = [wait_random(max_delay) for _ in range(n)]
    return [await delay for delay in asyncio.as_completed(c_routines)]
