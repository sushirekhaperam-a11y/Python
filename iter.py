a  =[10,20,30,40,50]
it = iter(a)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

s = "apple"
it = iter(s)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

dict = {1:'a',2:'b',3:'c'}
it = iter(dict)
print(next(it))

for key in it:
    print(key)

for key,values in dict.items():
    print(key,"->",values)

def get_input():
    return input("enter the input")
for value in iter(get_input,"quit"):
    print("you entered",value)
print("loop entered")
