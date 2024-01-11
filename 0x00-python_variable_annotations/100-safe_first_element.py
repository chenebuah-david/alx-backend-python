#!/usr/bin/env python3
"""This is the duck typing - first element of a sequence"""
from typing import Any, Union, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """This retrieves the first element of a sequence if it exists"""
    if lst:
        return lst[0]
    else:
        return None
