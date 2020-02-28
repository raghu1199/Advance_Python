class Animal:
    def breathe(self):
        print("Breathes oxygen")

    def feed(self):
        print("Eat fruits and vegatables")


class Herbivorous(Animal):

    def feed(self):
       # super().feed() to call parent feed method
        print("eats only plants")

herbi=Herbivorous()
herbi.feed()
