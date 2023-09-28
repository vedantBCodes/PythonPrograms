studentID={
    'vedant':123,
    'rahul':456,
    'omkar':789,
    'aditya':321,
    'pratik':654
}

#Sorting dictionary by keys

print("Sorting dictionary by keys \n")

#Ascending sort

print("Sorting dictionary in ascending order :")
keyList=list(studentID.keys());

keyList.sort()

for i in keyList:
    print(f"{i} : {studentID[i]}");

#Descending sort

print("\nSorting dictionary in descending order :")

keyList.reverse();

for i in keyList:
    print(f"{i} : {studentID[i]}");

#Sorting dictionary by values

print("\nSorting dictionary by values \n")

#Ascending sort

print("Sorting dictionary in ascending order :");
keyList2=list(studentID.keys());
valuesList=list(studentID.values());
valuesList.sort();

for i in valuesList:
    index2=valuesList.index(i);
    print(f"{keyList2[index2]} :{i}");

# #Descending sort

print("\nSorting dictionary in descending order :");
keyList3=list(studentID.keys());
valuesList.reverse();

for i in valuesList:
    index2=valuesList.index(i);
    print(f"{keyList3[index2]} :{i}");
