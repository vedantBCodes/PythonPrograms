#Factorial Of INTEGERS (all kind of integers)

def FactorialOfNum(num):
    fact = 1;
    for i in range(1, num + 1):
        fact = fact * i;
    return fact;

num=int(input("Enter an integer : "));
fact=FactorialOfNum(num);
if (num == 0):
    print("Factorial of zero is  1");
elif (num < 0):
    print("Factorial doesn't define for negative integers");
else:
     print(f"Factorial of {num} is {fact}");