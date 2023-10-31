
# Multiple Of All Entered Numbers

def multipleOfAll(nums):
    numList = nums.split();
    for i in range(0,len(numList)):
        numList[i]=int(numList[i]);
    prod = 1;

    for i in numList:
        prod = prod * i;

    return prod;

nums=input("Entered numbers seperated by space :");

product=multipleOfAll(nums);
print(f"The product of all entered numbers is : {product}");