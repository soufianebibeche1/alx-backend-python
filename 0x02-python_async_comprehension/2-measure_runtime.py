#!/usr/bin/env python3
"""
Measure Runtime
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """
    Measure the total runtime of executing async_comprehension four times in parallel.
    Returns:
        float: The total runtime in seconds.
    """
    start = time.perf_counter()
    await async_comprehension()
    run_time = time.perf_counter() - start
    return run_time
