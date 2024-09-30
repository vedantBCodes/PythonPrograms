#Finding first pair whose sum is equal to the given value
list1=[1,2,3,4,5,6,7,8,9,10];
sum=6;

num1=0;
num2=0;

check=False;
for i in range(0,6):
    for j in range((i+1),6):
        if(list1[i]+list1[j]==sum):
            num1=list1[i];
            num2=list1[j];
            check=True;
    if(check==True):
        break;

if (check==True):
    print(num1,num2);
else:
    print("Not found");

