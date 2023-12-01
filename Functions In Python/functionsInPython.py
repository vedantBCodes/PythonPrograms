#Function is a block of code that performs specific task

#Defining a fucntion
def greet1():
    print(f"Hlw ! How are you");

#Calling a function

greet1();

#fucntion with arguments
def greet2(name,age):
    print(f"Hlw {name} . You are {age} years old");

greet2("veda","30");

#Functions with return type

def greet3(name,age):
    str1=f"Hlw {name} . You are {age} years old";
    return str1;

print(greet3("veda","101"));




