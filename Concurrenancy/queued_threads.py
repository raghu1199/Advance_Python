import time
import random
import queue
from threading import Thread

counter = 0
job_queue = queue.Queue()
counter_queue = queue.Queue()


def inc_manager():
    global counter
    while True:
        increment = counter_queue.get()
        time.sleep(random.random())
        old_counter = counter
        counter = old_counter + increment
        time.sleep(random.random())
        job_queue.put((f"{counter}","---"),)
        time.sleep(random.random())
        counter_queue.task_done()


def print_manager():
    while True:
        for line in job_queue.get():
            print(line)
            time.sleep(random.random())
        job_queue.task_done()


def inc_counter():
    counter_queue.put(1)
    time.sleep(random.random())


Thread(target=inc_manager,daemon=True).start()
Thread(target=print_manager,daemon=True).start()
worker_threads=[Thread(target=inc_counter) for thread in range(10)]

for thread in worker_threads:
    time.sleep(random.random())
    thread.start()
for thread in worker_threads:
    thread.join()
counter_queue.join()
job_queue.join()


