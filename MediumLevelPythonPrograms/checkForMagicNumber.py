
# In mathematics, if the sum of its digits recursively is calculated till a single digit.
# If the single digit is 1 then the number is called a magic number. It is quite similar to the happy number.
#
# For example, 325 is a magic number because the sum of its digits (3+2+5) is 10, and again sum up the resultant (1+0),
# we get a single digit (1) as the result. Hence, the number 325 is a magic number.
#
# Some other magic numbers are 1234, 226, 10, 1, 37, 46, 55, 73, etc.

num=int(input("Enter a number : "));
numCopy=num;
check=False;
cnt=0;
numList=[];   #Empty list
while(cnt!=1):
    total=0;
    while (num > 0):
        x = num % 10;
        total = total + x;
        num = num // 10;
    for i in numList:
        if(total==i):
            cnt=1;
            check=False;
            break;
    numList.append(total);
    num=total;
    if (total == 1):
        cnt=1;
        check=True;
        break;


if(check==True):
    print(f"{numCopy} is a magic number");
else:
    print(f"{numCopy} is Not a magic number");