from threading import Thread, current_thread


class Flight:
    def __init__(self, available_seat):
        self.available_seat = available_seat

    def reserve(self,need_seat):
        print("Availabe seat:",self.available_seat)

        if(self.available_seat >= need_seat):
            name=current_thread().name
            print(f"{need_seat} seat is alloted to {name}")
            self.available_seat-=need_seat
        else:
            print("Sorry! All seat is reserved..")

f=Flight(2)
t1=Thread(target=f.reserve,args=[1],name="Rahul")
t2=Thread(target=f.reserve,args=[1],name="Raghu")
t3=Thread(target=f.reserve,args=[1],name="sonam")
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
print("main Thread")


