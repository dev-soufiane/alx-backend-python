#!/usr/bin/env python3
"""Regular Function"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio.Task to run the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
