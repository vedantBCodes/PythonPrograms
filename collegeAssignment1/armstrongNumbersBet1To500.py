print("Armstrong numbers between 1 to 500 are : ",end=" ");

for i in range(1,500):
    total=0;
    j=i;
    while(j>0):
        x=j%10;
        total=total+(x*x*x);
        j=j//10;
    if(total==i):
        print(i,end=" ");
