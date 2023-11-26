numList=tuple(input("Enter numbers seperated by space :").split(" "));

#Method-1

tuple1=[];  #an empty tuple

for i in numList:
    if(numList.count(i)>1):
        if(i not in tuple1):
            tuple1.append(i);

print("Repeated items in a given tuple are :",end=" ");
print(tuple1);

#Method-2

length=len(numList);
print("Repeated items in a given tuple are :",end=" ");

for i in range(0,length):
    check1=False;
    for j in range(0,i):
        if(numList[i]==numList[j]):
            check1=True;
    if(check1==False):
        check2=False;
        for k in range(i+1,length):
            if(numList[i]==numList[k]):
                check2=True;
        if(check2==True):
            print(numList[i],end=" ");
