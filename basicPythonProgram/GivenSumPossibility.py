
list1=[1,4,3,2,6,5,8,7,10,9];
sum=11;

cnt=0;
for i in list1:
    j=sum-i;
    if((j in list1) and (j>i)):
        print(i,j);
        cnt+=1;

if(cnt==0):
    print("Not Found");