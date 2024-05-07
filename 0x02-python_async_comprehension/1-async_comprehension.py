#!/usr/bin/env python3
"""
Async Comprehension
"""
import asyncio

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension():
    """
    Collects 10 random numbers using async comprehensions over async_generator.
    Returns:
        List[float]: A list of 10 random numbers.
    """
    return [i async for i in async_generator()]
