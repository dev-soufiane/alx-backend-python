#!/usr/bin/env python3
"""Parallel Comprehensions Runtime."""

import asyncio
from time import perf_counter

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the execution time of async_comprehension()
    run four times in parallel.
    """
    starts = perf_counter()
    # Run async_comprehension four times in parallel using asyncio.gather()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    ends = perf_counter()
    return ends - starts
