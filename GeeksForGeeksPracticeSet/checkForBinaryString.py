str1=input("Enter a string :");

check=True;

for i in str1:
    if(i!="0" and i!="1"):
        check=False;

if(check==True):
    print("Given string is a binary string");
else:
    print("Given string is not a binary string");