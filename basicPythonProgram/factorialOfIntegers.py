#Factorial Of INTEGERS (all kind of integers)

num=int(input("Enter an integer : "));

fact=1;

if(num==0):
    print("Factorial of zero is  1");
elif(num<0):
    print("Factorial doesn't define for negative integers");
else:
    for i in range(1,num+1):
        fact=fact*i;
    print(f"Factorial of {num} is {fact}");

