# Implementation of Stack using Linked list (Dynamic)

# Defining Node

class Node:
    def __init__(self,data):
        self.data=data;
        self.next=None;

class LinkedList:
    def __init__(self):
        self.top=None;   #Here top represents a node

    def push(self,data):
        newNode=Node(data);
        newNode.next=self.top;
        self.top=newNode;

    def pop(self):
        if(self.top==None):
            print("Stack underflow");
        else:
            self.top=self.top.next;

    def peek(self):
        if (self.top == None):
            print("Stack is empty");
        else:
            print(self.top.data);

    def display(self):
        if(self.top==None):
            print("Stack is empty");
        else:
            currentNode=self.top;
            while(currentNode!=None):
                print(currentNode.data,end=" ");
                currentNode=currentNode.next;


st=LinkedList();

st.push(10);
st.peek();
st.push(20);
st.peek();
st.push(30);
st.peek();
st.push(40);
st.peek();

st.display();
print();
st.pop();
st.peek();

st.display();
