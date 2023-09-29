year=int(input('Enter any year :'));

if(year%100==0):
    if(year%400==0):
        print(f"{year} is a leap year");
    else:
        print(f"{year} is not a leap year");
else:
    if(year%4==0):
        print(f"{year} is a leap year");
    else:
        print(f"{year} is not a leap year");

