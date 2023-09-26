import myMathModule

#Accessing module varibales

print(myMathModule.PI);

#Accessing module functions

print(myMathModule.sum(20,40));
print(myMathModule.sub(90,40));
print(myMathModule.mul(10,40));
print(myMathModule.div(80,40));
print(myMathModule.mod(50,20));

#Accessing module class variables and class methods

obj=myMathModule.greeting();  #Creating object of a class defined in a module

print(obj.greet);
obj.gm("vedant");
obj.gn();
obj.gl("vedant");
