#Slicing a Tuple

tuple1=tuple(input("Enter the tuple item seperated by space :").split());

startIndex=int(input("Enter the last index for slicing :"));
endIndex=int(input("Enter the last index for slicing :"));

print(f"Tuple after slicing {tuple1[startIndex:endIndex]}");
