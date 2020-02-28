class Duck:
    def quack(self):
        print("quack")
    def fly(self):
        print("Flap,flap")


class Person:

    def quack(self):
        print("quacking like duck")

    def fly(self):
        print("Flapping his arms!")

def quack_and_fly_Nonpyhtonic(thing):
    if isinstance(thing,Duck):
        thing.quack()
        thing.fly()
    else:
        print("thing is not instance of Duck")

def quack_and_fly_pythonic(thing):
    try:
        thing.quack()
        thing.fly()
        thing.bark()
    except AttributeError as e:
        print(e)

d=Duck()
p=Person()
quack_and_fly_Nonpyhtonic(d)
print("Instance of Person with same methods")
quack_and_fly_Nonpyhtonic(p)
print("pythonic way")
quack_and_fly_pythonic(d)
print("Different object bt with same object")
quack_and_fly_pythonic(p)
