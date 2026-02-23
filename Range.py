#Even numbers
for i in range(1,51):
    if i %2==0:
        print(i)
# Numbers divisible by 5
for i in range(1,101):
    if i%5==0:
        print(i)
#Create a list of numbers from 50 to 100 with a step of 5
for i in range(50, 101,5):
    print(i)
# Print the square of each number from 1 to 10.
for i in range(1,10):
    print(i*i)
#Print numbers between -10 and 10.
for i in range(-10,10):
    print(i)
# Write a Python function to Sum of numbers from 1 to 100
sum=0
for i in range(1,100):
    sum+=i
print(sum)

#Write a Python function to check whether a number falls within a given range
n=int(input("enter the number"))
for i in range(1,10):
    if n == i:
        print("Number falls within the range")
    else:
        print("Number doesnt falls within the range")