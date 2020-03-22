import multiprocessing
import time
from multiprocessing.dummy import freeze_support

start=time.perf_counter()

def do_something(seconds):
    print(f"Sleeping {seconds} seconds..")
    time.sleep(seconds)
    return f"Done sleeping for {seconds} secs"


def multi_process():
    processes = []
    for _ in range(10):
        p = multiprocessing.Process(target=do_something, args=[1.5])
        p.start()
        processes.append(p)

    for pr in processes:
        pr.join()

def process():
    p1 = multiprocessing.Process(target=do_something, args=[1.5])
    p2 = multiprocessing.Process(target=do_something, args=[2.5])
    p1.start()
    p2.start()
    p1.join()
    p2.join()


if __name__=="__main__":
    #process()            #total time=2.7
    multi_process()       #10 process time 2.07
    finish = time.perf_counter()
    print(f"Finished in {round(finish - start, 2)} secs")


