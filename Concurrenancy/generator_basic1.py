
def numgen(n):
    number=yield
    while number<n:
        yield number
        number+=1


g=numgen(10)
g.send(None)
print(g.send(6))
print(next(g))
print(next(g))

