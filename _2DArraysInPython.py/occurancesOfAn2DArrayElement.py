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

# arr=[[1,2,2],[7,8,6],[7,1,1]];

newArr=[];

for  row in arr:
    for element in row:
        newArr.append(element);

len=len(newArr);

for  i in range(len):
    cnt=0;
    check=False;
    for k in range(0,i):
        if(newArr[i]==newArr[k]):
            check=True;
    for j in range(i,len):
        if (check == True):
            break;
        if(newArr[i]==newArr[j]):
            cnt+=1;
    if(check!=True):
        print(f"{newArr[i]} occurs {cnt} times");


