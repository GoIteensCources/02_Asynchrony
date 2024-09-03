import asyncio
import time


def benchmark(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        stop = time.time()
        print(f"time {func.__name__}: {stop - start}")
        return result
    return wrapper


def async_benchmark(coro):
    async def wrapper(*args, **kwargs):
        start = asyncio.get_event_loop().time()
        result = await coro(*args, **kwargs)
        stop = asyncio.get_event_loop().time()
        print(f"time {coro.__name__}: {stop - start}")
        return result
    return wrapper
