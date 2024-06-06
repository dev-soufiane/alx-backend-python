#!/usr/bin/env python3
"""
Defines a function to create a multiplier function.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Creates a function that multiplies a float by a given multiplier."""
    def multiplier_function(x: float) -> float:
        """Multiplies a float by the given multiplier."""
        return x * multiplier
    return multiplier_function
