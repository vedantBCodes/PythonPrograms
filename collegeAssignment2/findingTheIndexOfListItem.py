list1=[10,20,30,40,50];

cnt=0;
check=False;
num=int(input("Enter a list item : "));
for i in list1:
    if(i==num):
        check=True;
        break;
    cnt = cnt + 1;


if(check==True):
     print(f"The index of {num} is {cnt}");
else:
    print(f"{num} is not there in the given list");

