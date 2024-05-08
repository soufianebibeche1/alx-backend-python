#!/usr/bin/env python3
"""
Async Generator
"""
from asyncio import sleep
from random import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generator that yields a random number between 0 and 
    10 after waiting for 1 second asynchronously.
    """
    for i in range(10):
        await sleep(1)
        yield 10 * random()
