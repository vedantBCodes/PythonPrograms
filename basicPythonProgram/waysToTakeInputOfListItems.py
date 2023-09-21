#Different ways to take input of list items

#Method -1

nums1=input("Enter the list items seperated by spaces : ");

numList1=nums1.split(" ");   # OR numList=nums1.split();  Here the list items in numList are of string type

length=len(numList1);

for i in range(0,length):
    numList1[i]=int(numList1[i]);

#Method -2

numList2=input("Enter the list items seperated by spaces : ").split();

length2=len(numList2);

for i in range(0,length2):
    numList2[i]=int(numList2[i]);

#Method -3

n=int(input("Enter how many list items you want to enter : "));

numList3=[];
for i in range(0,n):
    num=int(input("Enter a list items : "));
    numList3.append(num);

print(numList3);
