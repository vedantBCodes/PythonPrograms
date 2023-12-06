"""

1
2  1
4  2  1
8  4  2  1
16 8  4  2  1

"""
x,y=1,1;
for i in range(1,6):
    for j in range(1,i+1):
        print(f"{x} \t",end=" ");
        x=x//2;
    y=y*2;
    x=y;
    print();