class Computer:

    def config1(self):
        print("i3,4gb,1tb")

    def config2(self,processor,ram,brand):
        print(f"{processor} {ram} {brand}")

class Computer2:
    count=0
    def __init__(self,cpu,ram,brand):
        self.cpu=cpu
        self.ram=ram
        self.brand=brand
        Computer2.count+=1

    def config(self):
        print(f"{self.cpu} {self.ram} {self.brand}")



com1=Computer()
com1.config1()
com1.config2("i5",4,"hp")
print("using __init__")

com=Computer2("i7","8gb","hp")
com2=Computer2("i5","6gb","lenovo")
com3=Computer2("i3","6gb","dell")
com.config()
com2.config()
com3.config()
print(Computer2.count)

