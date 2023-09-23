studentID1={
    'Vedant':123,
    'Rahul':456,
    'Omkar':789,
    'Aditya':321,

}
studentID2={
    'Soma':987,
    'Gopal':876,
    'Pratik':654
}
studentID1.update(studentID2);

for i in studentID1:
     print(f"{i} : {studentID1[i]}");