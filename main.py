from datetime import datetime as dt


current_time = dt.now().time().strftime('%H:%M:%S')
print(current_time)
a = 1
b = 22
c = 333
result = lambda d: a + b + c