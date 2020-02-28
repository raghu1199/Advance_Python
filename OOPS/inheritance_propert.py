class Student:
    def __init__(self,name,school):
        self.name=name
        self.school=school
        self.marks=[]

    def average(self):
        return sum(self.marks)/len(self.marks)


class WorkingStudent(Student):

    def __init__(self,name,school,salary):
        super().__init__(name,school)
        self.salary = salary

    @property
    def weekly_salary(self):
        return self.salary*37.5

raghu=WorkingStudent("Raghu","GEC-GN",15.5)
raghu.marks.append(87)
raghu.marks.append(89)
print(raghu.average())
print(raghu.weekly_salary)

