#What is the output?
lists = ['a','b','c']
for index,list in enumerate(lists):
    print(index,list)
#What is the output?
for i, v in enumerate([10, 20, 30]):
    print(i, v)
#Write code to print index + value from:index should start from 1.

colors = ['red', 'green', 'blue']
for index, color in enumerate(colors, start=1):
    print(index,color)
#What is the output?
lists = "PYTHON"
for index,list in enumerate(lists, start=1):
    print(index,list)
#Find the index of value 50 using enumerate():
nums = [10, 20, 30, 40, 50, 60]
for index,num in enumerate(nums):
    if num == 50:
        print(index)
#What is the output?
for i, n in enumerate(range(10, 60, 10)):
    print(i, n)
#Convert this into an enumerate() loop:
data=[10,20,40,50,60]
for i,value in enumerate(data):
    print(i,value)
#What is the output?
lists=[]
for index,list in enumerate(lists,start=5):
    print(index,list)
#What is printed?
items = ['a', 'b', 'c']
for i in enumerate(items):
    print(i)
#What is the output?
for i,v in enumerate([100, 200, 300], start=-1):
    print(i, v)
#What happens here?
for i,v in enumerate(['x', 'y', 'z']):
    print(i,v)

