#filter positive number
from functools import reduce

nums = [-5, 10, -3, 7, 0, 2]
positive = list(filter(lambda p : p>0, nums))
print(positive)

#Filter non-empty strings

data = ["hello", "", "world", "", "python"]
non_emptystring = list(filter(lambda s: s !="",data))
print(non_emptystring)

#even numbers
num = [1,2,3,4,5,6]
even = list(filter(lambda x : x%2==0,num))
print(even)

#lambda expression
add = lambda a,b:a+b
print(add(5,6))

#square of the number
square = lambda a :a*a
print(square(6))



# Using the reduce function to sum of the numbers
nums = [10,20,30,40,50]
print(reduce(lambda a,b:a+b,nums))

#multiply
print(reduce(lambda a,b:a*b,nums))

#maximum number
print(reduce(lambda a,b:max(a,b),nums))

#minimum number
print(reduce(lambda a,b:min(a,b),nums))


#map function to the square of the number
nums = [10,20,30,40,50]
square =list (map(lambda a :a*a,nums))
print(square)

#dorting in lambda
data = [(1,2),(3,4),(5,6)]
sorted = sorted(data,key = lambda x :x[1])
print(sorted)

data = {"a":50,"b":78,"c":90}
sorted = dict(sorted(data.items(),key = lambda x :x[1]))
print(sorted)

