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
            self.top-=1;

    def print(self):   #Prints the whole stack elemets by printing every element and removing it (SO be carefull before use)
        while(self.top!=-1):
            print(self.arr[self.top],end=" ");
            self.top-=1;

    def peek(self):
        if(self.isEmpty()==1):
            print("Stack is empty");
        else:
            print(self.arr[self.top]);

st=Stack(5);
st.peek();
st.push(10);
st.peek();
st.push(20);
st.peek();
st.push(30);
st.peek();
st.push(40);
st.peek();
st.push(50);
st.peek();
st.push(60);

# st.print();
st.pop();
st.peek();
st.pop();
st.peek();
st.pop();
st.peek();
st.pop();
st.peek();
st.pop();
st.peek();
st.pop();





