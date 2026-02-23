my_dict={1:"one",2:"two",3:"three",4:"four"}
print(my_dict)

#my_dict = {(1,2):"one two",(3,4):"three four"}
#print(my_dict)

print(my_dict[1])

my_dict[5]="five"
print(my_dict)

print(len(my_dict))

del my_dict[4]
print(my_dict)

print(my_dict.keys())

print(my_dict.values())

#print(my_dict.pop(3))

#print(my_dict.popitem())

#print(my_dict.clear())

#my_dict={1:"one",2:"two",3:"three",1:"four"}
#print(my_dict)

my_dict.update({6:"six"})
print(my_dict)


employee = [{"id":1,"name":"sunil","role":"ca"},
            {"id":2,"name":"varsha","role":"doctor"},
{"id":3,"name":"praveen","role":"it"}]
print(employee)

print(employee[1])

print(employee[0]["name"])

print(employee.pop(2))

employee.append({"id":4,"name":"chiru","role":"it"})
print(employee)

for emp in employee:
    print(emp["name"],emp["role"])

for emp in employee:
    if emp["name"] == "sunil":
        print(emp)



