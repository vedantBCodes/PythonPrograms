'''AS Input function takes every input as string constants,
SO type conversion is very necessary to perform some mathematical operations'''

x1=10; # Here the type of x1 is int.
x2=10.10 # Here the type of x2 is float.
x3=True # Here the type of x3 is boolean.
y=input("Enter the value of y:"); # But here type of y is string.
y=int(y); #Type conversion

z=int(input("Enter the value of z:"));  #Type conversion  , so here type of z will be int.
#This is the best way of taking a perticular type of variable using type conversion

print("The value of x1 is "+str(x1)); #Type conversion
print(f"The value of x2 is {x1}");
print(f"The value of x2 is {x2}");
print(f"The value of x3 is {x3}");
print(f"The value of y is {y}");
print(f"The value of z is {z}");

