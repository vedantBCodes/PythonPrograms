"""
Input :
 X= [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[9,8,7],
    [6,5,4],
    [3,2,1]]

Output :
 result= [[10,10,10],
         [10,10,10],
         [10,10,10]]
"""
x= [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]

y = [[9,8,7],
    [6,5,4],
    [3,2,1]]

add=[[0,0,0],
     [0,0,0],
     [0,0,0]]

for i in range(len(x)):
    for j in range(len(x)):
        add[i][j]=x[i][j]+y[i][j];

for i in range(len(x)):
    print("[",end=" ");
    for j in range(len(x)):
        print(f"{add[i][j]}",end=" ");
    print("]",end=" ")
    print();
