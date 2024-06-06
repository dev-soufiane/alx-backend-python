#!/usr/bin/env python3
"""
Defines a function to calculate the sum of a list of floats.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculates the sum of a list of floats.

    Parameters:
        input_list (List[float]): The list of floats.

    Returns:
        float: The sum of the floats in the input list.
    """
    return sum(input_list)
