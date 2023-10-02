list1=input("Enter the list items seperated by space :").split();

for i in range(len(list1)):
    list1[i]=int(list1[i]);

item=int(input("Enter the item you want to search in a given tuple : "));

#Method -1:    (using  in operator and count() method)

if(item in list1):
    print(f"{item} is there in a given tuple");
    cnt2=list1.count(item);
    print(f"{item} occurs {cnt2} times");
else:
    print(f"{item} is not there in a given tuple");

#Method -2:  (without using  in operator and count() method)

isPresent=False;
for i in list1:
    if(i==item):
        isPresent=True;

if (isPresent==True):
    print(f"{item} is there in a given tuple");
    count = 0;
    for i in range(0, len(list1)):
        if (list1[i] == item):
            count = count + 1;
    print(f"{item} occurs {count} times");

else:
    print(f"{item} is not there in a given tuple");
