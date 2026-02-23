#Write a Python function to sum all the numbers in a list
def sum(list):
    sum=0
    for i in list:
        sum+=i
    return sum
values = sum([10,20,30,40])
print(values)
#Write a Python function to find the maximum of three numbers.
def maximum(a,b,c):
    if a > b:
        return a
    elif b > c:
        return b
    else:
        return c
values = maximum(10,20,30)
print(values)
