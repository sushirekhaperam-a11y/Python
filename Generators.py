#Write a generator to generate numbers from 1 to N.

def numbers():
    n=int(input("enter the number:"))
    for i in range(1,n):
        yield i
gen = numbers()
for num in gen:
    print(num)
#Create a generator to generate even numbers only.
def even():
    for i in range(2,11,2):
        yield i
gen = even()
for num in gen:
    print(num)
#Write a generator to read a file line by line.
import csv
def line_by_line(read):
    with open(read,"r") as file:
        reader = csv.reader(file)
        for row in reader:
            yield row
for row in line_by_line("C://Users//Sushi//PycharmProjects//PythonAdvanceProgramming//PythonProgramming//dataformats//read.csv"):
    print(row)
#Create a generator for Fibonacci series.
def fibonacci():
    a,b=0,1
    while True:
        yield a,b
        a,b = b,a+b
ret_val =fibonacci()
print(next(ret_val))
print(next(ret_val))
print(next(ret_val))
#Write a generator that simulates retry attempts (max 3 tries).
def retry_attempt(max=3):
    for attempt in range(1,max+1):
        yield attempt
gen = retry_attempt()
print(next(gen))
print(next(gen))
print(next(gen))



