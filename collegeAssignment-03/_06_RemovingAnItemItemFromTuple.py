
#As tuples are immutable you cannot remove an item from a tuple
#But you can reset all the items of tuple using following method

tuple1=tuple(input("Enter the tuple item seperated by space :").split());

item=input("Enter the tuple item you want to remove :");

if(item not in tuple1):
    print(f"{item} is not there in a give tupple.");
    exit(0);

list1=list(tuple1);
list1.remove(item);
tuple1=tuple(list1);
print(tuple1);

