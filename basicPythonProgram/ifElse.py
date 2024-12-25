#Voting

age=int(input("Enter your age:"));

if(age>18) :    # Here paranthesis are optional
    print("You are selected to give vote");
else :
    print("You can't give vote");

#Marks and grades

marks=int(input("Enter your marks to know your grades:"));

if((marks>=90)and(marks<=100)):   # Here paranthesis are optional
    print("A+");
elif((marks>=80)and(marks<90)):
    print("A");
elif((marks>=70)and(marks<80)):
    print("B+");
elif((marks>=60)and(marks<70)):
    print("B");
else:
    print("C");
