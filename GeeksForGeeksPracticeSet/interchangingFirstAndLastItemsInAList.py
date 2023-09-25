list1=input("Enter list items seperated by spaces :").split(" ");


print(f"Before Swapping : {list1}");

temp=list1[0];
list1[0]=list1[len(list1)-1];
list1[len(list1)-1]=temp;

print(f"After Swapping : {list1}");