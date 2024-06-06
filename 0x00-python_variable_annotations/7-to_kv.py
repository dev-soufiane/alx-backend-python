#!/usr/bin/env python3
"""
Converts a string key and an int or float value into a tuple,
where the second element of the tuple is the square of the int or float value.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Converts 'k' to a string key and 'v' to its square in a tuple."""
    return (k, float(v ** 2))
