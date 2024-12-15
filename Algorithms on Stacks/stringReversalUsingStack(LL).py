class Node:
    def __init__(self,data):
        self.data=data;
        self.next=None;

class Stack:
    def __init__(self):
        self.top=None;

    def isEmpty(self):
        if(self.top==None):
            return 1;
        else:
            return 0;

    def push(self,element):
        newNode=Node(element);
        newNode.next=self.top;
        self.top=newNode;

    def pop(self):
        if(self.isEmpty()==True):
             print("Stack is empty");
        else:
             temp=self.top.data;
             self.top=self.top.next;
             return temp;

def strReverse(str):
    stack1 = Stack();
    for ch in str:
        stack1.push(ch);
    newStr = [];  # Empty list
    while (stack1.isEmpty() != True):
        newStr.append(stack1.pop());
    for x in newStr:
        print(x, end="");

str="vedant"
strReverse(str);
