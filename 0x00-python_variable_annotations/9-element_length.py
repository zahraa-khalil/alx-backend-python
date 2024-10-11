#!/usr/bin/env python3
""" Basic Annotations"""

from typing import List, Union, Tuple, Callable, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
