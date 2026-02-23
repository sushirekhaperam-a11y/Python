def numbers():
    return[1,2,3,4]
print(numbers())


#using geneartor and yield keyword
def generator():
    print("Printing 1")
    yield 1
    print("printing 2")
    yield 2
    print("printing 3")
    yield 3
    print("printing 4")
    yield 4
ret_val = generator()
print(next(ret_val))

