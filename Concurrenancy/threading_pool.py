import time
from threading import Thread
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed

start = time.perf_counter()


def do_something(seconds):
    print(f"Sleeping {seconds}")
    time.sleep(seconds)
    print(f"Done sleeping {seconds}")


threads = []
for _ in range(10):
    thread = Thread(target=do_something, args=[2])
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

finish=time.perf_counter()
print(f"Threadin Finished in {round(finish-start)} secs")

print("Using ThreadPoolExecutor submit...")
start=time.perf_counter()
with ThreadPoolExecutor() as pool:
    secs=[5,4,3,2,1]
    results=[pool.submit(do_something,sec) for sec in secs]
    for f in as_completed(results):
        f.result()
finish=time.perf_counter()
print(f"PoolExecutor Finished in {round(finish-start)} secs")

print("Using ThreadPoolExecutor with map...")
start=time.perf_counter()
with ThreadPoolExecutor() as pool:
    secs=[5,4,3,2,1]
    results=pool.map(do_something,secs)
finish=time.perf_counter()
print(f"PoolExecutor with map Finished in {round(finish-start)} secs")
