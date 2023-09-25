"""
A number is Fibonacci if and only if one or both of (5*n^2 + 4) or (5*n^2 – 4) is a perfect square
"""
import math

num=int(input("Enter a number : "));

x=((5*pow(num,2))+4);
y=((5*pow(num,2))-4);

xSquareRoot=math.isqrt(x);
ySquareRoot=math.isqrt(y);

if((pow(xSquareRoot,2)==x) or (pow(ySquareRoot,2)==y)):
    print(f"{num} is a fibonaccy number");
else:
    print(f"{num} is not a fibonaccy number");