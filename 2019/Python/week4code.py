from datetime import date, datetime


foo = datetime.now()
d0 = date(2000, 6, 24)
d1 = date(2019, 3, 7)
delta = d1 - d0
print(foo, delta.days)

