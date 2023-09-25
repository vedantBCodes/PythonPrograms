import math


def checkForPerfectCube(num):
    cubeRoot=math.is(num);
    if(pow(cubeRoot,3)==num):
        return True;
    return False;

try:
    num = int(input("Enter a number : "));
    check = checkForPerfectCube(num);

    if (check == True):
        print(f"{num} is  a perfect cube");
    else:
        print(f"{num} is  not a perfect cube");
except:
    print("Invalid input !!! Please enter a valid integer input");

