#!/usr/bin/env python3
"""This contains method that safely gets value from dictionary"""
from typing import Mapping, Any, Sequence, Union, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None
                     ) -> Union[Any, T]:
    """This retrieves a value from a dict using a given key"""
    if key in dct:
        return dct[key]
    else:
        return default
