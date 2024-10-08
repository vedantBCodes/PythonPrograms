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

# arr=[[12,21,13],[14,51,16],[17,34,45]];

max=arr[0][0];
for  row in arr:
    for element in row:
        if(element>max):
            max=element;

print(max);
x=-sys.maxsize - 1;
for  row in arr:
    for element in row:
        if(element > x and element < max):
            x=element;

print(f"The second smallest array element is  : {x}");

