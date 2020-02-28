class Duck:
    def fly(self):
        print("Duck flying")
class Airplane:
    def fly(self):
        print("Airplane Flying")
class Whale:
    def swim(self):
        print("Whale swimms")


for item in Duck(),Airplane(),Whale():
    item.fly()
