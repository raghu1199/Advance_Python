def countdown(n):
    while n > 0:
        yield n
        n -= 1
        print("after yield:", n)


c = countdown(10)
print(c)
print(next(c))
print(next(c))

from collections import deque

# friends = deque(('ROLF', 'JOSE', 'ANA', 'RAHUL'))
friends = ["RAGHU", "RAHUL", "ASHU", "RONAK", "MILAN", "JAYANT", "VIKAS"]


def get_friend():
    yield from friends


def greet(generator_obj):
    while True:
        try:
            friend = next(generator_obj)
            yield f"HEllo {friend}"
        except StopIteration:
            print("Friends list empty..")
            break


friends_gen = get_friend()
print(friends_gen)
g = greet(friends_gen)
print(next(g))
print("now using for loop")
for friend in g:
    print(friend)

