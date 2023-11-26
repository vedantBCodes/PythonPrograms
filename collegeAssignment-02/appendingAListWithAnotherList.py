list1=[10,20,30,40,50];

list2=[60,70,80,90,100];

list3=[11,22,33,44,55];

#Method-1

for i in list2:
    list1.append(i);
    
print(list1);

#Method-2

list3.extend(list2);

print(list3);
