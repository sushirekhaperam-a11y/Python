#Handle FileNotFoundError Exception When Opening a File
import json
try:
    with open("C://Users//Sushi//PycharmProjects//PythonAdvanceProgramming//PythonProgramming//dataformats//sushi.json",'r') as file:
        data = json.load(file)
    print(data)
except FileNotFoundError:
    print("File not found")
#Write a program to handle invalid user input
try:
    a = int(input("enter the number:"))
    if a > 0:
        print(a)
except ValueError:
    print("Invalid user input")
#Write a Python program that generates random alphabetical characters, alphabetical strings, and alphabetical strings of a fixed length. Use random.choice()
import random
import string

# Generate a random alphabetical character
def random_char():
    return random.choice(string.ascii_letters)

# Generate a random alphabetical string (random length between 1 and 10)
def random_string():
    length = random.randint(1, 10)
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

# Generate a random alphabetical string of fixed length
def fixed_length_string(length):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))


print("Random character:", random_char())
print("Random string:", random_string())
print("Fixed length string (length 8):", fixed_length_string(8))


