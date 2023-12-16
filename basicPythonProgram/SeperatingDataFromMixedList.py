"""
Primitive datatypes in python
1.integer
2.float
3.boolean
4.string
"""


mixList=["soma",123,True,22.5,"veda",321,False,12.5,"rahul",456,35.7];

integerList=[];
floatList=[];
booleanList=[];
stringList=[];

for i in mixList:
    if(type(i)==int):
        integerList.append(i);
    elif(type(i)==float):
        floatList.append(i);
    elif (type(i) == bool):
        booleanList.append(i);
    else:
        stringList.append(i);

print(f"The integer values from a given list are : {integerList}");
print(f"The floating values from a given list are : {floatList}");
print(f"The boolean values from a given list are : {booleanList}");
print(f"The string values from a given list are : {stringList}");
