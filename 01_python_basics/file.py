
employee_name=open("employee.txt","r")

# print(employee_name.readline()) #reads 1 line and move the pointer to next line
# print(employee_name.read())     #reads the remaining lines

# print(employee_name.readlines()[3])

for employee in employee_name.readlines():
    print(employee)

employee_name.close()

employee_write=open("employee1.txt","w")

employee_write.write("Adi engineer\n")
