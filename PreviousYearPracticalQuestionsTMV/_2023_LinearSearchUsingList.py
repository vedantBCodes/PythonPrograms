list1=input("Enter the list items seperated by space :").split();

for i in range(len(list1)):
    list1[i]=int(list1[i]);

item=int(input("Enter an item you want to search : "));

check=False;
for i in list1:
    if(i==item):
        check=True;

if(check==True):
    print(f"{item} is there in a given list");
else:
    print(f"{item} is not there in a given list");
