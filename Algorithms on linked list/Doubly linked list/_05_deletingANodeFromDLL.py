class Node:
    def __init__(self,data):
        self.data=data;
        self.next=None;
        self.prev=None;

class LinkedList:
    def __init__(self):
        self.head=None;

    def insertAtTail(self, newData):
        newNode = Node(newData);
        temp = self.head;
        if (temp == None):
            self.head = newNode;
            return;
        while (temp.next != None):
            temp = temp.next;
        temp.next = newNode;
        newNode.pre=temp;

    def deleteANode(self,newData):
        currentNode=self.head;

        # If head node itself holds the key
        if(currentNode.data==newData):
            self.head=currentNode.next;
            currentNode=None;
            return ;

        # Search for the key to be deleted
        preNode=None;
        while(currentNode!=None and currentNode.data!=newData):
            preNode=currentNode;
            currentNode=currentNode.next;

        # If key is not present
        if currentNode is None:
            print("Key is not present");
            return

        preNode.next=currentNode.next;
        currentNode.next=None;
        currentNode.prev=preNode;
        temp = None   # Clear the deleted node

    def printList(self):
        temp = self.head;
        while (temp != None):
            print(temp.data, end=" ");
            temp = temp.next;
        print();

obj=LinkedList();
obj.insertAtTail(10);
obj.insertAtTail(20);
obj.insertAtTail(30);
obj.insertAtTail(40);
print("Linked list before deletion",end=": ");
obj.printList();

print("Linked list after deletion",end=": ");
obj.deleteANode(30);
obj.printList();