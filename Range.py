a=range(5)
print(a[1])
print(a[4])
a1=range(2,6)
print(a1[2])
a2 = range(2,15,-3)
for i in a2:
    print(i)
a3 = range(25,2,-1)
for i in a3:
    print(i)
for attempt in range(3):
    pin = input("enter the pin")
    if pin == "1234":
        print("access granted")
        break
    else:
        print("account locked")
prices = [100,200,300,400]
for i in range(len(prices)):
    if i %2==0:
        print(f"discount applied on items{1}")
import time
for second in range(10):
    print("second status")
    time.sleep(1)
