#This program is for 2 digit number only

num=input("Enter a number:");
digit1=num[0];
digit2=num[1];
# Here both the digit1 and digit2 are string

sum=int(digit1)+int(digit2);

print(f"The sum of digits in {num} are {sum}");
