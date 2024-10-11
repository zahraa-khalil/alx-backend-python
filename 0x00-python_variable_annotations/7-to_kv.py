#!/usr/bin/env python3
""" Basic Annotations"""

from typing import List, Union, Tuple


def to_kv(k: str, v: List[Union[int, float]]) -> Tuple[Union[str, float]]:
    """to_kv function"""
    return (k, v ** 2)
