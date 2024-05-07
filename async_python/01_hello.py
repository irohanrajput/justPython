import asyncio
import asyncio

async def greet(name: str):
    print("Hello", name)
    await asyncio.sleep(1)
    print("Goodbye", name)
    
async def main():
    await asyncio.gather(
    greet("Alice"),
    greet("Bob"),
    greet("Charlie")
    )
asyncio.run(main())