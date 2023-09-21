list1=[10,20,30,20,30,10,50,60];

emptyList=[];
for i in list1:
    if i not in emptyList:
        emptyList.append(i);

print(f"List elements after removing duplicates are :",end=" ");
print(emptyList);

