import asyncio


async def brew_chai(name):
    print(f"Brewing {name}...")
    await asyncio.sleep(2)
    print(f"{name} is ready!")


async def main():
    await asyncio.gather(
        brew_chai("Lemon Chai"),
        brew_chai("Ginger Chai"),
        brew_chai("Cardamom Chai"),
    )


asyncio.run(main())