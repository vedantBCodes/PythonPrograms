#Given dictionary represents student roll numbers (As keys) and student names (As values)

studentData={
      5: 'Vedant',
      7: 'Rahul',
     12: 'Omkar',
     16: 'Aditya',
     20: 'Pratik'
}
#Printing keys between 1 to 15

for i in studentData:
     if(i<=15):
         print(f"{i} : {studentData[i]}");