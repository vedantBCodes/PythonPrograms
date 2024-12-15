def linearSearch(arr,key):
    for i in range(len(arr)):
        if(arr[i]==key):
            return 1;
    return 0;

arr=[1,2,3,4,5,6,7,8];
key=14;

if(linearSearch(arr,key)==True):
    print(f"{key} is present in given array");
else:
    print(f"{key} is not there in given array");