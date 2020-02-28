class Employee:
    emps=0
    raise_amt=1.5

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.emps+=1

    def info(self):
        print(self.name," ",self.salary," ",self.raise_amt)

    def apply_raise(self):
        self.salary=int(self.salary*self.raise_amt)

    @classmethod
    def set_raise(cls,amt):
        cls.raise_amt=amt
    @classmethod
    def from_string(cls,emp_str):
        name,pay=emp_str.split("-")
        pay=int(pay)
        return cls(name,pay)

emp_str="Raghvendra-70000"
new_emp=Employee.from_string(emp_str)
new_emp.info()

emp1=Employee("raghu",50000)
emp2=Employee("rahul",60000)
emp1.info()
emp2.info()
print("applying raise to emp1")
#emp1.raise_amt=1.10
emp1.apply_raise()
emp1.info()
emp2.info()
print("raising through class method")
Employee.set_raise(2.5)
emp1.apply_raise()
emp2.apply_raise()
emp1.info()
emp2.info()
#emp1.apply_raise()
#emp1.info()
