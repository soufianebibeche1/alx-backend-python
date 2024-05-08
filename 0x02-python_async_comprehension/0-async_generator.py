#!/usr/bin/env python3

# 0-async_generator.py

"""Async generator"""

import asyncio
import random


async def async_generator():
    """ asynchronously generate values from 0 - 10 """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
