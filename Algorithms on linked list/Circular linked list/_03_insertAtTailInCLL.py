class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insertAtTail(self, data):
    newNode = Node(data)
    if not self.head:  # List is empty
        self.head = newNode
        newNode.next = self.head  # Pointing to itself
    else:
        temp = self.head
        while temp.next != self.head:  # Traverse to the last node
            temp = temp.next
        temp.next = newNode
        newNode.next = self.head  # Make the list circular