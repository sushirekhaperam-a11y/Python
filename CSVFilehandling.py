import csv
#read the csv file
with open("C://Users//Sushi//PycharmProjects//PythonAdvanceProgramming//PythonProgramming//dataformats//read.csv",'r')as file:
    reader = csv.reader(file)
    for row in reader:
         print(row)

#write the csv file
with open("C://Users//Sushi//PycharmProjects//PythonAdvanceProgramming//PythonProgramming//dataformats//write.csv",'w',newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["id","name","marks"])
    writer.writerow([1,"sunil",90])
    writer.writerow([2,"varsha",85])

#append the data to the csv file
with open("C://Users//Sushi//PycharmProjects//PythonAdvanceProgramming//PythonProgramming//dataformats//write.csv","a",newline="") as file:
    writer = csv.writer(file)
    writer.writerow([3,"praveen",80])