import asyncio


async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")


async def main():
    await asyncio.gather(count(), count(), count())


# 'await' outside function
# await asyncio.run(main())


#ok
# asyncio.run(main())


# RuntimeWarning: coroutine 'count' was never awaited
# count()

#ok
# asyncio.run(count())
