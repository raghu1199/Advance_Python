from threading import Thread

class Hotel:
    def __init__(self,table):
        self.table=table

    def food(self):
        for i in range(1,6):
            print(self.table,i)

h1=Hotel("take order from table ")
h2=Hotel("serve order to table ")
t=Thread(target=h1.food)
t2=Thread(target=h2.food)
t.start()
t2.start()
t.join()
t2.join()
