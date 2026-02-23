import xml.etree.ElementTree as ET

#parse the xml file into the variable tree
tree = ET.parse("C://Users//Sushi//PycharmProjects//PythonAdvanceProgramming//PythonProgramming//dataformats//xmlread.xml")
root = tree.getroot()
print(root.tag)

#get the first child node
print(root[0].tag)
print(root[1].tag)

#get the attributes of the child node

print(root[0].attrib)
print(root[1].attrib)

#fetch the attributes of the child node

for employee in root.findall("employee"):
    emp_id = employee.get("id")
    print(emp_id)
    emp_name =employee.find("name").text
    print(emp_name)

for emp in root.findall("employee"):
    name = emp.find("name").text
    role = emp.find("role").text
    exp = emp.find("experience").text
    print(name,role,exp)

# write the xml file
#create the root element

root = ET.Element("employees")
# create the child node
emp1 = ET.SubElement(root,"employee",id="101")
ET.SubElement(emp1,"name").text = "harsha"
ET.SubElement(emp1,"role").text ="tester"
ET.SubElement(emp1,"experience").text="6"

#create the child2 node
emp2 = ET.SubElement(root,"employee",id="102")
ET.SubElement(emp2,"name").text = "amit"
ET.SubElement(emp2,"role").text ="developer"
ET.SubElement(emp2,"experience").text="3"

#write to the file
tree = ET.ElementTree(root)
tree.write("C://Users//Sushi//PycharmProjects//PythonAdvanceProgramming//PythonProgramming//dataformats//write.xml",encoding="utf-8", xml_declaration=True)

#update the xml file

tree = ET.parse("C://Users//Sushi//PycharmProjects//PythonAdvanceProgramming//PythonProgramming//dataformats//update.xml")
root = tree.getroot()
for emp in root.findall("employee"):
    if emp.get("id") == "101":
        emp.find("experience").text="10"
ET.indent(tree, space="    ", level=0)
tree.write("C://Users//Sushi//PycharmProjects//PythonAdvanceProgramming//PythonProgramming//dataformats//update.xml",encoding="utf-8", xml_declaration=True)

