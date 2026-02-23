#From a list of numbers: Filter even numbers Square them Find their sum
from functools import reduce

nums = [1, 2, 3, 4, 5, 6]
even = list(filter(lambda x :x%2==0,nums))
print(even)

print(reduce(lambda x,y: x+y,nums))

square = list(map(lambda x :x*x,nums))
print(square)
2.
salaries = [25000, 40000, 32000, 18000]
salary = list(filter(lambda x :x > 30000,salaries))
print(salary)

#add hike
hike = list(map(lambda x : x+(x*(10/100)),salary))
print(hike)

#total payout

total_payout = reduce(lambda a,b :a+b,salaries)
print(total_payout)



