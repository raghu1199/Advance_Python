class UncountableError(ValueError):

    def __init__(self,wrong_value):
        super().__init__(f"Invalid value for n, {wrong_value}. n must be greater than 0")


def count(num):
    if num<1:
        raise UncountableError(num)
    for i in range(0,num+1):
        print(i)

count(-10)