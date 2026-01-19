from concurrent.futures import ProcessPoolExecutor
import asyncio
import time


def encrypt(data):
    print(f"{data[::-1]}")


async def main():

    loop = asyncio.get_running_loop()
    with ProcessPoolExecutor() as pool:
        response = await loop.run_in_executor(pool, encrypt, "secret_data_1234")
        print(f"{response}")


if __name__ == "__main__":
    asyncio.run(main())