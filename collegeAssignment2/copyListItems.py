list1=[10,20,30,40,50];

cnt=0;
for i in list1:
    cnt=cnt+1;

copyList=[];  #Empty list
for i in list1:
    copyList.append(i);

print(copyList);