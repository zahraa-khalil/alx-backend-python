#!/usr/bin/env python3
"""Async Generator"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """coroutine called async_generator"""
    for i in range(10):
        await asyncio.sleep(1)
        randomNum = random.uniform(0, 10)
        yield randomNum
