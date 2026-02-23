import threading
def numbers():
    for i in range(5):
        print("numbers",i)
def letters():
    for k in "ABCDEF":
        print("letters",k)
t1 = threading.Thread(target = numbers)
t2 = threading.Thread(target=letters)
t1.start()
t2.start()
t1.join()
t2.join()