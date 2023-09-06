ch=input("Enter an alphabet :");

chLower=ch.upper();

if((ord(chLower)>=65) and (ord(chLower)<=90)):
    if(chLower=='A' or chLower=='E' or chLower=='I' or chLower=='O' or chLower=='U'):
        print(f"{ch} is a vowel");
    else:
        print(f"{ch} is a consonant");
else:
     print("Entered character is not an alphabet");