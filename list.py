#Write a Python program to get the largest number from a list.
list=[30,50,70,90,80]
max_value=max(list)
print(max_value)
#remove the even numbers from the list
list=[2,5,7,9,4,6]
for i in list[:]:
    if i%2==0:
        list.remove(i)
print(list)

#multiply the items in the list
mul=1
list1=[2,3,4,5,6]
for i in list1:
    mul*=i
print(mul)

