class Student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
        self.lap=self.Laptop()

    def show(self):
        print(self.name,self.roll)
        self.lap.show()


    class Laptop:
        def __init__(self):
            self.brand="HP"
            self.cpu="i7"
            self.ram=8

        def show(self):
            print(self.brand,self.cpu,self.ram)


s1=Student("RAghu",47)
s2=Student("Rahul",40)
s1.show()
s1.lap.brand="lenovo"
s1.lap.ram=12
s1.show()
