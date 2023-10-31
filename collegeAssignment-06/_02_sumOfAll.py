
# sum Of All Entered Numbers

def sumOfAll(nums):
    numList = nums.split();
    for i in range(0,len(numList)):
        numList[i]=int(numList[i]);
    total = 0;

    for i in numList:
        total = total + i;

    return total

nums=input("Entered numbers seperated by space :");

Total=sumOfAll(nums);
print(f"The sum of all entered numbers is : {Total}");