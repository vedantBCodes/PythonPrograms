#Types of Arguments

# 1.Default arguments
def greet1(name="veda",age="21"):  #Here default values of name and age are set
    print(f"Hlw {name} . You are {age} years old");

greet1();

# 2.Positional arguments
def greet2(name,age):
    print(f"Hlw {name} . You are {age} years old");

greet2("veda","25");

# 3.Keyword arguments
def greet3(name,age):
    print(f"Hlw {name} . You are {age} years old");

greet3(age="42",name="veda");
greet3(name="veda",age="42");

# 4.Arbitrary arguments
def greet3(*details):  #Here details is a tuple of arguments .
    print(f"Hlw {details[0]} . You are {details[1]} years old");

greet3("veda","50");

def sum(*numbers):
    total=0;
    for i in numbers:
        total=total+i;
    print(f"Total : {total}");

sum(2,3,4,5);