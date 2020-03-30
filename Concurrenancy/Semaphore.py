from threading import *


class Flight:
    def __init__(self, available_seat):
        self.available_seat = available_seat
        self.lock = Semaphore(2)
        print(self.lock)

    def reserve(self, need_seat):
        self.lock.acquire()
        print(self.lock._value)
        print("Available seats:", self.available_seat)
        if (self.available_seat >= need_seat):
            name = current_thread().name
            print(f"{need_seat} seat is alloted to {name}")
            self.available_seat -= need_seat
        else:
            print("sorry!,All seat has alloted")
        self.lock.release()



f = Flight(2)
t1 = Thread(target=f.reserve, args=[1], name="Raghu")
t2 = Thread(target=f.reserve, args=[1], name="Rahul")
t3 = Thread(target=f.reserve, args=[1], name="Sonam")
t4 = Thread(target=f.reserve, args=[1], name="Ashu")
t1.start()
t2.start()
t3.start(),t4.start()
t1.join(), t2.join(), t3.join(),t4.join()
print("Main Thread")
