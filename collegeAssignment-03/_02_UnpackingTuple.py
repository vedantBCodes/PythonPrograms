
#Unpacking Tuple into several variables

EData=[21,"vedant",70000.00,True];  #EData --> Employee Data

(EID,EName,ESalary,EisMale)=EData;  #Unpacking tuple items

print(f"Employee ID : {EID}");

print(f"Employee Name : {EName}");

print(f"Employee Salary : {ESalary}");

print(f"Employee Gender -Male : {EisMale}");
