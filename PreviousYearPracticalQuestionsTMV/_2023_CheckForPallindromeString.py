str1=input("Enter a string :");


str2=str1[::-1];  #It will store a reversed string in str2

if(str1==str2):
    print(f"yes ! {str1} is a pallindrome string");
else:
    print(f"No ! {str1} is not a pallindrome string");
