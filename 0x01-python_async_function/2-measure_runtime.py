#!/usr/bin/env python3
"""Runtime Measurement"""

from time import perf_counter
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure time for wait_n(n, max_delay) and return average time per n.
    """

    # Start time measurement
    t1 = perf_counter()

    # Run wait_n and measure elapsed time
    asyncio.run(wait_n(n, max_delay))
    t2 = perf_counter() - t1

    # Return average time per n
    return t2 / n
