import json

# read the json file
with open("C://Users//Sushi//PycharmProjects//PythonAdvanceProgramming//PythonProgramming//dataformats//simple.json",'r') as file:
    data = json.load(file)
print(data)
print(data["name"])
#read the json file with nested file
with open("C://Users//Sushi//PycharmProjects//PythonAdvanceProgramming//PythonProgramming//dataformats//nested.json",'r') as file:
    data = json.load(file)
email = data["user"]["profile"]["email"]
print(email)
id = data["user"]["profile"]
print(id)

# write the json file
data ={
  "name": "Harsha",
  "role": "Tester",
  "experience": 5,
  "skills": ["Python", "Automation", "API"]
}
with open("C://Users//Sushi//PycharmProjects//PythonAdvanceProgramming//PythonProgramming//dataformats//write.json",'w') as file:
    json.dump(data,file)


#update the json file
with open("C://Users//Sushi//PycharmProjects//PythonAdvanceProgramming//PythonProgramming//dataformats//update.json",'r') as file:
    data = json.load(file)

data["experience"] = 6
with open("C://Users//Sushi//PycharmProjects//PythonAdvanceProgramming//PythonProgramming//dataformats//update.json",'w') as file:
    json.dump(data,file, indent=4)



