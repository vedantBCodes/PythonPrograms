num=int(input("Enter how many first fibonnacy series terms you want to print : "));

a=0;
b=1;

print(f"First {num} terms in fibonaccy series are :",end=" ");
print(f"{a} {b} ",end=" ");
for i in range(1,num):
    c=a+b;
    print(c,end=" ");
    a=b;
    b=c;