list1=input("Enter the list items seperated by space :").split();

for i in range(len(list1)):
    list1[i]=int(list1[i]);

#Method -1

list2=list1.copy();
list2.sort();
print(list2);

#Method -2

for i in range(0,len(list1)):
    for j in range(i+1,len(list1)):
        if(list1[j]<list1[i]):
            temp=list1[i];
            list1[i]=list1[j];
            list1[j]=temp;

print(list1);