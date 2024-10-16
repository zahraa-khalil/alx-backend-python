#!/usr/bin/env python3
"""Async Generator"""
import asyncio
import random
from typing import AsyncGenerator

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def async_comprehension():
    random_num = [randomNum async for randomNum in async_generator()]
    return random_num
