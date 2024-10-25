class Node:
    def __init__(self,data):
        self.data=data;
        self.next=None;

class LinkedList:
    def __init__(self):
        self.head=None;

    def insertAtPosition(self,pos,newData):
        newNode=Node(newData);

        # If the list is empty
        if(self.head==None):
            self.head = newNode;
            return

        # Insert at head
        if(pos==1):
            newNode.next=self.head;
            self.head=newNode;
            return

        # Insert at any position
        temp=self.head;
        cnt=1;
        while(cnt<pos-1 and temp is not None):
            temp=temp.next;
            cnt+=1;

        temp2=temp.next;
        # Inserting at last position
        if (temp.next == None):
            temp.next = newNode;
        else:
        # Inserting at other positions
            temp.next=newNode;
            newNode.next = temp2;


    def printList(self):
        temp=self.head;
        while(temp!=None):
            print(temp.data,end=" ");
            temp=temp.next;
        print();

obj=LinkedList();
obj.insertAtPosition(1,10);
obj.printList();

obj.insertAtPosition(2,20);
obj.printList();

obj.insertAtPosition(1,30);
obj.printList();

obj.insertAtPosition(3,40);
obj.printList();

obj.insertAtPosition(4,50);
obj.printList();
