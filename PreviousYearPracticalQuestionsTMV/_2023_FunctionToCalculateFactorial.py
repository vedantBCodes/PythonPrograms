#Calculating Factorial

from math import factorial

#Method -1:
def factorialOfNum(num):
    fact=1;
    for i in range(1,num+1):
        fact=fact*i;
    return fact;

num=int(input("Enter a number : "));

f1=factorialOfNum(num);

print(f"Factorial of {num} is {f1}");

#Method -2:

f2=factorial(num);  #Factorial() is a predefined method of math module

print(f"Factorial of {num} is {f2}");

