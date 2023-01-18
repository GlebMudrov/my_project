from datetime import datetime as dt


current_time = dt.now().time().strftime('%H:%M:%S')
print(current_time)
a = 1
b = 22
c = 333
result = lambda: a + b + c
print(result())


class PowerMixin:
    power = 1000000


class Person:
    pass


class Superman(Person, PowerMixin):
    pass

man = Person()
woman = Person()
clark = Superman()