"""
Given an integer ‘n’, write a Python function that returns true if binary representation of x is palindrome else return false.
Examples:

Input : n = 9
Output : True
Binary representation of n=9 is 1001 which is palindrome as well.

Input : n = 10
Output : False
Binary representation of n=10 is 1010 which is not palindrome.

"""

num=int(input("Enter a number : "));

binaryNum=bin(num);

#bin() function returns binary conversion of a given number
#but it adds "0b" as prefix before binary representation

binaryNum=binaryNum[2:];  #doing slicing to remove the first two charcters "0b"

print(binaryNum);

if (binaryNum==binaryNum[::-1]):
    print(f"Yes ! The binary reprentation of {num} is a pallindrome ");
else:
    print(f"No ! The binary reprentation of {num} is not a pallindrome ");