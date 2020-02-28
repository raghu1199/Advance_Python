class Student:
    roll = 0
    income_rate = 1.10

    def __init__(self, name, std, income):
        self.avg=0
        Student.roll += 1
        self.name = name
        self.std = std
        self.id = self.name + '.' + str(Student.roll) + '@'
        self.income = income

    def marks(self,m1,m2,m3):
        self.avg=int(m1+m2+m3)/3

    def apply_raise(self):
        self.income=int(self.income*Student.income_rate)

    def display_student(self):
        print(self.name,self.id,'income:',self.income,'avg marks:',self.avg)


class Teacher(Student):
    count_teacher=0

    def __init__(self,name,std,income):
        super().__init__(name,std,income)
        Teacher.count_teacher+=1
        self.tid=self.name+'@'+str(Teacher.count_teacher)

    def display_teacher(self):
        print(self.name,self.tid,self.std,self.income)


class Principal(Student):

    def __init__(self,name,std,income,students=None,teachers=None):
        super().__init__(name,std,income)
        if students is None:
            self.students=[]
        else:
            self.students=students

        if teachers is None:
            self.teachers=[]
        else:
            self.teachers=teachers

    def add_student(self,student):
        if student not in self.students:
            self.students.append(student)

    def add_teacher(self,teacher):
        if teacher not in self.teachers:
            self.teachers.append(teacher)

    def remove_student(self,student):
        if student in self.students:
            self.students.remove(student)

    def remove_teacher(self,teacher):
        if teacher in self.teachers:
            self.teachers.remove(teacher)

    def print_students(self):
        for st in self.students:
            st.display_student()

    def print_teachers(self):
        for tch in self.teachers:
            tch.display_teacher()


s1=Student("Raghu",'12th',50000)
s1.marks(89,85,96)
s2=Student("Rahul",'11th',40000)
s2.marks(67,75,66)
s3=Student("Ashu",'10th',35000)
s3.marks(77,78,85)
t1=Teacher("NVP SIR",'12th',66000)
t2=Teacher('KK ACHARYA','11th',55000)
p=Principal('AARTI BOKADE','12th',78000)
s1.display_student()
p.add_student(s1)
p.add_student(s2)
p.add_student(s3)
p.add_teacher(t1)
p.add_teacher(t2)
print("STUDENTS LIST:")
p.print_students()
print("TEACHERS LIST:")
p.print_teachers()





