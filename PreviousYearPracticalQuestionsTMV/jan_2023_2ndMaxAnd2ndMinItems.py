list1=input("Enter the list items seperated by space :").split();

for i in range(len(list1)):
    list1[i]=int(list1[i]);

#Method -1:

for i in range(0,len(list1)):
    for j in range(i,len(list1)):
        if(list1[i]>list1[j]):
            temp=list1[i];
            list1[i]=list1[j];
            list1[j]=temp;

print(f"The second maximum item from a given list is : {list1[-2]}");

print(f"The second minimum item from a given list is : {list1[1]}");

#Method -2:

list1.sort();

print(f"The second maximum item from a given list is : {list1[-2]}");

print(f"The second minimum item from a given list is : {list1[1]}");