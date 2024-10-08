
# Declaring a 2D array

arr=[[1,2,3],[4,5,6],[7,8,9]];

# Printing whole array

print(arr);

# Accessing 2D array elements

print(arr[0][0]);     #Accessing 0,0 element

#Updating array element

arr[0][0]=21;

print(arr[0][0]);

# Appending array elements

arr.append([10,20,30]);

print(arr);

# Inserting array elements

arr.insert(0,[11,12,23]);

print(arr);

# Removing array elements

# arr.remove([1,2,3]);
del arr[0];

print(arr);

# Iterating over 2D array

for row in arr:
    for element in row:
        print(f"{element} ",end="");
    print();
