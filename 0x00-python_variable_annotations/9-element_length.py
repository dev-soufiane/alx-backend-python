#!/usr/bin/env python3
"""
Calculates the length of elements in a list.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples with elements from 'lst' and their lengths."""
    return [(i, len(i)) for i in lst]
