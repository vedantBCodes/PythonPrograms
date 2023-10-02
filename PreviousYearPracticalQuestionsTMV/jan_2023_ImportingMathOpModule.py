import MathOpModule

num1,num2=input("Enter any two numbers seperated by space :").split(" ");

num1=int(num1);
num2=int(num2);

print(MathOpModule.sum(num1,num2));
print(MathOpModule.sub(num1,num2));
print(MathOpModule.mul(num1,num2));
print(MathOpModule.div(num1,num2));
