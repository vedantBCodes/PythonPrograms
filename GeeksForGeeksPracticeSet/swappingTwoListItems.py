list1=input("Enter list items seperated by space : ").split();

for i in range(len(list1)):
    list1[i]=int(list1[i]);

item1,item2=input("Enter two list items seperated by space : ").split();

item1=int(item1);
item2=int(item2);

index1=list1.index(item1);
index2=list1.index(item2);

print(f"list items before swapping : {list1}");

temp=list1[index1];
list1[index1]=list1[index2];
list1[index2]=temp;

print(f"list items after swapping : {list1}");