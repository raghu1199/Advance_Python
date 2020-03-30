import time
import asyncio


async def count():
    print("Started One..")
    await asyncio.sleep(1)
    print("Done sleep Two..")


async def main():
    await asyncio.gather(count(), count(), count())

if __name__=="__main__":
    start=time.time()
    asyncio.run(main())
    print(f"Finished {time.time()-start} secs..")
    