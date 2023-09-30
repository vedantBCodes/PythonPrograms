list1=input("Enter the list items seperated by space :").split();

for i in range(len(list1)):
    list1[i]=int(list1[i]);

maxItem=list1[0];


for i in list1:
    if(i>maxItem):
        maxItem=i;

print(f"The largest item from a given list is : {maxItem}");