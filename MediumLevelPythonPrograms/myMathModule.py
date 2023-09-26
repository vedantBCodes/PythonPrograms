#Here i am creating a built in module

#A module is a file containing some variables , functions and classes
#A python file with .py extension can be a module

#Varibales

PI =3.14;

#Functions

def sum(a,b):
    return a+b;


def sub(a,b):
    return a-b;

def mul(a,b):
    return a*b;

def div(a,b):
    return a/b;

def mod(a,b):
    return a%b;

#Class

class greeting:
    greet="Hello !";
    def gm(self,name):
        print(f"{self.greet} Good morning {name}");

    def gn(self,name):
        print(f"{self.greet} Good night {name}");

    def gl(self,name):
        print(f"{self.greet} Good luck {name}");
