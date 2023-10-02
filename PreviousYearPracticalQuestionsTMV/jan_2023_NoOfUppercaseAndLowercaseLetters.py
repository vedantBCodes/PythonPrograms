str1=input("Enter a string :");

upperCount=0;
lowerCount=0;

for characters in str1:
    if(characters.isupper()==True):
        upperCount+=1;
    elif(characters.islower()==True):
        lowerCount+=1;

print(f"The total number of uppercase letters in a givem string are {upperCount}");
print(f"The total number of uppercase letters in a givem string are {lowerCount}");