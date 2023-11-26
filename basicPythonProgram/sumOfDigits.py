
#code for 2 digit number only

num=input("Enter a 2 digit number:");
digit1=num[0];
digit2=num[1];
# Here both the digit1 and digit2 are string

sum=int(digit1)+int(digit2);

print(f"The sum of digits in {num} are {sum}");

#code for numbers with any no. of digits

num2=int(input("Enter any number : "));
temp=num2;
sum2=0;
while(num2>0):
    x=num2%10;
    sum2=sum2+x;
    num2=num2//10;

print(f"The sum of digits in {temp} are {sum2}");
