class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def __add__(self, other):
        a=self.m1 + other.m1
        b=self.m2 + other.m2

        s3=Student(a, b)
        return s3

    def __str__(self):
        return f"({self.m1}, {self.m2})"

    def __gt__(self, other):
        r1=self.m1+self.m2
        r2=other.m1+other.m2

        if r1>r2:
            return True
        else:
            return False

s1=Student(20,30)
s2=Student(40,50)
res=s1+s2
print(s1,s2)
print(res)
if s1>s2:
    print("S1 wins")
else:
    print("S2 wins")