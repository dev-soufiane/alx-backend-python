#!/usr/bin/env python3
"""
Zooms in on a tuple by repeating its elements.

Parameters:
    lst (Tuple): The tuple to zoom in on.
    factor (int): The factor by which to zoom in. Default is 2.

Returns:
    Tuple: The zoomed-in tuple.
"""

from typing import Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> Tuple:
    """Zooms in on a tuple by repeating its elements."""
    zoomed_in: Tuple = tuple(
        item for item in lst
        for i in range(factor)
    )
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)

print(zoom_array.__annotations__)
