import time
from multiprocessing import Process


def ask_user():
    start = time.time()
    user_input = input("enter your name:")
    greet = f"hello,{user_input}"
    print(greet)
    print(f"ask_user,{time.time() - start} sec")


def complex_calc():
    start = time.time()
    print("started calc..")
    [x ** 2 for x in range(20000000)]
    print(f"complex_calc,{time.time() - start}")


def single_process():
    print("single process..")
    start = time.time()
    ask_user()
    complex_calc()
    print(f"single process {time.time() - start}")


def without_io():
    print("CPU PROCESS WITHOUT USER IO..")
    start = time.time()
    p1 = Process(target=complex_calc)
    p1.start()
    ask_user()
    p1.join()
    print(f"Two procees without user io {time.time() - start}")

def with_io():
    print("CPU PROCESS WITH USER IO..")
    start = time.time()
    p1 = Process(target=complex_calc)
    p2=Process(target=ask_user)
    p1.start()
    p2.start()
    p2.join()
    p1.join()
    print(f"Two procees with user io {time.time() - start}")


if __name__ == "__main__":
    single_process()
    without_io()
    with_io()
