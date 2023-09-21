numbers=input("Enter the list items seperated by space : ");

numberList=numbers.split(" ");

cnt=0;

for i in numberList:
    cnt=cnt+1;

for i in range(0,cnt):
    numberList[i]=int(numberList[i]);

count=0;
num=int(input("Enter a number : "));
for i in range(0,cnt):
    if(numberList[i]==num):
        count=count+1;

if(count>0):
    print(f"{num} occurs {count} times");
else:
    print(f"{num} is not there in a list");
