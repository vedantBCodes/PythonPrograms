num=int(input("Enter a number : "));

tempNum=num;
total=0;
while (tempNum>0):
    rem=tempNum%10;
    total=total+(rem**3);
    tempNum=tempNum//10;

if(total==num):
    print(f"{num} is an armstrong number ");
else:
    print(f"{num} is not an armstrong number ")