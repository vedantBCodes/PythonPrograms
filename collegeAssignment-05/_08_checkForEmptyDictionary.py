#Checking for empty dictionary

#Example -1 :

studentID1={
    'Vedant':123,
    'Rahul':456,
    'Omkar':789,
    'Aditya':321,
    'Pratik':765
}

#Example 2 :

studentID2={};  #An Empty dictionary

#Method -1    (Using len() Method)

#Example -1 :

if(len(studentID1)==0):
    print("Given dictionary is an Empty dictionary");
else:
    print("Given dictionary is Not an empty dictionary");

#Example -2 :

if(len(studentID2)==0):
    print("Given dictionary is an Empty dictionary");
else:
    print("Given dictionary is Not an empty dictionary");


#Method -2:       (Using clear() method)

#Example -1 :

studentID1Copy=studentID1.copy();
studentID1Copy.clear()
if(studentID1==studentID1Copy):
    print("Given dictionary is an Empty dictionary");
else:
    print("Given dictionary is Not an empty dictionary");

#Example -2 :

studentID2Copy=studentID2.copy();
studentID2Copy.clear()
if(studentID2==studentID2Copy):
    print("Given dictionary is an Empty dictionary");
else:
    print("Given dictionary is Not an empty dictionary");
