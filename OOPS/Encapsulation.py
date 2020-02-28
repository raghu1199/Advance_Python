class Car:
    __maxspeed=0
    __name=""

    def __init__(self):
        self.__updateSoft()
        self.__maxspeed=200
        self.__name="Supercar"

    def drive(self):
        print(f"{self.__name} driving at maxspeed {self.__maxspeed}")

    def __updateSoft(self):

        print("Updating softwares..")

    def setAtrribites(self,maxspeed,name):
        self.__maxspeed=maxspeed
        self.__name=name

    def getAtrribute(self):
        return self.__name,self.__maxspeed


c=Car()
c.drive()
c.setAtrribites(250,"Jaguar")
c.drive()
name,sp=c.getAtrribute()
print(name,sp)
c._Car__updateSoft()


