import random
import time
from threading import Thread

counter = 0


def inc_counter():
    global counter
    time.sleep(random.random())
    counter += 1
    time.sleep(random.random())
    print(f"New counter:{counter}...")
    time.sleep(random.random())


threads=[]
for x in range(10):
    t = Thread(target=inc_counter)
    time.sleep(random.random())
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()


