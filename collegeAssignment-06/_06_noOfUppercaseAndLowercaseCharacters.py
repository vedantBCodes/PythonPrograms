
str1=input("Enter any string :");

upperCnt=0;
lowerCnt=0;
for char in str1:
    order=ord(char);
    if(order>=65 and order<=90):
        upperCnt=upperCnt+1;
    elif(order>=97 and order<=122):
        lowerCnt=lowerCnt+1;
print(f"The total uppercase characters in a given string is {upperCnt}");
print(f"The total lowercase characters in a given string is {lowerCnt}");