#Using input fuction
#Input function takes every input as string constants

name=input("Enter your name:");
print(f"Hii {name}. \nHow are you!");

age=input("Enter your age:"); # Here type of age is string.
print(f"So you are {age} years old.");

# One can also take input of integer,float directly also

var1=int(input("Enter an integer value :"));   #here one can enter interger values only
print(f"The type of entered value is : {type(var1)}");

var2=float(input("Enter a float value :"));   #Here one can enter float values only
print(f"The type of entered value is : {type(var2)}");

var3=eval(input("Enter any type of value :"));  #Here one can enter any type of values
print(f"The type of entered value is : {type(var3)}"); #Here the type of  var3 will be the same as the intered value

#NOTE : if you are using eval and entering string value , then use double quote " "