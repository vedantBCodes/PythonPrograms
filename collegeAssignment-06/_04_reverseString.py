
# Reversing a string  Strings are immutable in python

# Method -1   (Using Loop)

def reverseAString1(str1):
    tempStr="";  #Empty string
    for i in range(len(str1)-1,-1,-1):
        tempStr=tempStr+str1[i];
    return tempStr;

# Method -2   (Using slicing)

def reverseAString2(str1):
    tempStr=str1[::-1]
    return tempStr;


str1=input("Enter a string :");
reversedStr1=reverseAString1(str1);

print(f"The reversed string : {reversedStr1}");

reversedStr2=reverseAString2(str1);

print(f"The reversed string : {reversedStr2}");