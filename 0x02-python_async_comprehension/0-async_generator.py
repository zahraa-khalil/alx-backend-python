#!/usr/bin/env python3
"""Async Generator"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """coroutine called async_generator"""
    for _ in range(0, 10):
        await asyncio.sleep(1)
        randomNum = random.uniform(0, 10)
        yield randomNum
