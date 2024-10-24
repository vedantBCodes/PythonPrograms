import array  #array is a built-in module

#Creating an array :

arr=array.array('i',[1,2,3,4,5]);

#Printing an array :

print(arr);

#Accessing array items

print(arr[2]);

#updating array items

arr[2]=10;
print(arr);

#Adding array items

arr.append(21);
print(arr);

#Removing array items
arr.remove(4);
print(arr);

#Array slicing

print(arr[1:4]);

#Iterating over an array

for element in arr:
    print(element,end=" ");