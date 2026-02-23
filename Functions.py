def printdata():
    print("hi")
printdata()


def printdata(name):
    print("hello",name)
printdata("sunil")
printdata("varsha")

def squ(num):
    result=num*num
    return result
print(squ(6))

def fun_pass():
    pass
fun_pass()

#multiple values return
def cal(a,b):
    return a+b,a-b,a*b
add,sub,mul = cal(15,10)
print(add)
print(sub)
print(mul)

#function calling another function
def areaofrect(len,width):
    return len * width
def areaofsqu(side):
    return side * side
value = areaofrect(4,5)
squ = areaofsqu(value)
print(squ)

#using the for loop
def even(limit):
    for i in range(2, limit+1,2):
        print(i)
even(10)

#using the if else condition
def even(num):
    if num%2==0:
        return "even"
    else:
        return "odd"
print(even(6))
print(even(9))