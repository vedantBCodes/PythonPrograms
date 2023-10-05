"""
Given a number n, we need to find the product of all of its unique prime factors.
Prime factors: It is basically a factor of the number that is a prime number itself. Examples:

Input: num = 10
Output: Product is 10
Explanation:
Here, the input number is 10 having only 2 prime factors and they are 5 and 2.
And hence their product is 10.

Input : num = 25
Output: Product is 5
Explanation:
Here, for the input to be 25  we have only one unique prime factor i.e 5.
And hence the required product is 5.

"""

def isPrime(num):
    for i in range(2,num):
        if(num%i==0):
            return False;
    return True;

num=int(input("Enter a Number : "));
prod=1;
for i in range(1,(num//2)+1):
    if((isPrime(i)==True) and (num%i==0)):
        prod=prod*i;

print(f"Product of unique prime factors is : {prod}");

