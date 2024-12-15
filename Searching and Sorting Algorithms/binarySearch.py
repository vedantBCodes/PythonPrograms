
# Binary search can be only applied in a sorted array

def binarySearch(arr,key):
    startIndex = 0;
    endIndex = len(arr) - 1;
    while (startIndex <= endIndex):
        midIndex = (startIndex + endIndex) // 2;
        if (arr[midIndex] == key):
            return 1;
        elif (key < arr[midIndex]):
            endIndex = midIndex - 1;
        else:
            startIndex = midIndex + 1;

arr=[1,2,3,4,5,6,7];
key=10;

if(binarySearch(arr,key)==True):
    print(f"{key} is present in the given array");
else:
    print(f"{key} is not there in given array");

