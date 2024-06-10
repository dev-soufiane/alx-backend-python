#!/usr/bin/env python3
"""New Function from wait_n"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Run n tasks that execute task_wait_random.
    """

    # Create a list of n tasks running task_wait_random
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
