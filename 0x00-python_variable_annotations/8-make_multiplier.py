#!/usr/bin/env python3
"""This is the annotated function, that returns a function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """This returns a function that multiplies a float by a number"""

    def multiplier_function(number: float) -> float:
        """This multiplies a number by a multiplier"""
        return multiplier * number

    return multiplier_function
