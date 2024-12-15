class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def insertAtHead(self, data):
    newNode = Node(data)
    if not self.head:  # List is empty
        self.head = newNode
        newNode.next = self.head  # Pointing to itself i.e making CLL
    else:
        temp = self.head
        while temp.next != self.head:  # Traverse to the last node
            temp = temp.next
            
        newNode.next = self.head
        self.head = newNode   # Setting new head node
        temp.next = self.head  # Update last node's next pointer
