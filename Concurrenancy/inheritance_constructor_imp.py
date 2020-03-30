class Myclass():
    def __init__(self):
        self.a=10
        self.b=20
    def printValue(self):
        print(self.a,self.b)

class child(Myclass):

    def __init__(self):
        Myclass.__init__(self)    #if parent constructor not called then it gives Error
        #super().__init__()
        self.c=30

    def display(self):
        super().printValue()

c=child()
c.display()