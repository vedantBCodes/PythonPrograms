#One can import some specific function from a module

#from myMathModule import sum   --->This will import only sum function from a module .
                                  # Now it can be accessed directly without using module name

from myMathModule import*   #-->This will import all the attributes from myMathModule module
                             # And these all attributes can be accessed directly

#Accessing module varibales

print(PI);

#Accessing module functions

print(sum(20,40));
print(sub(90,40));
print(mul(10,40));
print(div(80,40));
print(mod(50,20));

#Accessing module class variables and class methods

obj=greeting();  #Creating object of a class defined in a module

print(obj.greet);
obj.gm("vedant");
obj.gn();
obj.gl("vedant");