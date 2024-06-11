#!/usr/bin/env python3
"""Asynchronous Random Number Generator"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronously generates random floating-point numbers between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)  # Wait asynchronously for 1 second
        yield random.uniform(0, 10)  # Generate a random float between 0 and 10


async def print_yielded_values():
    """
    Asynchronously prints the values yielded by the async generator.
    """
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)

asyncio.run(print_yielded_values())
