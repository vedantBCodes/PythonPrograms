class Node:
    def __init__(self,data):
        self.data=data;
        self.next=None;

class LinkedList:
    def __init__(self):
        self.head=None;

    def insertAtTail(self,newData):
        newNode = Node(newData);
        if not self.head:
            self.head=newNode;     # If list is empty, make new node the head
            return
        temp=self.head;
        while(temp.next!=None):    # Traverse to the last node
            temp=temp.next;
        temp.next=newNode;         # Set the next of last node to new node

    def lengthOfAList(self):
        temp=self.head;
        cnt=0;
        while(temp!=None):
            temp=temp.next;
            cnt+=1;
        return cnt;

obj=LinkedList()
obj.insertAtTail(10);
obj.insertAtTail(20);
obj.insertAtTail(30);
obj.insertAtTail(40);

print(f"Length of a given list is : {obj.lengthOfAList()}");