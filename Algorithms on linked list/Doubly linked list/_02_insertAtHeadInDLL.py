class Node:
    def __init__(self,data):
        self.data=data;
        self.next=None;
        self.prev=None;

class LinkedList:
    def __init__(self):
        self.head=None;

    def insertAtHead(self,newData):
        newNode=Node(newData);
        temp=self.head;
        if(temp==None):   #For empty list
            self.head=newNode;
        else:
            newNode.next=temp;
            temp.pre=newNode;
            self.head=newNode;  #Reinitializing head node (important step)

    def printList(self):
        temp=self.head;
        while(temp!=None):
            print(temp.data,end=" ");
            temp=temp.next;
        print();

obj=LinkedList();
obj.insertAtHead(10);
obj.insertAtHead(20);
obj.insertAtHead(30);

obj.printList();
