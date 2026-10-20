import asyncio

async def fetch(name: str, delay: float) -> str:
    await asyncio.sleep(delay)
    return f"{name} done"

async def fetch_all(pairs) -> list[str]:
    return await asyncio.gather(
        *(fetch(name, delay) for name, delay in pairs)
    )