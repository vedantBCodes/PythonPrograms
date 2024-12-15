# Implementation of Queue using Linked list (Dynamic)

# Defining Node

class Node:
    def __init__(self,data):
        self.data=data;
        self.next=None;

class Queue:
    def __init__(self):
        self.front=None;
        self.rare=None;

    def insert(self,data):
        newNode=Node(data);
        if(self.rare==None):  # i.e queue is empty , then both front and rare will point to the newNode
            self.rare=newNode;
            self.front=newNode;
        else:
            #Attach the new node to the end of the queue and update rare
            self.rare.next=newNode;
            self.rare=newNode;

    def delete(self):
        if(self.front==None):
            print("Queue is empty");
        else:
            self.front=self.front.next;
            #if queue becomes empty after removal then set rare to None
            if(self.front==None):
                self.rare=None;

    def display(self):
        if(self.front==None):
            print("Queue is empty");
        else:
            temp=self.front;
            while(temp!=None):
                print(temp.data,end=" ");
                temp=temp.next;
            print();

q1=Queue();

q1.insert(10);
q1.insert(20);
q1.insert(30);
q1.insert(40);
q1.insert(50);

q1.display();

q1.delete();


q1.display();
