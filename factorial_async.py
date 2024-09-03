import asyncio
import time
import tool_benchmark as tb

N = 500


# ==== SYNC ============================
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


@tb.benchmark
def run_sync():
    res = list()
    for _ in range(1000):
        res.append(factorial(N))
    # print(f"Factorial of {N} = {res}")


# ==== ASYNC ============================
async def a_factorial(n):
    if n == 0:
        return 1
    else:
        return n * await a_factorial(n - 1)


@tb.async_benchmark
async def loop_factorial():
    tasks = [a_factorial(N) for _ in range(1000)]
    res = await asyncio.gather(*tasks)
    # print(f"Factorial of {N} = {res[0]}")


if __name__ == "__main__":
    run_sync()
    asyncio.run(loop_factorial())

