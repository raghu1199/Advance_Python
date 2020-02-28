class Student:
    def __init__(self, name, new_grades):
        self.name = name
        self.grades = new_grades

    def average(self):
        return sum(self.grades) / len(self.grades)

st1=Student("RAHUL MC",[60,55,34,21,17])
st2=Student("RAGHU HERO",[96,98,97,90,93])
print(st1.name,st1.grades)
print(st2.name,st2.grades)
print(st1.average())
print(st2.average())

def average1(student):
    return sum(student.grades)/len(student.grades)

print("average by separate :",average1(st1))