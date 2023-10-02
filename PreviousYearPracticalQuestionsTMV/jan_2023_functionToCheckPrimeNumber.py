def primeNumber(num):
    check = True;
    for i in range(2, num):
        if (num % i == 0):
            check = False;
    if (check == True and num > 1):
        print(f"{num} is  a prime number");
    else:
        print(f"{num} is not a prime number");


num=int(input("Enter an integer number : "));
primeNumber(num);

