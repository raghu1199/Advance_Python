from threading import Thread
class Mythread(Thread):
    def __init__(self,a):
        super().__init__()
        print("Child Thread Constructor:",a)

    def run(self):
        for i in range(5):
            print("Child overrided  run() method.. ")

t=Mythread(10)
t.start()
t.join()
for i in range(5):
    print("Main Thread..")
