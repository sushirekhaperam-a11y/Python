#Built in Exceptions
try:
    a = int(input("enter the number:"))
    b = int(input("enter the number:"))
    print(a/b)
except ZeroDivisionError:
    print("cannot divide by zero")
except ValueError:
    print("Enter the valid number")

#Generic Exception
try:
    a=5/0
except Exception as e:
    print(e)
else:
    print("Division successfull")
finally:
    print("Exit the browser")

#Custom Exception
age=int(input("enter the age"))
if age > 18:
    raise  ValueError("age must be 18 or above")

