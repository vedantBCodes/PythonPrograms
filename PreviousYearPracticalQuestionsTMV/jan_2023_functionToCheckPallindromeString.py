def pallindrome(str1):
    str2=str1[::-1];
    if(str1==str2):
        print(f"{str1} is a pallindrome string");
    else:
        print(f"{str1} is not a pallindrome string");

str1=input("Enter a string :");
pallindrome(str1);