#Write a Python program to sort a list of tuples using Lambda
list = [(1,2),(5,90),(10,45)]
sort = sorted(list,key = lambda l : l[1])
print(sort)
#Write a Python program to extract year, month, date and time using Lambda
from datetime import datetime
now = datetime.now()

year  = (lambda d:d.year)(now)
month = (lambda d:d.month)(now)
day  = (lambda d:d.day)(now)
time  = (lambda d:d.strftime("%H:%M:%S"))(now)
print(year)
print(month)
print(day)
print(time)


#Write a Python script to concatenate the following dictionaries to create a new one.
d1 = {"a":1,"b":2,"c":3}
d2 = {"d":4,"e":5,"f":6}
new={}
new.update(d1)
new.update(d2)
print(new)



