from datetime import datetime as dt


current_time = dt.now().time().strftime('%H:%M:%S')
print(current_time)
a = 1
b = 22
c = 333
result = lambda: a + b + c
print(result())


class Person:
    pass

man = Person()
woman = Person()