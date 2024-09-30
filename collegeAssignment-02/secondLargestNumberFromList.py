numbers=input("Enter the list items seperated by space : ");

numberList=numbers.split(" ");

cnt=0;

for i in numberList:
    cnt=cnt+1;

for i in range(0,cnt):
    numberList[i]=int(numberList[i]);


# Method -1

max=numberList[0];

for i in range(0,cnt):
    if(numberList[i]>max):
        max=numberList[i];

secondMax=numberList[0];numbers=input("Enter the list items seperated by space : ");

numberList=numbers.split(" ");

cnt=0;

for i in numberList:
    cnt=cnt+1;

for i in range(0,cnt):
    numberList[i]=int(numberList[i]);

max=numberList[0];

for i in range(0,cnt):
    if(numberList[i]>max):
        max=numberList[i];

secondMax=numberList[0];
for i in range(0,cnt):
    if(numberList[i]<max and numberList[i]>secondMax):
        secondMax=numberList[i];

print(f"The second maximum number from a list is :{secondMax}");
for i in range(0,cnt):
    if(numberList[i]<max and numberList[i]>secondMax):
        secondMax=numberList[i];

print(f"The second maximum number from a list is :{secondMax}");

# Method -2

max=numberList[0];
secondMax2=0;
for i in range(0,cnt):
    if(numberList[i]>max):
        secondMax2 = max;
        max=numberList[i];

print(f"The second maximum number from a list is :{secondMax2}");

