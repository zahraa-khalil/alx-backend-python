#!/usr/bin/env python3
"""Async Generator"""
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """coroutine will collect 10 random numbers & return the 10 random numbers"""
    random_num = [randomNum async for randomNum in async_generator()]
    return random_num
