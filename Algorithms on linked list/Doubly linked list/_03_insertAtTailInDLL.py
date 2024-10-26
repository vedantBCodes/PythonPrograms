class Node:
    def __init__(self,data):
        self.data=data;
        self.next=None;
        self.prev=None;

class LinkedList:
    def __init__(self):
        self.head=None;

    def insertAtTail(self,newData):
        newNode=Node(newData);
        temp=self.head;
        if(temp==None):
            self.head=newNode;
            return;
        while(temp.next!=None):
            temp=temp.next;
        temp.next=newNode;
        newNode.prev=temp;

    def printList(self):
        temp=self.head;
        while(temp!=None):
            print(temp.data,end=" ");
            temp=temp.next;
        print();

obj=LinkedList();
obj.insertAtTail(10);
obj.insertAtTail(20);
obj.insertAtTail(30);

obj.printList();