from concurrent.futures import ThreadPoolExecutor
import asyncio
import time


def check_stock(item):
    print(f"Checking {item} in store ....")
    time.sleep(3)
    return f"42 {item} in stock!"


async def main():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, check_stock, "Deodrants")
        print(result)


asyncio.run(main())