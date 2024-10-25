# Creating Node class which represents each element in the linked list
class Node:
    def __init__(self,data):   #Parameterized constructor
        self.data=data;
        self.next=None;

# LinkedList class to handle the linked list operations
class LinkedList:
        def __init__(self):     #Parameterized constructor
            self.head=None;

        def  insertAtHead(self,Newdata):
            newNode=Node(Newdata);  #Created an object of Node class with data = newData and next = None i.e created a node with data=newData and next pointer=None
            newNode.next=self.head;   # New node points to current head
            self.head=newNode;         # Update head to new node

        def print(self):
            temp=self.head;
            while(temp!=None):
                print(temp.data,end=" ");
                temp=temp.next;

obj=LinkedList();
obj.insertAtHead(10);
obj.insertAtHead(20);
obj.insertAtHead(30);

obj.print();



