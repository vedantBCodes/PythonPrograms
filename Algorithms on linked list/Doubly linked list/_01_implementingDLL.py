class Node:
    def __init__(self,data):
        self.data=data;
        self.next=None;
        self.prev=None;

class LinkedList:
    def __init__(self):
        self.head=None;

    def printList(self):
        temp=self.head;
        while(temp!=None):
            print(temp.data,end=" ");
            temp=temp.next;
        print();

obj=LinkedList();
obj.printList();
