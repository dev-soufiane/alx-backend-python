#!/usr/bin/env python3
"""Execute multiple coroutines at the same time with async"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronously spawns n coroutines to wait for random delays.
    """

    # Generates a random float (random_delay) between 0 and max_delay
    random_delay = random.uniform(0, max_delay)

    # Asynchronously waits for the random delay
    await asyncio.sleep(random_delay)

    # Returns the generated random delay value
    return random_delay
