# Implementation of Stack using array (Static)

# Defining Stack class

class Stack:
    def __init__(self,size):
        self.arr = [0] * size;   #It will create an empty array with size=size;
        self.size=size;
        self.top=-1;    #Initializing top variable to -1 (Top variable shows the index of the topmost stack element

    def isEmpty(self): #Checks whether the stack is empty or not
        if(self.top==-1):
            return 1;
        else:
            return 0;

    def isFull(self):   #Checks whether the stack is full or not
        if(self.top==(self.size-1)):
            return 1;
        else:
            return 0;

    def push(self,element):  #Insert a new element into the stack
        if(self.isFull()==1):
            print("Stack Overflow");
        else:
            self.top+=1;
            self.arr[self.top]=element;

    def pop(self):   # Removes an element from a stack
        if(self.isEmpty()==1):
            print("Stack underflow");
        else:
            temp=self.top;
            self.top -= 1;
            return self.arr[temp];

def strReverse(str):
    stack1 = Stack(len(str));
    for ch in str:
        stack1.push(ch);
    newStr = [];  # Empty list
    while (stack1.isEmpty() != True):
        newStr.append(stack1.pop());
    for x in newStr:
        print(x, end="");

str="vedant"
strReverse(str);






