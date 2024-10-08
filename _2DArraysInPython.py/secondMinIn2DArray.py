import sys;
row=int(input("Please enter the number of rows :"));

col=int(input("Please enter the number of columns :"));

arr=[];  #Defining an empty array

print(f"Please enter {row*col} array items : ");

for i in range(row):
    row=[];
    print(f"Enter any {col} array elements for Row {i+1} :");
    for j in range(col):
        element=int(input());
        row.append(element);
    arr.append(row);

# arr=[[1,2,3],[4,5,6],[7,8,9]];

min=arr[0][0];
for  row in arr:
    for element in row:
        if(element < min):
            min=element;

print(min);
x=sys.maxsize;
for  row in arr:
    for element in row:
        if(element < x and element > min):
            x=element;

print(f"The second smallest array element is  : {x}");