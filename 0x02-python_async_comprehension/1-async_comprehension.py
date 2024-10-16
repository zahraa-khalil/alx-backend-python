#!/usr/bin/env python3
"""Async Generator"""
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    random_num = [randomNum async for randomNum in async_generator()]
    return random_num
