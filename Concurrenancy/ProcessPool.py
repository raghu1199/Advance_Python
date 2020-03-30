from concurrent.futures import ProcessPoolExecutor, as_completed
import time


def do_something(seconds):
    print(f"Sleeping {seconds} secs")
    time.sleep(seconds)
    print(f"Done sleeping {seconds}")


def multi_process():
    with ProcessPoolExecutor() as pool:
        secs = [5, 4, 3, 2, 1]
        results = [pool.submit(do_something, sec) for sec in secs]
        for f in as_completed(results):
            f.result()


if __name__ == "__main__":
    start = time.time()
    multi_process()
    print(f"ProcessPool finished in {time.time() - start} sec")
