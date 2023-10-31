
# Removing duplicates from a list

def removingDuplicates(nums):
    numList=nums.split();
    emptyList=[];
    for i in range(0,len(numList)):
        numList[i]=int(numList[i]);

    for i in numList:
        if(i not in emptyList):
            emptyList.append(i);
    return emptyList;


nums = input("Enter list items seperated by space :");
newList=removingDuplicates(nums);
print(f"The unique items in a given lists are : {newList}");