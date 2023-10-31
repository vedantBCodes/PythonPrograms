
def evenNumberFromAList(nums):
    numList=nums.split();
    emptyList=[];
    for i in range(0,len(numList)):
        numList[i]=int(numList[i]);

    for i in numList:
        if(i%2==0):
            emptyList.append(i);
    return emptyList;


nums = input("Enter list items seperated by space :");
newList=evenNumberFromAList(nums);
print(f"The even items in a given lists are : {newList}");