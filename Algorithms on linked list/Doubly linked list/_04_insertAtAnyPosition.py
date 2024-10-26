class Node:
    def __init__(self,data):
        self.data=data;
        self.next=None;
        self.prev=None;

class LinkedList:
    def __init__(self):
        self.head=None;

    def insertAtAnyPosition(self,pos,newData):
        newNode=Node(newData);
        temp=self.head;

        # If the list is empty
        if (self.head == None):
            self.head = newNode;
            return

        # Insert at head
        if (pos == 1):
            newNode.next = self.head;
            self.head = newNode;
            return

        # Insert at any position
        temp = self.head;
        cnt = 1;
        while (cnt < pos - 1 and temp is not None):
             temp = temp.next;
             cnt += 1;

        temp2 = temp.next;
        # Inserting at last position
        if (temp.next == None):
            temp.next = newNode;
        else:
        # Inserting at other positions
            temp.next = newNode;
            newNode.next = temp2;
            newNode.prev=temp;

    def printList(self):
        temp=self.head;
        while(temp!=None):
            print(temp.data,end=" ");
            temp=temp.next;
        print();

obj=LinkedList();
obj.insertAtAnyPosition(1,10);
obj.insertAtAnyPosition(2,20);
obj.insertAtAnyPosition(3,30);
obj.insertAtAnyPosition(2,40);

obj.printList();