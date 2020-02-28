class Employee:
    raise_amt = 1.04
    no_of_emps=0

    def __init__(self, name, salary):
        self.name = name
        self.email = name + '@gmail.com'
        self.salary = salary
        Employee.no_of_emps+=1

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amt)

    @classmethod
    def set_raise(cls, amt):
        cls.raise_amt=amt

    def display_emp(self):
        print(f"name:{self.name} email:{self.email} salary:{self.salary} raise:{self.raise_amt}")


class Developer(Employee):

    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def display_emp(self):
        super().display_emp()
        print("lang:",self.language)



class Manager(Employee):

    def __init__(self, name, salary, employees=None):
        super().__init__(name, salary)
        if employees is None:
            self.employees = []
        else:
            self.employees=employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):

        for emp in self.employees:
            emp.display_emp()



dev1 = Developer("raghu", 60000, 'Python')
dev2 = Developer("rahul", 50000, "Embedded C")
dev1.apply_raise()
dev1.display_emp()

emp1 = Employee("Ashu", 45000)
emp1.apply_raise()
mgr = Manager('Raghu', 90000)
mgr.add_emp(emp1)

print("under mgr1:employyee list")
mgr.print_emps()
print(Employee.no_of_emps)
Employee.set_raise(2.7)
print("after raise:")
mgr.print_emps()
print(Employee.no_of_emps)
