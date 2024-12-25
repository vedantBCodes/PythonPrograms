""""
Interpolation Search is an advanced searching algorithm that works on sorted arrays.
It improves the efficiency of searching for values that are uniformly distributed (difference between two consecative
list elements must be same )by estimating the position of the target value, similar to the way humans look for a name in a telephone directory.
"""
def interpolationSearch(arr, key):
    startIndex = 0     #index of 1st element
    endIndex = len(arr) - 1    #index of last element

    while startIndex <= endIndex and arr[startIndex] != arr[endIndex]:
        # Estimate the position
        pos = startIndex + ( (key - arr[startIndex]) * (endIndex - startIndex) // (arr[endIndex] - arr[startIndex]) )

        # Check the estimated position
        if arr[pos] == key:
            return pos
        elif arr[pos] < key:
            startIndex = pos + 1
        else:
            endIndex = pos - 1

    return -1

# Example usage
arr = [10, 20, 30, 40, 50]
key = 10
result = interpolationSearch(arr, key);

if(result==-1):
    print("Element not found");
else:
    print(f"Element found at index: {result}");

