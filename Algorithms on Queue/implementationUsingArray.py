# Implementation of Stack using array (Static)

# Defining Queue class

class Queue:
    def __init__(self,size):
        self.arr=[0] * size;  #Defining an empty array with size=size
        self.size=size;  #Initializing value of size with size
        self.rare=0;    #Initializing rare variable with 0 which represents the number of inserted elements
        self.front=0;   #Initializing front variable with 0 which represents the number of deleted elements

    def isEmpty(self):
        if(self.rare==self.front):
            return 1;
        else:
            return 0;

    def isFull(self):
        if(self.rare==self.size): #According to this , we can only insert <size> number of elements even if we delete an element
            return 1;
        else:
            return 0;

    def insert(self,element):
        if(self.isFull()==1):
            print("Queue is full");
        else:
            self.arr[self.rare]=element;
            self.rare+=1;

    def delete(self):  # deleting frontmost element
        if(self.isEmpty()==1):
            print("Queue is empty");
        else:
            self.front+=1;

    def display(self):
        for i in range(self.front,self.rare):
            print(self.arr[i],end=" ");
        # print(self.arr[1]);


q1=Queue(5);

q1.insert(10);
q1.insert(20);
q1.insert(30);
q1.delete();

q1.insert(40);
q1.insert(50);
q1.insert(60); #This won't be inserted as the array size is 5 , we have already inserted 5 elements before ,it won't add even if we delete add the existing elements

q1.display();

