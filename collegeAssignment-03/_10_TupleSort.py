#Sorting in Ascending order

tuple1=input("Enter the tuple item seperated by space :").split();   #Here tuple1 is a list
tuple1.sort();
tuple1=tuple(tuple1);
print(f"Tuple items in ascending order {tuple1}");

#Sorting in Ascending order

tuple1=list(tuple1);
tuple1.reverse();
tuple1=tuple(tuple1);
print(f"Tuple items in descending order {tuple1}");