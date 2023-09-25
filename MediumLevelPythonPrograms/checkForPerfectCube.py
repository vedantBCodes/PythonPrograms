import math


def checkForPerfectCube(num):
    cubeRoot=round(pow(num,1/3));
    if(pow(cubeRoot,3)==num):
        return True;
    return False;

try:
    num = int(input("Enter a number : "));
    tempNum=abs(num);   #The cube of any negative number is always a negative number
    check = checkForPerfectCube(tempNum);

    if (check == True):
        print(f"{num} is  a perfect cube");
    else:
        print(f"{num} is  not a perfect cube");
except:
    print("Invalid input !!! Please enter a valid integer input");

