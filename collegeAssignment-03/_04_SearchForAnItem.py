tupleItems=tuple(input("Enter the items of tuple seperated by space :").split());

item=input("Enter the item you want to search in a given tuple : ");

#Method -1

isPresent=False;
for i in tupleItems:
    if(i==item):
        isPresent=True;

if (isPresent==True):
    print(f"{item} is there in a given tuple");
else:
    print(f"{item} is not there in a given tuple");

#Method -2

if(item in tupleItems):
    print(f"{item} is there in a given tuple");
else:
    print(f"{item} is not there in a given tuple");
