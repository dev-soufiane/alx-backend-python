#!/usr/bin/env python3
"""Asynchronous Comprehension."""

from typing import List
import random

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Asynchronously collects 10 random float numbers using async comprehension.

    Returns:
        List[float]: A list of 10 random float numbers.
    """
    result = [i async for i in async_generator()]
    return result
