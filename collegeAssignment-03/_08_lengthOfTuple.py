#Calculating length of a tuple

tuple1=tuple(input("Enter the tuple item seperated by space :").split());

#Method -1

len1=len(tuple1);
print(f"Length of a given tuple is : {len1}");

#Method -2

len2=0;

for items in tuple1:
    len2=len2+1;

print(f"Length of a given tuple is : {len2}");
