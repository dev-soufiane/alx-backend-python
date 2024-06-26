#!/usr/bin/env python3
"""Adds type annotations to a function's parameters and return values."""
from typing import Mapping, Any, Union, TypeVar, Optional

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default:
                     Optional[T] = None) -> Union[Any, T]:
    """Safely retrieves a value from a dictionary."""
    if key in dct:
        return dct[key]
    else:
        return default
