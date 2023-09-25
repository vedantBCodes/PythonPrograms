"""
Calculating Compound Interest
A = P(1 + R/100)^t

Compound Interest = A – P

Where,

-->A is amount
-->P is the principal amount
-->R is the rate and
-->T is the time span
"""
import math

def compoundInterest(principle,rate,time):
    A=principle*math.pow((1+(rate/100)),time);
    CI=A-principle;
    return CI;

p=int(input("Enter the value of priciple amount : "));
r=float(input("Enter the value of rate of interest : "));
t=float(input("Enter the time period (in sec) : "));

CI=compoundInterest(p,r,t);   #CI - Compound Interest

print(f"The value of compound interest is : {CI}");