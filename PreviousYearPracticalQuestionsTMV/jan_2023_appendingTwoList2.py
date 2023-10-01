list1=input("Enter the list items seperated by space :").split();

for i in range(len(list1)):
    list1[i]=int(list1[i]);

list2=input("Enter the list items seperated by space :").split();

for i in range(len(list2)):
    list2[i]=int(list2[i]);

# Method -1
list3=list1+list2;

print(list3)

#Method -2

tempList=list1.copy();
for x in list2:
    tempList.append(x);

print(tempList);

#Method -3

list1.extend(list2);

print(list1);
