#!/usr/bin/env python3
"""0-basic_async_syntax.py"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay
    (included and float value) seconds and
    eventually returns it
    """
    r_delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(r_delay)
    return r_delay
