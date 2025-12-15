import time
import asyncio
# Synchronous function
def sync_task():
    time.sleep(2)
    print("Sync task completed")

# Asynchronous function
async def async_task():
    await asyncio.sleep(2)
    print("Async task completed")

# Measure synchronous execution time
start_time = time.time()
for _ in range(3):
    sync_task()
print("Total Sync Time:",time.time()-start_time)

# Measure asynchronous execution time
async def main():
    start_time=time.time()
    await asyncio.gather(
        async_task(),
        async_task(),
        async_task()
    )
    print("Total Async Time:",time.time()-start_time)
asyncio.run(main())
