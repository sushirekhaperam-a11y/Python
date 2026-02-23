#comphrension
sqs = [x**2 for x in range(1,6)]
print(sqs)
#comphrension with condition
even = [x for x in range(10) if x%2==0]
print(even)
#dictionary comphrension
dict = {"a" : 90000,"b":60000,"c":40000}
hike = {k:v+0.1*v for k,v in dict.items()}
print(hike)
#set comphrension
sqs = [a**2 for a in range(20)]
print(sqs)
#set comphrension with condition
sqs = [x**2 for x in range(20) if x%2==0]
print(sqs)
#filtering of dictionary
emp = {
    "sunil":"active",
    "varsha":"active",
    "deepu":"inactive"
}
empl = {k:v for k,v in emp.items() if v == "active"}
print(empl)