#!/usr/bin/env python3
"""This is the Annonated function, returns values with appropriate types"""
from typing import Mapping, MutableMapping, Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Ths is the element length"""
    return [(i, len(i)) for i in lst]
