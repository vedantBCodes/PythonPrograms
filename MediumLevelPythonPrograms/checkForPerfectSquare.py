import math


def checkForPerfectSquare(num):
    squareRoot=math.isqrt(num);
    if(pow(squareRoot,2)==num):
        return True;
    return False;

try:
    num = int(input("Enter a number : "));
    check = checkForPerfectSquare(num);

    if (check == True):
        print(f"{num} is  a perfect square");
    else:
        print(f"{num} is  not a perfect square");
except:
    print("Invalid input !!! Please enter a valid integer input");

