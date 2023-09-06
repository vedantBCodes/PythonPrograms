ch=input("Enter any chacter :");

if((ord(ch)>=65) and (ord(ch)<=90)):
    print(f"{ch} is an uppercase character");
elif((ord(ch)>=97) and (ord(ch)<=122)):
    print(f"{ch} is an lowercase character");
elif((ord(ch)>=48) and (ord(ch)<=57)):
    print(f"{ch} is a number");
else:
     print(f"{ch} is a special charcter ");