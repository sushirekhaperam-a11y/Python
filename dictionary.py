#create a dictionary with student roll number as key and name as value. Print the dictionary.

dict = {1:"sunil",2:"varsha",3:"praveen",4:"chiru"}
print(dict)

#Access the value of a key that exists and one that does not exist

print(dict[4])  # for the existing key
print(dict.get(5))  # for an not existing key


#Update the value of an existing key in a dictionary.

dict.update({4:"sushi"})
print(dict)

#Delete a key from a dictionary using:

dict.pop(1)
print(dict)

del dict[2]
print(dict)

#Find the number of key–value pairs in a dictionary.

print(dict.keys())

print(dict.values())

print(dict.items())

#Find the number of key–value pairs in a dictionary.

print(len(dict))